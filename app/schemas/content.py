from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field
from app.models.content import ContentType, ContentStatus, ContentCategory


class ContentListRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)
    type: Optional[ContentType] = None
    category: Optional[ContentCategory] = None
    status: Optional[ContentStatus] = None
    searchKeyword: Optional[str] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None


class ContentResponse(BaseModel):
    id: int
    code: str
    type: ContentType
    title: str
    description: Optional[str] = None
    category: ContentCategory
    status: ContentStatus
    keywords: List[str] = []
    thumbnailUrl: Optional[str] = None
    viewCount: int = 0
    shareCount: int = 0
    publishedAt: Optional[datetime] = None


class TouchContentResponse(ContentResponse):
    fileUrl: str
    fileSize: int
    fileType: str
    downloadCount: int = 0


class InteractiveContentResponse(ContentResponse):
    contentUrl: str
    duration: Optional[int] = None
    questionCount: Optional[int] = None
    completionRate: float = 0.0
    avgScore: Optional[float] = None


class ViralContentResponse(ContentResponse):
    contentUrl: str
    viralReach: int = 0
    secondaryShares: int = 0
    engagementRate: float = 0.0


class ContentCreateRequest(BaseModel):
    code: str
    type: ContentType
    title: str
    description: Optional[str] = None
    category: ContentCategory
    keywords: List[str] = []
    thumbnailUrl: Optional[str] = None
    contentData: Dict[str, Any]  # Type-specific data


class ContentUpdateRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[ContentCategory] = None
    keywords: Optional[List[str]] = None
    thumbnailUrl: Optional[str] = None
    status: Optional[ContentStatus] = None
    contentData: Optional[Dict[str, Any]] = None