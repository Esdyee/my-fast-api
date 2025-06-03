from typing import List, Optional
from fastapi import APIRouter, Path, Query, HTTPException
from app.models.common import BaseResponse, PaginatedResponse
from app.schemas.hq_direct_touch import (
    SendGroupListRequest,
    SendGroupResponse,
    SendGroupEndRequest,
    TouchTargetListRequest,
    TouchTargetResponse,
    SendTargetListRequest,
    SendTargetResponse,
    CustomerReactionListRequest,
    CustomerReactionResponse,
    CustomerDetailRequest,
    CustomerDetailResponse,
    TouchPointEventListRequest,
    TouchPointEventResponse,
    TouchPointEventCreateRequest,
    TouchPointContentListRequest,
    TouchPointContentResponse,
    TouchPointContentCreateRequest
)

router = APIRouter(prefix="/hqdt", tags=["본사직접터치"])


# 본사직접터치 - 발송그룹 관리
@router.get("/send-grop/list/get", response_model=PaginatedResponse)
async def get_send_group_list(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    searchKeyword: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    startDate: Optional[str] = Query(None),
    endDate: Optional[str] = Query(None)
):
    """발송그룹 관리 목록 조회"""
    send_groups = [
        {
            "id": 1,
            "groupCode": "SG20240101",
            "groupName": "2024년 신년 이벤트 발송",
            "status": "진행중",
            "touchType": "이벤트",
            "totalCount": 1000,
            "sentCount": 850,
            "viewCount": 650,
            "reactionCount": 234,
            "viewRate": 76.5,
            "reactionRate": 27.5,
            "startDate": "2024-01-01T09:00:00",
            "endDate": None
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": send_groups},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": page,
            "pageSize": size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.post("/send-grop/end/put")
async def end_send_group(request: SendGroupEndRequest):
    """발송그룹 종료"""
    return BaseResponse(
        isSuccess=True,
        data={
            "endedCount": len(request.groupIds),
            "message": "발송그룹이 종료되었습니다"
        }
    )


@router.get("/send-grop/tctg-list/get", response_model=PaginatedResponse)
async def get_touch_target_list(
    groupId: int = Query(...),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)
):
    """그룹 상세 - 좌측 Topic (터치거리 목록)"""
    touch_targets = [
        {
            "id": 1,
            "targetType": "이벤트",
            "targetId": 101,
            "targetName": "신년 맞이 특별 이벤트",
            "targetCode": "EVT20240101",
            "description": "2024년 새해를 맞아 진행하는 특별 이벤트",
            "thumbnailUrl": "/images/event/newyear2024.jpg",
            "sentCount": 850,
            "viewCount": 650
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": touch_targets},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": page,
            "pageSize": size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.get("/send-grop/send-list/get", response_model=PaginatedResponse)
async def get_send_target_list(
    groupId: int = Query(...),
    touchTargetId: Optional[int] = Query(None),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)
):
    """그룹 상세 - 우측 Topic (발송 대상 목록)"""
    send_targets = [
        {
            "id": 1,
            "fpId": "FP001",
            "fpName": "김철수",
            "customerCount": 45,
            "sentAt": "2024-01-01T09:30:00",
            "status": "완료",
            "viewCount": 32,
            "reactionCount": 12
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": send_targets},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": page,
            "pageSize": size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.get("/send-grop/cust-rctn-list/get", response_model=PaginatedResponse)
async def get_customer_reaction_list(
    groupId: int = Query(...),
    reactionType: Optional[str] = Query(None),
    fpId: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)
):
    """고객 반응 목록 조회"""
    reactions = [
        {
            "customerId": "CUST001",
            "customerName": "홍길동",
            "fpId": "FP001",
            "fpName": "김철수",
            "reactionType": "참여",
            "reactionAt": "2024-01-02T14:30:00",
            "contentId": 101,
            "contentName": "신년 이벤트"
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": reactions},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": page,
            "pageSize": size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.get("/send-grop/cust-rctn-detl/get", response_model=BaseResponse)
async def get_customer_detail(
    groupId: int = Query(...),
    customerId: str = Query(...)
):
    """발송그룹 고객정보 팝업"""
    customer_detail = {
        "customerId": "CUST001",
        "customerName": "홍길동",
        "email": "hong@example.com",
        "phone": "010-1234-5678",
        "fpId": "FP001",
        "fpName": "김철수",
        "reactions": [
            {
                "type": "조회",
                "contentName": "신년 이벤트 안내",
                "reactionAt": "2024-01-01T10:15:00"
            },
            {
                "type": "참여",
                "contentName": "신년 이벤트",
                "reactionAt": "2024-01-02T14:30:00"
            }
        ],
        "contents": [
            {
                "id": 1,
                "name": "신년 이벤트 안내",
                "type": "이벤트",
                "viewedAt": "2024-01-01T10:15:00"
            }
        ]
    }
    
    return BaseResponse(isSuccess=True, data=customer_detail)


@router.get("/send-grop/tctg-cnt/get", response_model=BaseResponse)
async def get_touch_target_count(groupId: int = Query(...)):
    """터치거리 총 건수 조회"""
    return BaseResponse(
        isSuccess=True,
        data={
            "totalCount": 15,
            "eventCount": 8,
            "contentCount": 7
        }
    )


@router.get("/send-grop/stts-cnt/get", response_model=BaseResponse)
async def get_send_group_status_count():
    """발송그룹상태별 건수 조회"""
    return BaseResponse(
        isSuccess=True,
        data={
            "대기": 5,
            "진행중": 12,
            "완료": 45,
            "종료": 8,
            "total": 70
        }
    )


@router.post("/send-grop/send-trgt/post")
async def export_send_target_excel(groupId: int = Query(...)):
    """발송 대상 엑셀 다운로드"""
    return BaseResponse(
        isSuccess=True,
        data={
            "downloadUrl": f"/downloads/send_target_group_{groupId}.xlsx",
            "message": "엑셀 파일 생성이 완료되었습니다"
        }
    )


# 터치거리 관리 - 이벤트
@router.get("/toch-trgt/evnt-list/get", response_model=PaginatedResponse)
async def get_touch_point_event_list(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    searchKeyword: Optional[str] = Query(None),
    isActive: Optional[bool] = Query(None)
):
    """터치거리 이벤트 목록 조회"""
    events = [
        {
            "id": 1,
            "code": "EVT20240101",
            "name": "신년 맞이 특별 이벤트",
            "description": "2024년 새해를 맞아 진행하는 특별 이벤트",
            "category": "프로모션",
            "keywords": ["신년", "이벤트", "2024"],
            "thumbnailUrl": "/images/event/newyear2024.jpg",
            "startDate": "2024-01-01T00:00:00",
            "endDate": "2024-01-31T23:59:59",
            "isActive": True,
            "participantCount": 1234
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": events},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": page,
            "pageSize": size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.get("/toch-trgt/evnt-detl/get", response_model=BaseResponse)
async def get_touch_point_event_detail(eventId: int = Query(...)):
    """터치거리 이벤트 상세 조회"""
    event = {
        "id": eventId,
        "code": "EVT20240101",
        "name": "신년 맞이 특별 이벤트",
        "description": "2024년 새해를 맞아 진행하는 특별 이벤트입니다. 많은 참여 부탁드립니다.",
        "category": "프로모션",
        "keywords": ["신년", "이벤트", "2024"],
        "thumbnailUrl": "/images/event/newyear2024.jpg",
        "startDate": "2024-01-01T00:00:00",
        "endDate": "2024-01-31T23:59:59",
        "isActive": True,
        "participantCount": 1234,
        "eventSettings": {
            "maxParticipants": 10000,
            "participationType": "응모형",
            "winnerCount": 100
        }
    }
    
    return BaseResponse(isSuccess=True, data=event)


@router.post("/toch-trgt/evnt-rgst-altr/post")
async def create_touch_point_event(request: TouchPointEventCreateRequest):
    """터치거리 이벤트 등록"""
    return BaseResponse(
        isSuccess=True,
        data={
            "eventId": 123,
            "message": "터치거리 이벤트가 성공적으로 등록되었습니다"
        }
    )


# 터치거리 관리 - 터치콘텐츠
@router.get("/toch-trgt/toch-cnts-list/get", response_model=PaginatedResponse)
async def get_touch_point_content_list(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    searchKeyword: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    isActive: Optional[bool] = Query(None)
):
    """터치거리 터치콘텐츠 목록 조회"""
    contents = [
        {
            "id": 1,
            "code": "TCCT20240001",
            "name": "2024년 세제개편안 가이드",
            "description": "2024년 달라지는 세제 정책을 쉽게 설명합니다",
            "category": "세무",
            "keywords": ["세금", "세제개편", "2024"],
            "thumbnailUrl": "/images/content/tax_guide_thumb.jpg",
            "isActive": True,
            "viewCount": 2345,
            "shareCount": 123
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": contents},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": page,
            "pageSize": size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.get("/toch-trgt/fetch-list/get", response_model=PaginatedResponse)
async def get_fetch_content_list(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    searchKeyword: Optional[str] = Query(None)
):
    """불러오기 팝업 목록 조회"""
    contents = [
        {
            "id": 1,
            "code": "TCCT20240001",
            "name": "2024년 세제개편안 가이드",
            "type": "터치콘텐츠",
            "category": "세무",
            "createdAt": "2023-12-20T10:00:00"
        },
        {
            "id": 2,
            "code": "EVT20240101",
            "name": "신년 이벤트",
            "type": "이벤트",
            "category": "프로모션",
            "createdAt": "2023-12-15T14:00:00"
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": contents},
        pagination={
            "totalCount": 2,
            "totalPages": 1,
            "currentPage": page,
            "pageSize": size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.get("/toch-trgt/toch-cnts-detl/get", response_model=BaseResponse)
async def get_touch_point_content_detail(contentId: int = Query(...)):
    """터치거리 터치콘텐츠 상세 조회"""
    content = {
        "id": contentId,
        "code": "TCCT20240001",
        "name": "2024년 세제개편안 가이드",
        "description": "2024년 달라지는 세제 정책을 쉽게 설명합니다",
        "category": "세무",
        "keywords": ["세금", "세제개편", "2024"],
        "thumbnailUrl": "/images/content/tax_guide_thumb.jpg",
        "contentUrl": "/files/tax_guide_2024.pdf",
        "fileType": "application/pdf",
        "fileSize": 2048576,
        "isActive": True,
        "viewCount": 2345,
        "shareCount": 123,
        "createdAt": "2023-12-20T10:00:00",
        "updatedAt": "2023-12-22T14:00:00"
    }
    
    return BaseResponse(isSuccess=True, data=content)


@router.post("/toch-trgt/toch-cnts-rgst-altr/post")
async def create_touch_point_content(request: TouchPointContentCreateRequest):
    """터치거리 터치콘텐츠 등록"""
    return BaseResponse(
        isSuccess=True,
        data={
            "contentId": 456,
            "message": "터치거리 터치콘텐츠가 성공적으로 등록되었습니다"
        }
    )