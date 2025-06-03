from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel


class BaseResponse(BaseModel):
    isSuccess: bool = True
    data: Optional[Any] = None
    message: Optional[str] = None


class PaginationRequest(BaseModel):
    page: int = 1
    size: int = 10
    sort: Optional[str] = None


class PaginationInfo(BaseModel):
    totalCount: int
    totalPages: int
    currentPage: int
    pageSize: int
    hasNext: bool
    hasPrevious: bool


class PaginatedResponse(BaseResponse):
    data: Optional[Dict[str, Any]] = None
    pagination: Optional[PaginationInfo] = None