from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field
from app.models.newsletter import NewsletterStatus


class NewsletterListRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)
    searchKeyword: Optional[str] = None
    status: Optional[NewsletterStatus] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None


class NewsletterResponse(BaseModel):
    id: int
    code: str
    title: str
    status: NewsletterStatus
    scheduledDate: Optional[datetime] = None
    sentDate: Optional[datetime] = None
    recipientCount: int = 0
    openCount: int = 0
    clickCount: int = 0
    openRate: float = 0.0
    clickRate: float = 0.0


class NewsletterDetailResponse(NewsletterResponse):
    content: str
    createdAt: datetime
    updatedAt: Optional[datetime] = None
    settings: Optional[dict] = None


class RecipientListRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)
    searchKeyword: Optional[str] = None
    isOpened: Optional[bool] = None
    isClicked: Optional[bool] = None