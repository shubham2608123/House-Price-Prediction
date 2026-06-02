import streamlit as st
import pandas as pd
import joblib

# Page Configuration for wider layout
st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")

# Custom CSS for slight styling adjustments (like center aligning headers)
st.markdown("""
<style>
    .center-text {
        text-align: center;
    }
    .stButton>button {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_artifacts():
    model = joblib.load('model/house_price_model.pkl')
    columns = joblib.load('model/model_columns.pkl')
    return model, columns

model, columns = load_artifacts()

# Extract valid locations (removing 'location_' prefix)
locations = [col.replace("location_", "") for col in columns if col.startswith("location_")]

# UI Layout
st.markdown("<h1 class='center-text'>Welcome to Bangalore House Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='center-text' style='font-size:18px; margin-bottom: 2rem;'>Want to predict the price of a new House in Bangalore? Try filling the details below:</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    location = st.selectbox("Select the Location:", locations)
    bath_input = st.text_input("Enter Number of Bathrooms:", placeholder="Enter Number of bathrooms")

with col2:
    bhk_input = st.text_input("Enter BHK:", placeholder="Enter BHK")
    sqft_input = st.text_input("Enter Total Square Feet:", placeholder="Enter Total Square Feet")

# Large primary button at the bottom
st.write("") # some spacing
predict_btn = st.button("Predict Price", type="primary", use_container_width=True)

if predict_btn:
    try:
        # Parse inputs
        sqft = float(sqft_input)
        bath = float(bath_input)
        bhk = float(bhk_input)
        
        # Create a zero-filled dataframe for prediction
        input_data = pd.DataFrame(columns=columns)
        input_data.loc[0] = 0
        
        # Fill numerical features
        if 'total_sqft' in input_data.columns:
            input_data['total_sqft'] = sqft
        if 'bath' in input_data.columns:
            input_data['bath'] = bath
        if 'bhk' in input_data.columns:
            input_data['bhk'] = bhk
        # If there's a balcony feature, default to 0 as it is not in the form
            
        # One-hot encode the selected location
        location_column = "location_" + location
        if location_column in input_data.columns:
            input_data[location_column] = 1
            
        # Predict
        prediction = model.predict(input_data)
        
        # Display Result
        st.success(f"Estimated Price: ₹ {prediction[0]:.2f} Lakhs")
        
    except ValueError:
        st.error("Please ensure you have entered valid numbers for BHK, Bathrooms, and Total Square Feet.")
    except Exception as e:
        st.error(f"Prediction error: {e}")
