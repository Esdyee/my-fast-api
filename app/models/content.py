from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class ContentType(str, Enum):
    TCCT = "TCCT"  # 터치콘텐츠
    INVL = "INVL"  # 참여형 콘텐츠
    VIRL = "VIRL"  # 전파형 콘텐츠


class ContentStatus(str, Enum):
    DRAFT = "작성중"
    PUBLISHED = "발행"
    ARCHIVED = "보관"


class ContentCategory(str, Enum):
    INSURANCE = "보험"
    RETIREMENT = "은퇴"
    TAX = "세무"
    INVESTMENT = "투자"
    ESTATE = "부동산"
    EDUCATION = "교육"


class BaseContent(BaseModel):
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
    createdAt: datetime
    publishedAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class TouchContent(BaseContent):
    fileUrl: str
    fileSize: int
    fileType: str
    downloadCount: int = 0


class InteractiveContent(BaseContent):
    contentUrl: str
    duration: Optional[int] = None
    questionCount: Optional[int] = None
    completionRate: float = 0.0
    avgScore: Optional[float] = None


class ViralContent(BaseContent):
    contentUrl: str
    viralReach: int = 0
    secondaryShares: int = 0
    engagementRate: float = 0.0