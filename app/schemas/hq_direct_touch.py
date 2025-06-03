from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field
from app.models.hq_direct_touch import SendGroupStatus, TouchType, CustomerReactionType


class SendGroupListRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)
    searchKeyword: Optional[str] = None
    status: Optional[SendGroupStatus] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None


class SendGroupResponse(BaseModel):
    id: int
    groupCode: str
    groupName: str
    status: SendGroupStatus
    touchType: TouchType
    totalCount: int
    sentCount: int
    viewCount: int
    reactionCount: int
    viewRate: float
    reactionRate: float
    startDate: datetime
    endDate: Optional[datetime] = None


class SendGroupEndRequest(BaseModel):
    groupIds: List[int]
    endReason: Optional[str] = None


class TouchTargetListRequest(BaseModel):
    groupId: int
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)


class TouchTargetResponse(BaseModel):
    id: int
    targetType: TouchType
    targetId: int
    targetName: str
    targetCode: str
    description: Optional[str] = None
    thumbnailUrl: Optional[str] = None
    sentCount: int
    viewCount: int


class SendTargetListRequest(BaseModel):
    groupId: int
    touchTargetId: Optional[int] = None
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)


class SendTargetResponse(BaseModel):
    id: int
    fpId: str
    fpName: str
    customerCount: int
    sentAt: Optional[datetime] = None
    status: SendGroupStatus
    viewCount: int
    reactionCount: int


class CustomerReactionListRequest(BaseModel):
    groupId: int
    reactionType: Optional[CustomerReactionType] = None
    fpId: Optional[str] = None
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)


class CustomerReactionResponse(BaseModel):
    customerId: str
    customerName: str
    fpId: str
    fpName: str
    reactionType: CustomerReactionType
    reactionAt: datetime
    contentId: Optional[int] = None
    contentName: Optional[str] = None


class CustomerDetailRequest(BaseModel):
    groupId: int
    customerId: str


class CustomerDetailResponse(BaseModel):
    customerId: str
    customerName: str
    email: Optional[str] = None
    phone: Optional[str] = None
    fpId: str
    fpName: str
    reactions: List[Dict[str, Any]]
    contents: List[Dict[str, Any]]


class TouchPointEventListRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)
    searchKeyword: Optional[str] = None
    isActive: Optional[bool] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None


class TouchPointEventResponse(BaseModel):
    id: int
    code: str
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    keywords: List[str] = []
    thumbnailUrl: Optional[str] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    isActive: bool
    participantCount: int = 0


class TouchPointEventCreateRequest(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    keywords: List[str] = []
    thumbnailUrl: Optional[str] = None
    startDate: Optional[datetime] = None
    endDate: Optional[datetime] = None
    eventSettings: Optional[Dict[str, Any]] = None


class TouchPointContentListRequest(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)
    searchKeyword: Optional[str] = None
    category: Optional[str] = None
    isActive: Optional[bool] = None


class TouchPointContentResponse(BaseModel):
    id: int
    code: str
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    keywords: List[str] = []
    thumbnailUrl: Optional[str] = None
    isActive: bool
    viewCount: int = 0
    shareCount: int = 0


class TouchPointContentCreateRequest(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    keywords: List[str] = []
    thumbnailUrl: Optional[str] = None
    contentUrl: str
    fileType: Optional[str] = None
    fileSize: Optional[int] = None