import streamlit as st
import requests
from datetime import datetime, time

st.title("Google Calendar Event Creator")

summary = st.text_input("Event Summary")
description = st.text_area("Event Description")

# Date pickers
start_date = st.date_input("Start Date")
st.write("Start Time:")
col1, col2 = st.columns(2)
with col1:
    start_hour = st.number_input("Hour (0-23)", min_value=0, max_value=23, step=1, key="start_hour")
with col2:
    start_minute = st.number_input("Minute (0-59)", min_value=0, max_value=59, step=1, key="start_minute")

end_date = st.date_input("End Date")
st.write("End Time:")
col3, col4 = st.columns(2)
with col3:
    end_hour = st.number_input("Hour (0-23)", min_value=0, max_value=23, step=1, key="end_hour")
with col4:
    end_minute = st.number_input("Minute (0-59)", min_value=0, max_value=59, step=1, key="end_minute")

if st.button("Create Event"):
    try:
        # Combine date and time into ISO format
        start_time = time(start_hour, start_minute)
        end_time = time(end_hour, end_minute)

        start_datetime = datetime.combine(start_date, start_time).isoformat()
        end_datetime = datetime.combine(end_date, end_time).isoformat()

        url = "https://tailortalkagent-production.up.railway.app/create_event/"
        payload = {
            "summary": summary,
            "description": description,
            "start_time": start_datetime,
            "end_time": end_datetime
        }

        response = requests.post(url, params=payload)

        if response.status_code == 200:
            st.success("Event Created Successfully!")
            st.json(response.json())
        else:
            st.error("Failed to create event.")
    except Exception as e:
        st.error(f"Error: {str(e)}")
