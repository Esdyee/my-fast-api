from fastapi import FastAPI
from app.models.event import Event, EventParticipant, EventWinner, EventStatistics
from app.api import events

app = FastAPI(title="Event Management API")

app.include_router(events.router)

@app.get("/")
async def root():
    return {"message": "Event Management API is running"} 