from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class EventType(str, Enum):
    APLN = "APLN"  # 응모형
    IMDT = "IMDT"  # 즉시당첨형


class EventStatus(str, Enum):
    SCHEDULED = "예정"
    IN_PROGRESS = "진행중"
    ENDED = "종료"


class Event(BaseModel):
    id: int
    code: str
    name: str
    type: EventType
    status: EventStatus
    startDate: datetime
    endDate: datetime
    participantCount: Optional[int] = 0
    winnerCount: Optional[int] = 0
    description: Optional[str] = None
    imageUrl: Optional[str] = None
    createdAt: datetime
    updatedAt: Optional[datetime] = None


class EventParticipant(BaseModel):
    id: int
    eventId: int
    userId: str
    userName: str
    email: Optional[str] = None
    phone: Optional[str] = None
    participatedAt: datetime
    isWinner: bool = False
    winningDate: Optional[datetime] = None


class EventWinner(BaseModel):
    id: int
    eventId: int
    participantId: int
    userId: str
    userName: str
    prizeInfo: Optional[str] = None
    winningDate: datetime
    isNotified: bool = False
    notifiedAt: Optional[datetime] = None


class EventStatistics(BaseModel):
    eventId: int
    totalParticipants: int
    uniqueParticipants: int
    totalWinners: int
    participationByDate: List[Dict[str, Any]]
    participationByHour: List[Dict[str, Any]]