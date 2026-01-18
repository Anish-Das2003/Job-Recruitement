import streamlit as st
import pandas as pd
import pickle

model=pickle.load(open('model.pkl','rb'))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ===================== HOME =====================
st.title("Employee & Placement App")

st.header("Placement Prediction")

sl_no = st.text_input("Serial No")
gender = st.selectbox("Gender", ["Male", "Female"])
ssc_p = st.number_input("SSC Percentage")
hsc_p = st.number_input("HSC Percentage")
degree_p = st.number_input("Degree Percentage")
workex = st.selectbox("Work Experience", ["Yes", "No"])
etest_p = st.number_input("E-test Percentage")
specialisation = st.selectbox("Specialisation", ["Mkt&HR", "Mkt&Fin"])
mba_p = st.number_input("MBA Percentage")


def prediction(sl_no,gender, ssc_p, hsc_p, degree_p, workex, etest_p, specialisation, mba_p):
    data = {
    'sl_no': [sl_no],
    'gender': [gender],
    'ssc_p': [ssc_p],
    'hsc_p': [hsc_p],
    'degree_p': [degree_p],
    'workex': [workex],
    'etest_p': [etest_p],
    'specialisation': [specialisation],
    'mba_p': [mba_p]
    }
    data = pd.DataFrame(data)
    
    data['gender'] = data['gender'].map({'M':1,"F":0})
    data['workex'] = data['workex'].map({"Yes":1,"No":0})
    data['specialisation'] = data['specialisation'].map({"Mkt&HR":1,"Mkt&Fin":0})
    scaled_df = scaler.fit_transform(data)
    result = model.predict(scaled_df).reshape(1, -1)
    return result[0]


if st.button("Predict"):
        result = prediction(sl_no, gender, ssc_p, hsc_p, degree_p,workex, etest_p, specialisation, mba_p)

        if result == 1:
            st.success("Placed")
            st.write("This candidate is suitable for your business")
        else:
            st.error("Not Placed")
            st.write("This candidate is not suitable for your business")