from fastapi import APIRouter, HTTPException
from typing import List
from app.models.event import Event, EventParticipant, EventWinner, EventStatistics

router = APIRouter(
    prefix="/events",
    tags=["events"]
)

@router.get("/", response_model=List[Event])
async def get_events():
    # TODO: 실제 데이터베이스 연동 필요
    return []

@router.get("/{event_id}", response_model=Event)
async def get_event(event_id: int):
    # TODO: 실제 데이터베이스 연동 필요
    raise HTTPException(status_code=404, detail="Event not found")

@router.post("/", response_model=Event)
async def create_event(event: Event):
    # TODO: 실제 데이터베이스 연동 필요
    return event 