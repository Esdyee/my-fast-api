from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class StatsPeriod(str, Enum):
    DAILY = "일별"
    WEEKLY = "주별"
    MONTHLY = "월별"
    YEARLY = "연별"


class StatsType(str, Enum):
    ACCESS = "접속"
    EVENT = "이벤트"
    NEWSLETTER = "뉴스레터"
    CONTENT = "콘텐츠"
    FP_ACTIVITY = "FP활동"


class AccessStats(BaseModel):
    date: datetime
    totalVisits: int
    uniqueVisitors: int
    pageViews: int
    avgSessionDuration: float
    bounceRate: float
    newVisitors: int
    returningVisitors: int


class EventStats(BaseModel):
    date: datetime
    totalEvents: int
    activeEvents: int
    totalParticipants: int
    totalWinners: int
    avgParticipationRate: float


class NewsletterStats(BaseModel):
    date: datetime
    totalSent: int
    totalOpened: int
    totalClicked: int
    avgOpenRate: float
    avgClickRate: float
    unsubscribeCount: int


class ContentStats(BaseModel):
    date: datetime
    contentType: str
    totalViews: int
    uniqueViewers: int
    totalShares: int
    avgEngagementTime: float


class FPActivityStats(BaseModel):
    date: datetime
    activeFPs: int
    totalLogins: int
    contentViews: int
    contentShares: int
    customerInteractions: int