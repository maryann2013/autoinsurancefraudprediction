#!/usr/bin/env python
# coding: utf-8

# # Predict Auto Insurance Fraud

# In[7]:


import pickle
import numpy as np
import streamlit as st
import pandas as pd


# In[8]:


# load the model from disk
loaded_model = pickle.load(open('Streamlit_Autoinsurancefraud.pkl', 'rb'))


# In[9]:


# Creating the Titles and Image

st.title("Predict Auto Insurance fraud claim")
st.header("Predicting if a claim requested for an auto insurance policy is genuine or fraud")


# In[10]:


# create the dropdown menus for input fields

DropDown1 = pd.DataFrame({'insured_hobbies': ['chess', 'cross-fit','other'],
                          'policy_deductable': [500,1000,2000],
                          'police_report_available': ['YES','NO','other']})
DropDown2 = pd.DataFrame({'collision_type': ['Rear Collision', 'Side Collision', 'Front Collision','other'],
                          'incident_severity': ['Minor Damage','Total Loss','Major Damage','Trivial Damage'],
                          'incident_type': ['Multi-vehicle Collision','Single Vehicle Collision','Vehicle Theft','Parked Car']})
DropDown3 = pd.DataFrame({'authorities_contacted': ['Police', 'Fire', 'Ambulance','Other','None']})
DropDown4 = pd.DataFrame({'months_as_customer': ['0-50','51-100','101-150','151-200','201-250','251-300','301-350','351-400','401-450','451-500'],
                          'umbrella_limit': [0,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]})                        
DropDown5 = pd.DataFrame({'vehicle_claim': ['0-10000','10001-20000','20001-30000','30001-40000','40001-50000','50001-60000','60001-70000','70001-80000']})


# In[11]:


# take user inputs

insured_hobbies = st.selectbox('Hobbies',DropDown1['insured_hobbies'].unique())
policy_deductable = st.selectbox('Policy deductable',DropDown1['policy_deductable'].unique())
police_report_available = st.selectbox('Is Police Report available ?',DropDown1['police_report_available'].unique())
collision_type = st.selectbox('Type of collision',DropDown2['collision_type'].unique())
incident_severity = st.selectbox('Severity of incident',DropDown2['incident_severity'].unique())
incident_type = st.selectbox('Type of incident',DropDown2['incident_type'].unique())
authorities_contacted = st.selectbox('Type of authorities contacted',DropDown3['authorities_contacted'].unique())
months_as_customer = st.selectbox('Number of months with the insurer',DropDown4['months_as_customer'].unique())
umbrella_limit = st.selectbox('Select umbrella limit',DropDown4['umbrella_limit'].unique())
vehicle_claim = st.selectbox('Amount of vehicle claim requested',DropDown5['vehicle_claim'].unique())
number_of_vehicles_involved = st.slider("Number of vehicles involved", 1, 4)
bodily_injuries = st.slider("Number of injuries", 0, 2)
witnesses = st.slider("Number of witnesses", 0, 3)

# dealing with input passed by user in the app and converting them back to type understandable by the machine learning algorithm

# insured_hobbies
if insured_hobbies == 'chess':
    hobby = 0
else:
    if insured_hobbies == 'cross-fit':
        hobby = 1
    else:
        hobby = 2
        
# police_report_available
if police_report_available == 'other':
    report = 0
else:
    if police_report_available == 'NO':
        report = 1
    else:
        report = 2
        
# collision_type
if collision_type == 'other':
    collision = 0
else:
    if collision_type == 'Front Collision':
        collision = 1
    else:
        if collision_type == 'Rear Collision':
            collision = 2     
        else:
            collision = 3

# incident_severity
if incident_severity == 'Major Damage':
    severity = 0
else:
    if incident_severity == 'Minor Damage':
        severity = 1
    else:
        if incident_severity == 'Total Loss':
            severity = 2     
        else:
            severity = 3
        
# incident_type
if incident_type == 'Multi-vehicle Collision':
    incident = 0
else:
    if incident_type == 'Parked Car':
        incident = 1
    else:
        if incident_type == 'Single Vehicle Collision':
            incident = 2     
        else:
            incident = 3
        

# authorities_contacted
if authorities_contacted == 'Ambulance':
    authorities = 0
else:
    if authorities_contacted == 'Fire':
        authorities = 1
    else:
        if authorities_contacted == 'None':
            authorities = 2 
        else:
            if authorities_contacted == 'Other':
                authorities = 3     
            else:
                authorities = 4
        
# months_as_customer
if months_as_customer == '0-50':
    customer = 0
else:
    if months_as_customer == '101-150':
        customer = 1
    else:
        if months_as_customer == '151-200':
            customer = 2 
        else:
            if months_as_customer == '201-250':
                customer = 3 
            else:
                if months_as_customer == '251-300':
                    customer = 4 
                else:
                    if months_as_customer == '301-350':
                        customer = 5 
                    else:
                        if months_as_customer == '351-400':
                            customer = 6 
                        else:
                            if months_as_customer == '401-450':
                                customer = 7
                            else:
                                if months_as_customer == '451-500':
                                    customer = 8
                                else:
                                    customer = 9
        
# vehicle_claim
if vehicle_claim == '0-10000':
    claim = 0
else:
    if vehicle_claim == '10001-20000':
        claim = 1
    else:
        if vehicle_claim == '20001-30000':
            claim = 2 
        else:
            if vehicle_claim == '30001-40000':
                claim = 3 
            else:
                if vehicle_claim == '40001-50000':
                    claim = 4 
                else:
                    if vehicle_claim == '50001-60000':
                        claim = 5 
                    else:
                        if vehicle_claim == '60001-70000':
                            claim = 6 
                        else:
                            claim = 7
    


# In[12]:


# store the inputs

features = [umbrella_limit, hobby, policy_deductable, report, collision, severity, incident, authorities, customer, claim,
            number_of_vehicles_involved, bodily_injuries, witnesses]

# convert user inputs into an array for the model
int_features = [int(x) for x in features]
final_features = [np.array(int_features)]

if st.button('Predict'):
    prediction = loaded_model.predict(final_features)
    #st.balloons()
    if (prediction[0]) == 1:
        st.success('The claim reported is fraud.')
    else:
        st.success('The claim reported is genuine.')


# In[ ]:


# Save in C folder as 'streamlitpredictautoinsurancefraud' as python extension.

