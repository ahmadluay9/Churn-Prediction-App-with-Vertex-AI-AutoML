# Import libraries
import streamlit as st
import requests
import pandas as pd

# Title and Introduction
st.sidebar.title("🚀 Churn Prediction DEMO")
   
def automl():
    st.header("Vertex AI AutoML Model Prediction")
    st.write(
    """Predicting customer churn using Vertex AI AutoML model.
         This streamlit example uses a FastAPI service as backend.
         Visit this [URL](http://localhost:8000/docs) for FastAPI documentation.""")

    # Collect user input through Streamlit widgets
    user_id = st.text_input('User ID')
    age = st.text_input('Age')
    gender = st.radio('Gender',('Male','Female'))
    if gender=='Male':
        gender='M'
    else: 
        gender='F'
    region_category = st.radio('Region Category',('Town', 'City','Village'))
    membership_category = st.radio('Membership Category',('Premium Membership','Basic Membership','No Membership', 'Gold Membership','Silver Membership','Platinum Membership'))
    joining_date = st.text_input('Joining Date',value='2023-12-31',help='YYYY-MM-DD')
    joined_through_referral = st.radio('Joined Through Referral',('No','Yes'))
    preferred_offer_types = st.radio('Preferred Offer Types',('Credit/Debit Card Offers','Gift Vouchers/Coupons','Without Offers'))
    medium_of_operation = st.radio('Medium of Operation',('Smartphone','Desktop','Both'))
    internet_option = st.radio('Internet Option',('Mobile Data','Wi-Fi','Fiber Optic'))
    if internet_option=='Mobile Data':
        internet_option='Mobile_Data'
    elif internet_option=='Fiber Optic': 
        internet_option='Fiber_Optic'
    else:
        internet_option='Wi-Fi'
    last_visit_time = st.text_input('Last Visit Time',value='00:00:01',help='HH:mm: ss')
    days_since_last_login = st.text_input('Days Since Last Login')
    avg_time_spent = st.text_input('Average Time Spent')
    avg_transaction_value = st.text_input('Average Transaction Value')
    avg_frequency_login_days = st.text_input('Average Frequency Login Days')
    points_in_wallet = st.text_input('Points in Wallet')
    used_special_discount = st.radio('Used Special Discount',('No','Yes'))
    offer_application_preference = st.radio('Offer Application Preference',('No','Yes'))
    past_complaint = st.radio('Past Complaint',('No','Yes'))
    complaint_status = st.text_input('Complaint Status')
    feedback = st.text_input('Feedback')

    if st.button('Predict'):
        # Prepare the data for prediction
        data = {
            'user_id': user_id,
            'age': age,
            'gender': gender,
            'region_category': region_category,
            'membership_category': membership_category,
            'joining_date': joining_date,
            'joined_through_referral': joined_through_referral,
            'preferred_offer_types': preferred_offer_types,
            'medium_of_operation': medium_of_operation,
            'internet_option': internet_option,
            'last_visit_time': last_visit_time,
            'days_since_last_login': days_since_last_login,
            'avg_time_spent': avg_time_spent,
            'avg_transaction_value': avg_transaction_value,
            'avg_frequency_login_days': avg_frequency_login_days,
            'points_in_wallet': points_in_wallet,
            'used_special_discount': used_special_discount,
            'offer_application_preference': offer_application_preference,
            'past_complaint': past_complaint,
            'complaint_status': complaint_status,
            'feedback': feedback,
        }

        # Send the data to the FastAPI endpoint for prediction
        response = requests.post('http://backend:8000/vertexai_automl_prediction', json=data)

        # Display the prediction result
        result = response.json()
        st.dataframe(data)
        st.success(f'Prediction: {result["prediction"]}')

def tensorflow():
    st.header("Tensorflow Model Prediction")
    st.write(
    """Predicting customer churn using Tensorflow model.
         This streamlit example uses a FastAPI service as backend.
         Visit this [URL](http://localhost:8000/docs) for FastAPI documentation.""")

    # Collect user input through Streamlit widgets
    user_id = st.text_input('User ID')
    age = st.text_input('Age')
    gender = st.radio('Gender',('Male','Female'))
    if gender=='Male':
        gender='M'
    else: 
        gender='F'
    region_category = st.radio('Region Category',('Town', 'City','Village'))
    membership_category = st.radio('Membership Category',('Premium Membership','Basic Membership','No Membership', 'Gold Membership','Silver Membership','Platinum Membership'))
    joining_date = st.text_input('Joining Date',value='2023-12-31',help='YYYY-MM-DD')
    joined_through_referral = st.radio('Joined Through Referral',('No','Yes'))
    preferred_offer_types = st.radio('Preferred Offer Types',('Credit/Debit Card Offers','Gift Vouchers/Coupons','Without Offers'))
    medium_of_operation = st.radio('Medium of Operation',('Smartphone','Desktop','Both'))
    internet_option = st.radio('Internet Option',('Mobile Data','Wi-Fi','Fiber Optic'))
    if internet_option=='Mobile Data':
        internet_option='Mobile_Data'
    elif internet_option=='Fiber Optic': 
        internet_option='Fiber_Optic'
    else:
        internet_option='Wi-Fi'
    last_visit_time = st.text_input('Last Visit Time',value='00:00:01',help='HH:mm: ss')
    days_since_last_login = st.text_input('Days Since Last Login')
    avg_time_spent = st.text_input('Average Time Spent')
    avg_transaction_value = st.text_input('Average Transaction Value')
    avg_frequency_login_days = st.text_input('Average Frequency Login Days')
    points_in_wallet = st.text_input('Points in Wallet')
    used_special_discount = st.radio('Used Special Discount',('No','Yes'))
    offer_application_preference = st.radio('Offer Application Preference',('No','Yes'))
    past_complaint = st.radio('Past Complaint',('No','Yes'))
    complaint_status = st.text_input('Complaint Status')
    feedback = st.text_input('Feedback')

    if st.button('Predict'):
        # Prepare the data for prediction
        data = {
            'user_id': user_id,
            'age': age,
            'gender': gender,
            'region_category': region_category,
            'membership_category': membership_category,
            'joining_date': joining_date,
            'joined_through_referral': joined_through_referral,
            'preferred_offer_types': preferred_offer_types,
            'medium_of_operation': medium_of_operation,
            'internet_option': internet_option,
            'last_visit_time': last_visit_time,
            'days_since_last_login': days_since_last_login,
            'avg_time_spent': avg_time_spent,
            'avg_transaction_value': avg_transaction_value,
            'avg_frequency_login_days': avg_frequency_login_days,
            'points_in_wallet': points_in_wallet,
            'used_special_discount': used_special_discount,
            'offer_application_preference': offer_application_preference,
            'past_complaint': past_complaint,
            'complaint_status': complaint_status,
            'feedback': feedback,
        }

        # Send the data to the FastAPI endpoint for prediction
        response = requests.post('http://backend:8000/tensorflow_prediction', json=data)

        # Display the prediction result
        result = response.json()
        st.dataframe(data)
        st.success(f'Prediction: {result["prediction"]}')

# Radio button to choose between manual input and file upload
prediction_option = st.sidebar.radio("Choose Model", ["Vertex AI AutoML", "Tensorflow"])

# Conditionally display the appropriate prediction form
if prediction_option == "Vertex AI AutoML":
    automl()
elif prediction_option == "Tensorflow":
    tensorflow()

