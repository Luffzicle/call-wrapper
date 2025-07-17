from datetime import date
import streamlit as st
import pandas as pd

# Set up session state to store inputs
if 'submitted_data' not in st.session_state:
    st.session_state.submitted_data = []

st.set_page_config(page_title="Interest Capture Tool", layout="centered")
st.title("📝 Interest Capture Form")

# Basic Details
with st.form("interest_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    user_id = st.text_input("User ID")
    dob = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())

    # Interest Dropdown
    interest = st.selectbox("Select Interest", ["Select", "Football", "Basketball", "Tennis", "Cricket"])

    # Conditional Fields Based on Interest
    details = {}
    if interest == "Football":
        details['Region'] = st.selectbox("Region", ["Europe", "America", "Asia"])
        details['Favorite Player'] = st.selectbox("Favorite Player", ["Messi", "Ronaldo", "Mbappe"])
        details['Position'] = st.selectbox("Position", ["Winger", "Defender", "Midfielder", "Goalkeeper"])
    elif interest == "Basketball":
        details['League'] = st.selectbox("League", ["NBA", "EuroLeague"])
        details['Position'] = st.selectbox("Position", ["Guard", "Forward", "Center"])
        details['Favorite Player'] = st.selectbox("Favorite Player", ["LeBron James", "Stephen Curry", "Giannis"])
    elif interest == "Tennis":
        details['Favorite Surface'] = st.selectbox("Favorite Surface", ["Clay", "Grass", "Hard"])
        details['Handedness'] = st.selectbox("Play Style", ["Left-handed", "Right-handed"])
        details['Favorite Player'] = st.selectbox("Favorite Player", ["Federer", "Nadal", "Djokovic"])
    elif interest == "Cricket":
        details['Format'] = st.selectbox("Preferred Format", ["Test", "ODI", "T20"])
        details['Favorite Player'] = st.selectbox("Favorite Player", ["Kohli", "Root", "Smith", "Babar"])
        details['Role'] = st.selectbox("Role", ["Batsman", "Bowler", "All-rounder", "Wicketkeeper"])

    submitted = st.form_submit_button("Submit")

    if submitted:
        record = {
            "Name": name,
            "ID": user_id,
            "DOB": dob.strftime("%Y-%m-%d"),
            "Interest": interest
        }
        record.update(details)
        st.session_state.submitted_data.append(record)
        st.success("Submission recorded!")

# Show collected data in a table
if st.session_state.submitted_data:
    df = pd.DataFrame(st.session_state.submitted_data)
    st.write("### Submitted Records")
    st.dataframe(df)

    # Export to Excel
    def convert_df(df):
        return df.to_excel(index=False, engine='openpyxl')

    st.download_button(
        label="📥 Download as Excel",
        data=convert_df(df),
        file_name="interest_submissions.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
