from typing import List
from datetime import datetime
from fastapi import APIRouter, Path, Query
from app.models.common import BaseResponse, PaginatedResponse
from app.schemas.sending import (
    SendingTaskListRequest,
    SendingTaskResponse,
    SendingTaskDetailResponse,
    SendingTargetListRequest,
    SendingCreateRequest,
    SendingRetryRequest
)

router = APIRouter(prefix="/sending", tags=["발송 관리"])


@router.post("/task/list/get", response_model=PaginatedResponse)
async def get_sending_task_list(request: SendingTaskListRequest):
    """발송 작업 목록 조회"""
    tasks = [
        {
            "id": 1,
            "type": "이벤트",
            "title": "신년 이벤트 당첨자 발표",
            "channel": "이메일",
            "status": "완료",
            "targetCount": 100,
            "sentCount": 98,
            "failedCount": 2,
            "successRate": 98.0,
            "scheduledAt": "2024-01-31T10:00:00",
            "completedAt": "2024-01-31T10:15:00"
        },
        {
            "id": 2,
            "type": "뉴스레터",
            "title": "1월 금융 뉴스레터",
            "channel": "이메일",
            "status": "발송중",
            "targetCount": 5000,
            "sentCount": 3421,
            "failedCount": 12,
            "successRate": 99.6,
            "scheduledAt": "2024-01-01T09:00:00"
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": tasks},
        pagination={
            "totalCount": 2,
            "totalPages": 1,
            "currentPage": request.page,
            "pageSize": request.size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.get("/task/{task_id}/get", response_model=BaseResponse)
async def get_sending_task_detail(task_id: int = Path(..., description="발송 작업 ID")):
    """발송 작업 상세 조회"""
    task = {
        "id": task_id,
        "type": "이벤트",
        "title": "신년 이벤트 당첨자 발표",
        "channel": "이메일",
        "status": "완료",
        "targetCount": 100,
        "sentCount": 98,
        "failedCount": 2,
        "successRate": 98.0,
        "scheduledAt": "2024-01-31T10:00:00",
        "startedAt": "2024-01-31T10:00:05",
        "completedAt": "2024-01-31T10:15:00",
        "createdAt": "2024-01-30T15:00:00",
        "createdBy": "admin001",
        "settings": {
            "retryCount": 3,
            "retryInterval": 300,
            "priority": "high"
        }
    }
    
    return BaseResponse(isSuccess=True, data=task)


@router.post("/task/{task_id}/target/list/get", response_model=PaginatedResponse)
async def get_sending_target_list(
    task_id: int = Path(..., description="발송 작업 ID"),
    request: SendingTargetListRequest = ...
):
    """발송 대상 목록 조회"""
    targets = [
        {
            "id": 1,
            "userId": "user001",
            "contactInfo": "user001@example.com",
            "status": "완료",
            "sentAt": "2024-01-31T10:01:00"
        },
        {
            "id": 2,
            "userId": "user002",
            "contactInfo": "user002@example.com",
            "status": "실패",
            "failedAt": "2024-01-31T10:02:00",
            "failureReason": "Invalid email address"
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": targets},
        pagination={
            "totalCount": 2,
            "totalPages": 1,
            "currentPage": request.page,
            "pageSize": request.size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.post("/task/create/post")
async def create_sending_task(request: SendingCreateRequest):
    """발송 작업 생성"""
    return BaseResponse(
        isSuccess=True,
        data={
            "taskId": 123,
            "message": "발송 작업이 생성되었습니다",
            "scheduledAt": request.scheduledAt,
            "targetCount": len(request.targetIds)
        }
    )


@router.post("/task/{task_id}/cancel/post")
async def cancel_sending_task(task_id: int = Path(..., description="발송 작업 ID")):
    """발송 작업 취소"""
    return BaseResponse(
        isSuccess=True,
        data={
            "taskId": task_id,
            "message": "발송 작업이 취소되었습니다",
            "cancelledCount": 1579  # 취소된 미발송 건수
        }
    )


@router.post("/task/{task_id}/retry/post")
async def retry_sending_task(
    task_id: int = Path(..., description="발송 작업 ID"),
    request: SendingRetryRequest = ...
):
    """발송 실패 건 재시도"""
    return BaseResponse(
        isSuccess=True,
        data={
            "taskId": task_id,
            "message": "재발송이 시작되었습니다",
            "retryCount": 2 if request.targetIds else 12  # 재시도 대상 건수
        }
    )


@router.get("/channel/status/get", response_model=BaseResponse)
async def get_channel_status():
    """발송 채널별 상태 조회"""
    status = {
        "email": {
            "status": "정상",
            "dailyLimit": 100000,
            "dailySent": 45678,
            "remainingQuota": 54322,
            "successRate": 98.5
        },
        "sms": {
            "status": "정상",
            "dailyLimit": 50000,
            "dailySent": 12345,
            "remainingQuota": 37655,
            "successRate": 99.2
        },
        "push": {
            "status": "정상",
            "dailyLimit": 200000,
            "dailySent": 89012,
            "remainingQuota": 110988,
            "successRate": 95.8
        },
        "kakao": {
            "status": "점검중",
            "dailyLimit": 80000,
            "dailySent": 0,
            "remainingQuota": 80000,
            "successRate": 0.0,
            "message": "카카오 알림톡 서비스 점검 중 (14:00 ~ 15:00)"
        }
    }
    
    return BaseResponse(isSuccess=True, data=status)


@router.post("/history/excel/get")
async def download_sending_history_excel(
    startDate: datetime = Query(...),
    endDate: datetime = Query(...)
):
    """발송 이력 엑셀 다운로드"""
    return BaseResponse(
        isSuccess=True,
        data={
            "downloadUrl": f"/downloads/sending_history_{startDate.strftime('%Y%m%d')}_{endDate.strftime('%Y%m%d')}.xlsx",
            "message": "엑셀 파일 생성이 완료되었습니다"
        }
    )