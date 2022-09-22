
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open('diabetes_prediction.pkl', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_prediction.pkl', 'rb'))

parkinsons_model = pickle.load(open("parkinson_prediction.pkl", 'rb'))

# sidebar for navigation

with st.sidebar:

  selected = option_menu('Multiple Disease Prediction System', 
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                          icons = ['activity', 'heart', 'person'],
                          default_index=0)
                                                   
# Diabetes Prediction Page

if(selected == 'Diabetes Prediction'):
     
  # giving a title
  st.title("Diabetes Prediction")

  # getting the input data from the user
  # columns for input fields

  col1, col2, col3 = st.columns(3)

  with col1:
    Pregnancies = st.text_input('Number of Pregnancies')

  with col2:
     Glucose = st.text_input("Glucose Level(mg/dL) eg. 90") 

  with col3:
     BloodPressure = st.text_input("Blood Pressure(mmHg) eg. 80")

  with col1:
    SkinThickness = st.text_input("Skin Thickness(mm) eg. 20") 

  with col2:
    Insulin = st.text_input("Insulin Level(IU/mL) eg. 80")
    
  with col3:
    BMI = st.text_input("BMI value eg. 23.1")

  with col1: 
    DPF = st.text_input("DiabetesPedigreeFunction eg. 0.52")

  with col2:   
    Age = st.text_input("Age of the Person")       

  # code for prediction

  diab_diagnosis = ''

  #creating a button for prediction

  if st.button('Diabetes Test Result'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age]])
    
    if (diab_prediction[0] == 1):
        diab_diagnosis = "Sorry! You have diabetes."
    else:
        diab_diagnosis = "Great! You don't have diabetes."

  st.success(diab_diagnosis)

# Heart Disease Prediction Page

if(selected == 'Heart Disease Prediction'):
     
  # giving a title
  st.title("Heart Disease Prediction")

  # getting the input data from the user
  # columns for input fields

  col1, col2 = st.columns(2)

  with col1:
    age = st.text_input('Age of the person')

  with col2:
     sex = st.text_input("Sex (1 = Male; 0 = Female)") 

  with col1:
     cp = st.text_input("Chest pain type eg. (0–3)")

  with col2:
    trestbps = st.text_input("Resting Blood Pressure(mmHg) eg. 130") 

  with col1:
    chol = st.text_input("Serum Cholestrol(mg/dl) eg. 230")
    
  with col2:
    fbs = st.text_input("fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)")

  with col1: 
    restecg = st.text_input("Resting Electrocardiographic results eg. (0–2)")

  with col2:   
    thalach = st.text_input("Maximum Heart Rate Achieved eg. 170")
  
  with col1:
     exang = st.text_input("Exercise induced angina (1 = yes; 0 = no)")

  with col2: 
    oldpeak = st.text_input("ST depression induced by exercise eg. 2.3 ")

  with col1:   
    slope = st.text_input("Slope of the peak exercise ST segment eg. (0–2)")
  
  with col2:
     ca = st.text_input("Major vessels colored by flourosopy eg. (0–3) ")

  with col1:   
    thal = st.text_input("Thalassemia Defect eg. (0–2)")   


  # code for prediction

  heart_diagnosis = ''

  #creating a button for prediction

  if st.button('Heart Disease Test Result'):
    heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    if (heart_prediction[0] == 1):
        heart_diagnosis = "Heart disease detected. Please consult Doctor!"
    else:
        heart_diagnosis = "Great! You don't have Heart disease."

  st.success(heart_diagnosis) 

# Parkinsons Prediction Page

if(selected == 'Parkinsons Prediction'):
     
  # giving a title
  st.title("Parkinson's Disease Detection")

  # getting the input data from the user
  # columns for input fields

  col1, col2, col3 = st.columns(3)

  with col1:
    fo = st.text_input('MDVP:Fo(Hz) eg. 120.5')

  with col2:
    flo = st.text_input("MDVP:Flo(Hz) eg. 84.52") 

  with col3:
    jitter = st.text_input("MDVP:Jitter(Abs) eg. 0.00007")

  with col1:
    rap = st.text_input("MDVP:RAP eg. 0.00826") 

  with col2:
    ddp = st.text_input("Jitter:DDP eg. 0.01116")
    
  with col3:
    apq = st.text_input("MDVP:APQ eg. 0.021")

  with col1: 
    hnr = st.text_input("HNR eg. 22.52")

  with col2:   
    spread1 = st.text_input("spread1 eg. -4.476")  

  with col3:
    spread2 = st.text_input("spread2 eg. 0.245")
    
  with col1:
    ppe = st.text_input("PPE eg. 0.326")  


  # code for prediction

  parkinsons_diagnosis = ''

  #creating a button for prediction

  if st.button("Parkinson's Test Result"):
    parkinsons_prediction = parkinsons_model.predict([[fo, flo, jitter, rap, ddp, apq, hnr, spread1, spread2, ppe]])
    
    if (parkinsons_prediction[0] == 1):
        parkinsons_diagnosis = "The person has Parkinson disease."
    else:
        parkinsons_diagnosis = "The person does not have Parkinson disease."

  st.success(parkinsons_diagnosis)
