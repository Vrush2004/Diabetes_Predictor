import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabeties_model = pickle.load(open(r"C:/Users/Dell/Desktop/Multiple_Disease_Predictor/Saved Models/diabetes_model.sav",'rb'))

heart_disease_model = pickle.load(open(r"C:\Users\Dell\Desktop\Multiple_Disease_Predictor\Saved Models\heart_disease_model.sav", 'rb'))

parkinsons_model = pickle.load(open(r"C:\Users\Dell\Desktop\Multiple_Disease_Predictor\Saved Models\parkinsons_model.sav", 'rb'))

# Sidebar for navigate
with st.sidebar:
    selected = option_menu('Multiple Disease System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons= ['activity','heart-pulse-fill','person'],
                           default_index=0)

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    #columns for input feilds
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Presure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
   
    
    
    #Code for Prediction
    diab_dignosis = ''
    
    #Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabeties_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
        if (diab_prediction[0] == 1):
            diab_dignosis = 'The Person is Diabetic'
        else:
            diab_dignosis = 'The Person is not Diabetic'
        
    st.success(diab_dignosis)
    

# Heart Disease Prediction Page

    
    
if (selected == 'Parkinsons Prediction'):
    st.title('Parkinsons Prediction using ML')