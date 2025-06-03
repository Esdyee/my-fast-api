from typing import List
from fastapi import APIRouter, Path, Query
from app.models.common import BaseResponse, PaginatedResponse
from app.schemas.newsletter import (
    NewsletterListRequest,
    NewsletterResponse,
    NewsletterDetailResponse,
    RecipientListRequest
)

router = APIRouter(prefix="/newsletter", tags=["뉴스레터"])


@router.post("/list/get", response_model=PaginatedResponse)
async def get_newsletter_list(request: NewsletterListRequest):
    """뉴스레터 목록 조회"""
    newsletters = [
        {
            "id": 1,
            "code": "NL20240101",
            "title": "1월 금융 뉴스레터",
            "status": "발송완료",
            "sentDate": "2024-01-01T09:00:00",
            "recipientCount": 5000,
            "openCount": 3500,
            "clickCount": 1200,
            "openRate": 70.0,
            "clickRate": 24.0
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": newsletters},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": request.page,
            "pageSize": request.size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.get("/{newsletter_id}/get", response_model=BaseResponse)
async def get_newsletter_detail(newsletter_id: int = Path(..., description="뉴스레터 ID")):
    """뉴스레터 상세 조회"""
    newsletter = {
        "id": newsletter_id,
        "code": "NL20240101",
        "title": "1월 금융 뉴스레터",
        "content": "<h1>2024년 1월 금융 뉴스레터</h1><p>새해 금융 트렌드를 소개합니다.</p>",
        "status": "발송완료",
        "sentDate": "2024-01-01T09:00:00",
        "recipientCount": 5000,
        "openCount": 3500,
        "clickCount": 1200,
        "openRate": 70.0,
        "clickRate": 24.0,
        "createdAt": "2023-12-20T10:00:00",
        "settings": {
            "targetGroup": "all",
            "excludeGroups": []
        }
    }
    
    return BaseResponse(isSuccess=True, data=newsletter)


@router.post("/{newsletter_id}/recipient/list/get", response_model=PaginatedResponse)
async def get_recipient_list(
    newsletter_id: int = Path(..., description="뉴스레터 ID"),
    request: RecipientListRequest = ...
):
    """뉴스레터 수신자 목록 조회"""
    recipients = [
        {
            "id": 1,
            "userId": "user001",
            "email": "user001@example.com",
            "sentAt": "2024-01-01T09:00:00",
            "openedAt": "2024-01-01T10:30:00",
            "clickedAt": "2024-01-01T10:35:00",
            "isSent": True,
            "isOpened": True,
            "isClicked": True
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": recipients},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": request.page,
            "pageSize": request.size,
            "hasNext": False,
            "hasPrevious": False
        }
    )