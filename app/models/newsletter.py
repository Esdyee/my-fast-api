from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class NewsletterStatus(str, Enum):
    DRAFT = "작성중"
    SCHEDULED = "예약"
    SENT = "발송완료"
    FAILED = "발송실패"


class Newsletter(BaseModel):
    id: int
    code: str
    title: str
    content: str
    status: NewsletterStatus
    scheduledDate: Optional[datetime] = None
    sentDate: Optional[datetime] = None
    recipientCount: int = 0
    openCount: int = 0
    clickCount: int = 0
    createdAt: datetime
    updatedAt: Optional[datetime] = None


class NewsletterRecipient(BaseModel):
    id: int
    newsletterId: int
    userId: str
    email: str
    sentAt: Optional[datetime] = None
    openedAt: Optional[datetime] = None
    clickedAt: Optional[datetime] = None
    isSent: bool = False
    isOpened: bool = False
    isClicked: bool = False