from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class SendGroupStatus(str, Enum):
    WAITING = "대기"
    IN_PROGRESS = "진행중"
    COMPLETED = "완료"
    ENDED = "종료"


class TouchType(str, Enum):
    EVENT = "이벤트"
    CONTENT = "터치콘텐츠"


class CustomerReactionType(str, Enum):
    VIEW = "조회"
    CLICK = "클릭"
    SHARE = "공유"
    PARTICIPATE = "참여"


class SendGroup(BaseModel):
    id: int
    groupCode: str
    groupName: str
    status: SendGroupStatus
    touchType: TouchType
    totalCount: int
    sentCount: int
    viewCount: int
    reactionCount: int
    startDate: datetime
    endDate: Optional[datetime] = None
    createdAt: datetime
    createdBy: str


class TouchTarget(BaseModel):
    id: int
    groupId: int
    targetType: TouchType
    targetId: int
    targetName: str
    targetCode: str
    description: Optional[str] = None
    thumbnailUrl: Optional[str] = None
    createdAt: datetime


class SendTarget(BaseModel):
    id: int
    groupId: int
    touchTargetId: int
    fpId: str
    fpName: str
    customerCount: int
    sentAt: Optional[datetime] = None
    status: SendGroupStatus


class CustomerReaction(BaseModel):
    id: int
    groupId: int
    customerId: str
    customerName: str
    fpId: str
    fpName: str
    reactionType: CustomerReactionType
    reactionAt: datetime
    contentId: Optional[int] = None
    contentName: Optional[str] = None


class TouchPoint(BaseModel):
    id: int
    type: TouchType
    code: str
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    keywords: List[str] = []
    thumbnailUrl: Optional[str] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    isActive: bool = True
    createdAt: datetime
    updatedAt: Optional[datetime] = None