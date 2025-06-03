from typing import List, Optional
from datetime import datetime
from fastapi import APIRouter, Query, HTTPException, Path
from app.models.common import BaseResponse, PaginatedResponse
from app.schemas.event import (
    EventListRequest,
    EventResponse,
    EventDetailResponse,
    ParticipantListRequest,
    ParticipantResponse,
    WinnerRegistrationRequest,
    EventStatisticsResponse
)

router = APIRouter(prefix="/event", tags=["이벤트"])


@router.post("/list/get", response_model=PaginatedResponse)
async def get_event_list(request: EventListRequest):
    """이벤트 목록 조회"""
    # Mock data for demonstration
    events = [
        {
            "id": 1,
            "code": "EVT20240101",
            "name": "신년 이벤트",
            "type": "APLN",
            "status": "진행중",
            "startDate": "2024-01-01T00:00:00",
            "endDate": "2024-01-31T23:59:59",
            "participantCount": 1234,
            "winnerCount": 10
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": events},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": request.page,
            "pageSize": request.size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.get("/{event_id}/get", response_model=BaseResponse)
async def get_event_detail(event_id: int = Path(..., description="이벤트 ID")):
    """이벤트 상세 조회"""
    event = {
        "id": event_id,
        "code": "EVT20240101",
        "name": "신년 이벤트",
        "type": "APLN",
        "status": "진행중",
        "startDate": "2024-01-01T00:00:00",
        "endDate": "2024-01-31T23:59:59",
        "participantCount": 1234,
        "winnerCount": 10,
        "description": "2024년 신년 맞이 특별 이벤트",
        "imageUrl": "/images/event/2024_newyear.jpg",
        "createdAt": "2023-12-15T10:00:00",
        "settings": {
            "maxParticipants": 10000,
            "maxWinners": 100,
            "participationLimit": 1
        }
    }
    
    return BaseResponse(isSuccess=True, data=event)


@router.post("/{event_id}/participant/list/get", response_model=PaginatedResponse)
async def get_participant_list(
    event_id: int = Path(..., description="이벤트 ID"),
    request: ParticipantListRequest = ...
):
    """이벤트 참여자 목록 조회"""
    participants = [
        {
            "id": 1,
            "userId": "user001",
            "userName": "홍길동",
            "email": "hong@example.com",
            "phone": "010-1234-5678",
            "participatedAt": "2024-01-05T14:30:00",
            "isWinner": False
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": participants},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": request.page,
            "pageSize": request.size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.post("/{event_id}/participant/excel/get")
async def download_participant_excel(event_id: int = Path(..., description="이벤트 ID")):
    """이벤트 참여자 엑셀 다운로드"""
    # In real implementation, this would return a file response
    return BaseResponse(
        isSuccess=True,
        data={"downloadUrl": f"/downloads/event_{event_id}_participants.xlsx"}
    )


@router.post("/{event_id}/winner/list/get", response_model=PaginatedResponse)
async def get_winner_list(
    event_id: int = Path(..., description="이벤트 ID"),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)
):
    """이벤트 당첨자 목록 조회"""
    winners = [
        {
            "id": 1,
            "userId": "user001",
            "userName": "홍길동",
            "prizeInfo": "1등 - 아이패드",
            "winningDate": "2024-01-31T15:00:00",
            "isNotified": True,
            "notifiedAt": "2024-01-31T15:30:00"
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": winners},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": page,
            "pageSize": size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.post("/{event_id}/winner/post")
async def register_winners(
    event_id: int = Path(..., description="이벤트 ID"),
    request: WinnerRegistrationRequest = ...
):
    """이벤트 당첨자 등록"""
    return BaseResponse(
        isSuccess=True,
        data={
            "registeredCount": len(request.participantIds),
            "message": "당첨자가 성공적으로 등록되었습니다."
        }
    )


@router.get("/{event_id}/statistics/get", response_model=BaseResponse)
async def get_event_statistics(event_id: int = Path(..., description="이벤트 ID")):
    """이벤트 통계 조회"""
    statistics = {
        "totalParticipants": 1234,
        "uniqueParticipants": 1000,
        "totalWinners": 10,
        "participationRate": 12.34,
        "winningRate": 0.81,
        "dailyStats": [
            {"date": "2024-01-01", "participants": 100},
            {"date": "2024-01-02", "participants": 150}
        ],
        "hourlyStats": [
            {"hour": 9, "participants": 50},
            {"hour": 10, "participants": 80}
        ]
    }
    
    return BaseResponse(isSuccess=True, data=statistics)