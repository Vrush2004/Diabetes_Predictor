import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabeties_model = pickle.load(open(r"C:/Users/Dell/Desktop/Multiple_Disease_Predictor/Saved Models/diabetes_model.sav", 'rb'))

heart_disease_model = pickle.load(open(r"C:\Users\Dell\Desktop\Multiple_Disease_Predictor\Saved Models\heart_disease_model.sav", 'rb'))

parkinsons_model = pickle.load(open(r"C:\Users\Dell\Desktop\Multiple_Disease_Predictor\Saved Models\parkinsons_model.sav", 'rb'))

#sidebar for navigate
with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System",
                           ['Diabetes Prediction','Heart Disease Prediction',
                            'Parkinson Prediction'],
                           default_index = 0)