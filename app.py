import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('disease_prediction_model.pkl')


symptoms = [
    'itching', 'nodal_skin_eruptions', 'chills', 'stomach_pain', 'muscle_wasting', 'vomiting', 
    'spotting_ urination', 'fatigue', 'weight_loss', 'cough', 'breathlessness', 'dark_urine', 
    'pain_behind_the_eyes', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'swelling_of_stomach', 
    'chest_pain', 'fast_heart_rate', 'pain_during_bowel_movements', 'dizziness', 'slurred_speech', 
    'knee_pain', 'muscle_weakness', 'unsteadiness', 'bladder_discomfort', 'passage_of_gases', 
    'depression', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'abnormal_menstruation', 
    'polyuria', 'lack_of_concentration', 'receiving_blood_transfusion', 'stomach_bleeding', 
    'prominent_veins_on_calf', 'scurring', 'silver_like_dusting', 'blister'
]

grouped_symptoms = [symptoms[i:i+10] for i in range(0, len(symptoms), 10)]

st.title("Disease Prediction Based on Symptoms")
st.write("This app predicts the disease based on the symptoms entered by the user.")


symptom_inputs = []
for idx, group in enumerate(grouped_symptoms):
    st.write(f"Select symptoms from Group {idx + 1}")
    selected_symptoms = st.multiselect(f"Symptoms Group {idx + 1}", group)
    symptom_inputs.extend([1 if symptom in selected_symptoms else 0 for symptom in group])

if st.button("Predict"):
    input_data = np.array(symptom_inputs).reshape(1, -1)
    
    prediction = model.predict(input_data)
    
    st.success(f"The model predicts: {prediction[0]}")

st.write("Please select symptoms from the drop-downs above and click on 'Predict' to get the result.")
