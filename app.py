import streamlit as st
import pandas as pd
from datetime import date

# Configure page
st.set_page_config(page_title="Interest Capture Tool", layout="centered")
st.title("📝 Interest Capture Form")

# Session state for storage
if "submitted_data" not in st.session_state:
    st.session_state.submitted_data = []

# Start form
with st.form("interest_form", clear_on_submit=True):
    # Basic Info
    name = st.text_input("Full Name")
    user_id = st.text_input("User ID")
    dob = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())

    # Interest selection
    interest = st.selectbox("Select Interest", ["", "Football", "Basketball", "Tennis", "Cricket"])

    # Conditional fields (shown immediately after interest is selected)
    interest_fields = {}
    if interest == "Football":
        interest_fields["Region"] = st.selectbox("Region", ["Europe", "America", "Asia"])
        interest_fields["Favorite Player"] = st.selectbox("Favorite Player", ["Messi", "Ronaldo", "Mbappe"])
        interest_fields["Position"] = st.selectbox("Position", ["Winger", "Defender", "Midfielder", "Goalkeeper"])
    elif interest == "Basketball":
        interest_fields["League"] = st.selectbox("League", ["NBA", "EuroLeague"])
        interest_fields["Position"] = st.selectbox("Position", ["Guard", "Forward", "Center"])
        interest_fields["Favorite Player"] = st.selectbox("Favorite Player", ["LeBron", "Curry", "Giannis"])
    elif interest == "Tennis":
        interest_fields["Surface"] = st.selectbox("Favorite Surface", ["Clay", "Grass", "Hard"])
        interest_fields["Handedness"] = st.selectbox("Play Style", ["Left-handed", "Right-handed"])
        interest_fields["Favorite Player"] = st.selectbox("Favorite Player", ["Federer", "Nadal", "Djokovic"])
    elif interest == "Cricket":
        interest_fields["Format"] = st.selectbox("Format", ["Test", "ODI", "T20"])
        interest_fields["Role"] = st.selectbox("Role", ["Batsman", "Bowler", "All-rounder", "Wicketkeeper"])
        interest_fields["Favorite Player"] = st.selectbox("Favorite Player", ["Kohli", "Smith", "Root", "Babar"])

    # Submit button
    submitted = st.form_submit_button("Submit")

    if submitted:
        entry = {
            "Name": name,
            "ID": user_id,
            "DOB": dob.strftime("%Y-%m-%d"),
            "Interest": interest
        }
        entry.update(interest_fields)
        st.session_state.submitted_data.append(entry)
        st.success("✅ Entry submitted successfully!")

# Show results if any
if st.session_state.submitted_data:
    df = pd.DataFrame(st.session_state.submitted_data)
    st.markdown("### 📋 Submitted Entries")
    st.dataframe(df)

    # Excel download
    def convert_df(df):
        return df.to_excel(index=False, engine='openpyxl')

    st.download_button(
        "📥 Download as Excel",
        data=convert_df(df),
        file_name="interest_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
