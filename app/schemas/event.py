from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field
from app.models.event import EventType, EventStatus


class EventListRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)
    searchType: Optional[str] = None
    searchKeyword: Optional[str] = None
    status: Optional[EventStatus] = None
    type: Optional[EventType] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None


class EventResponse(BaseModel):
    id: int
    code: str
    name: str
    type: EventType
    status: EventStatus
    startDate: datetime
    endDate: datetime
    participantCount: int = 0
    winnerCount: int = 0
    description: Optional[str] = None
    imageUrl: Optional[str] = None
    

class EventDetailResponse(EventResponse):
    createdAt: datetime
    updatedAt: Optional[datetime] = None
    settings: Optional[Dict[str, Any]] = None


class ParticipantListRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)
    searchKeyword: Optional[str] = None
    isWinner: Optional[bool] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None


class ParticipantResponse(BaseModel):
    id: int
    userId: str
    userName: str
    email: Optional[str] = None
    phone: Optional[str] = None
    participatedAt: datetime
    isWinner: bool = False
    winningDate: Optional[datetime] = None


class WinnerRegistrationRequest(BaseModel):
    participantIds: List[int]
    prizeInfo: Optional[str] = None
    notifyImmediately: bool = False


class EventStatisticsResponse(BaseModel):
    totalParticipants: int
    uniqueParticipants: int
    totalWinners: int
    participationRate: float
    winningRate: float
    dailyStats: List[Dict[str, Any]]
    hourlyStats: List[Dict[str, Any]]