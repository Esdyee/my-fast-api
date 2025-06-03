from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class SendingType(str, Enum):
    EVENT = "이벤트"
    NEWSLETTER = "뉴스레터"
    CONTENT = "콘텐츠"
    NOTIFICATION = "알림"


class SendingStatus(str, Enum):
    PENDING = "대기중"
    IN_PROGRESS = "발송중"
    COMPLETED = "완료"
    FAILED = "실패"
    CANCELLED = "취소"


class SendingChannel(str, Enum):
    EMAIL = "이메일"
    SMS = "SMS"
    PUSH = "푸시"
    KAKAO = "카카오알림톡"


class SendingTask(BaseModel):
    id: int
    type: SendingType
    title: str
    channel: SendingChannel
    status: SendingStatus
    targetCount: int
    sentCount: int = 0
    failedCount: int = 0
    scheduledAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None
    createdAt: datetime
    createdBy: str


class SendingTarget(BaseModel):
    id: int
    taskId: int
    userId: str
    contactInfo: str  # email, phone number, etc.
    status: SendingStatus
    sentAt: Optional[datetime] = None
    failedAt: Optional[datetime] = None
    failureReason: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None