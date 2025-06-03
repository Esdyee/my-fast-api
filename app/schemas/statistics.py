from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field
from app.models.statistics import StatsPeriod, StatsType


class StatsRequest(BaseModel):
    startDate: datetime
    endDate: datetime
    period: StatsPeriod = StatsPeriod.DAILY
    groupBy: Optional[List[str]] = None


class AccessStatsRequest(StatsRequest):
    deviceType: Optional[str] = None
    browser: Optional[str] = None
    os: Optional[str] = None


class EventStatsRequest(StatsRequest):
    eventId: Optional[int] = None
    eventType: Optional[str] = None


class NewsletterStatsRequest(StatsRequest):
    newsletterId: Optional[int] = None


class ContentStatsRequest(StatsRequest):
    contentType: Optional[str] = None
    contentId: Optional[int] = None


class FPActivityStatsRequest(StatsRequest):
    fpId: Optional[str] = None
    region: Optional[str] = None


class DashboardResponse(BaseModel):
    summary: Dict[str, Any]
    recentActivities: List[Dict[str, Any]]
    topContent: List[Dict[str, Any]]
    alerts: List[Dict[str, Any]]