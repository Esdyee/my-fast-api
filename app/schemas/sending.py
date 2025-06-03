from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field
from app.models.sending import SendingType, SendingStatus, SendingChannel


class SendingTaskListRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)
    type: Optional[SendingType] = None
    channel: Optional[SendingChannel] = None
    status: Optional[SendingStatus] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None


class SendingTaskResponse(BaseModel):
    id: int
    type: SendingType
    title: str
    channel: SendingChannel
    status: SendingStatus
    targetCount: int
    sentCount: int
    failedCount: int
    successRate: float
    scheduledAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None


class SendingTaskDetailResponse(SendingTaskResponse):
    startedAt: Optional[datetime] = None
    createdAt: datetime
    createdBy: str
    settings: Optional[Dict[str, Any]] = None


class SendingTargetListRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)
    status: Optional[SendingStatus] = None
    searchKeyword: Optional[str] = None


class SendingCreateRequest(BaseModel):
    type: SendingType
    title: str
    channel: SendingChannel
    targetIds: List[str]
    scheduledAt: Optional[datetime] = None
    settings: Optional[Dict[str, Any]] = None


class SendingRetryRequest(BaseModel):
    targetIds: Optional[List[int]] = None  # None means retry all failed
    retryFailedOnly: bool = True