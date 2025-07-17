import streamlit as st
import pandas as pd
from datetime import datetime

# Store form data
def get_interest_fields(interest):
    if interest == "Football":
        return {
            "Region": ["Europe", "South America", "North America"],
            "Player": ["Messi", "Ronaldo", "Mbappe"],
            "Position": ["Winger", "Defender", "Midfielder", "Goalkeeper"],
        }
    elif interest == "Basketball":
        return {
            "League": ["NBA", "EuroLeague"],
            "Position": ["Guard", "Forward", "Center"],
            "Player": ["LeBron", "Curry", "Giannis"]
        }
    elif interest == "Tennis":
        return {
            "Handedness": ["Left", "Right"],
            "Surface Preference": ["Grass", "Clay", "Hard"],
            "Favorite Player": ["Federer", "Nadal", "Djokovic"]
        }
    elif interest == "Cricket":
        return {
            "Format": ["Test", "ODI", "T20"],
            "Role": ["Batsman", "Bowler", "All-Rounder"],
            "Favorite Player": ["Kohli", "Root", "Smith"]
        }
    return {}

# Excel file name
EXCEL_FILE = "submissions.xlsx"

# Initialize Excel
def initialize_excel():
    try:
        pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        df = pd.DataFrame()
        df.to_excel(EXCEL_FILE, index=False)

# Save data to Excel
def save_data(data):
    try:
        df = pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        df = pd.DataFrame()

    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False)

# --- Streamlit App ---
st.set_page_config(page_title="Interest Collector", layout="centered")

st.title("📝 Interest Collection Tool")

with st.form("interest_form", clear_on_submit=True):
    st.subheader("Basic Info")
    name = st.text_input("Name")
    dob = st.date_input("Date of Birth")
    user_id = st.text_input("User ID")

    st.subheader("Interest Info")
    interest = st.selectbox("Select Interest", ["Football", "Basketball", "Tennis", "Cricket"])
    dynamic_fields = get_interest_fields(interest)
    
    field_responses = {}
    for label, options in dynamic_fields.items():
        field_responses[label] = st.selectbox(label, options)

    submitted = st.form_submit_button("Submit")

    if submitted:
        all_data = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": name,
            "DOB": dob,
            "User ID": user_id,
            "Interest": interest
        }
        all_data.update(field_responses)

        save_data(all_data)
        st.success("✅ Submitted successfully!")
