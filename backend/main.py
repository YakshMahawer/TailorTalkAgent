from fastapi import FastAPI
from backend.calendar_utils import create_event

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

@app.post("/create_event/")
def create_calendar_event(summary: str, description: str, start_time: str, end_time: str):
    event = create_event(summary, description, start_time, end_time)
    return {"message": "Event Created", "event": event}
