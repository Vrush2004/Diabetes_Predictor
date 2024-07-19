import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabeties_model = pickle.load(open(r"C:/Users/Dell/Desktop/Multiple_Disease_Predictor/Saved Models/diabetes_model.sav"))

heart_disease_model = pickle.load(open(r"C:\Users\Dell\Desktop\Multiple_Disease_Predictor\Saved Models\heart_disease_model.sav"))

parkinsons_model = pickle.load(open(r"C:\Users\Dell\Desktop\Multiple_Disease_Predictor\Saved Models\parkinsons_model.sav"))