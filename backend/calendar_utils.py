import os
from datetime import datetime
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    SERVICE_ACCOUNT_FILE = 'service_account.json'
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    return service

def create_event(summary, description, start_time, end_time):
    service = get_calendar_service()
    calendar_id = '096faed568627037bf854711076720000cd895883ca42e45bf216b8d31c471e5@group.calendar.google.com'

    # User input assumed to be in IST
    # 🚨 Do not apply any timezone conversions. Just send the raw datetime strings.

    # Example input: '2025-07-02T03:00:00'
    # Google will add +5:30 hours and display 3:00 AM IST correctly.

    event = {
        'summary': summary,
        'description': description,
        'start': {'dateTime': start_time, 'timeZone': 'UTC'},  # Force UTC but send raw time
        'end': {'dateTime': end_time, 'timeZone': 'UTC'},
    }

    print("Sending to Google Calendar:")
    print("Start Time Sent:", start_time)
    print("End Time Sent:", end_time)

    try:
        event_result = service.events().insert(calendarId=calendar_id, body=event).execute()
        return event_result
    except HttpError as error:
        print(f"An error occurred: {error}")
        raise error
