import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Muat model
try:
    model = joblib.load('model_dropout_prediction.pkl')
except FileNotFoundError:
    st.error("❌ File 'model_dropout_prediction.pkl' tidak ditemukan. Pastikan file ada di direktori yang sama dengan app.py.")
    st.stop()

# Judul aplikasi
st.title("Prediksi Risiko Dropout Mahasiswa")

# Buat form untuk input
with st.form(key='prediction_form'):
    # Input dalam form
    gender = st.selectbox("Jenis Kelamin", ['Male', 'Female'])
    age_at_enrollment = st.slider("Usia Saat Mendaftar", 17, 40, 18)
    debtor = st.selectbox("Memiliki Utang", ['No', 'Yes'])
    scholarship_holder = st.selectbox("Penerima Beasiswa", ['No', 'Yes'])
    admission_grade = st.slider("Nilai Penerimaan", 100, 200, 150)
    curricular_units_1st_sem_approved = st.slider("Unit Disetujui Semester 1", 0, 10, 5)
    curricular_units_1st_sem_enrolled = st.slider("Unit Terdaftar Semester 1", 0, 10, 6)
    curricular_units_2nd_sem_approved = st.slider("Unit Disetujui Semester 2", 0, 10, 5)
    curricular_units_2nd_sem_enrolled = st.slider("Unit Terdaftar Semester 2", 0, 10, 6)

    # Tombol submit dalam form
    submit_button = st.form_submit_button(label="Prediksi")

# Logika prediksi setelah tombol ditekan
if submit_button:
    # Buat data input dengan nilai default realistis
    input_data = {
        'Marital_status': 'Single',
        'Application_mode': '1st phase',
        'Application_order': 1,
        'Course': 'Engineering',
        'Daytime_evening_attendance': 'Daytime',
        'Previous_qualification': 'High School',
        'Previous_qualification_grade': 140,
        'Nacionality': 'Portuguese',
        'Mothers_qualification': 'Basic',
        'Fathers_qualification': 'Basic',
        'Mothers_occupation': 'Other',
        'Fathers_occupation': 'Other',
        'Admission_grade': admission_grade,
        'Displaced': 'No',
        'Educational_special_needs': 'No',
        'Debtor': debtor,
        'Tuition_fees_up_to_date': 'Yes',
        'Gender': gender,
        'Scholarship_holder': scholarship_holder,
        'Age_at_enrollment': age_at_enrollment,
        'International': 'No',
        'Curricular_units_1st_sem_credited': 0,
        'Curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled,
        'Curricular_units_1st_sem_evaluations': 5,
        'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': 12,
        'Curricular_units_1st_sem_without_evaluations': 0,
        'Curricular_units_2nd_sem_credited': 0,
        'Curricular_units_2nd_sem_enrolled': curricular_units_2nd_sem_enrolled,
        'Curricular_units_2nd_sem_evaluations': 5,
        'Curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': 12,
        'Curricular_units_2nd_sem_without_evaluations': 0,
        'Unemployment_rate': 7.0,
        'Inflation_rate': 2.0,
        'GDP': 1.0
    }

    # Konversi ke DataFrame
    input_df = pd.DataFrame([input_data])

    # Encode variabel kategorikal menggunakan LabelEncoder baru
    categorical_cols = ['Marital_status', 'Application_mode', 'Course', 'Daytime_evening_attendance',
                       'Previous_qualification', 'Nacionality', 'Mothers_qualification', 'Fathers_qualification',
                       'Mothers_occupation', 'Fathers_occupation', 'Displaced', 'Educational_special_needs',
                       'Debtor', 'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 'International']
    
    le = LabelEncoder()
    for col in categorical_cols:
        input_df[col] = le.fit_transform(input_df[col])

    # Tambahkan fitur academic_risk
    input_df['academic_risk_1st_sem'] = input_df['Curricular_units_1st_sem_approved'] / input_df['Curricular_units_1st_sem_enrolled']
    input_df['academic_risk_1st_sem'] = input_df['academic_risk_1st_sem'].fillna(0)
    input_df['academic_risk_2nd_sem'] = input_df['Curricular_units_2nd_sem_approved'] / input_df['Curricular_units_2nd_sem_enrolled']
    input_df['academic_risk_2nd_sem'] = input_df['academic_risk_2nd_sem'].fillna(0)

    # Pastikan urutan kolom sesuai dengan yang digunakan saat melatih model
    feature_names = ['Marital_status', 'Application_mode', 'Application_order', 'Course', 
                     'Daytime_evening_attendance', 'Previous_qualification', 'Previous_qualification_grade',
                     'Nacionality', 'Mothers_qualification', 'Fathers_qualification', 'Mothers_occupation', 
                     'Fathers_occupation', 'Admission_grade', 'Displaced', 'Educational_special_needs', 
                     'Debtor', 'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 
                     'Age_at_enrollment', 'International', 'Curricular_units_1st_sem_credited', 
                     'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_evaluations', 
                     'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 
                     'Curricular_units_1st_sem_without_evaluations', 'Curricular_units_2nd_sem_credited', 
                     'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations', 
                     'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade', 
                     'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate', 
                     'Inflation_rate', 'GDP', 'academic_risk_1st_sem', 'academic_risk_2nd_sem']

    # Debug: Periksa apakah semua fitur ada di input_df
    missing_features = [col for col in feature_names if col not in input_df.columns]
    if missing_features:
        st.error(f"Fitur yang hilang di input_df: {missing_features}")
    else:
        # Pastikan urutan kolom sama
        input_df = input_df[feature_names]

        # Prediksi
        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)
        
        # Tampilan hasil prediksi dengan format baru
        st.write("📢 **Hasil Prediksi**")
        st.write(f"Status Prediksi: {prediction[0]}")
        st.write(f"Probabilitas Dropout: {probability[0][1]*100:.2f}%")
        if prediction[0] == 1:
            st.error("⚠️ Mahasiswa ini **berisiko tinggi untuk dropout**.")
        else:
            st.success("✅ Mahasiswa ini **tidak berisiko dropout**.")