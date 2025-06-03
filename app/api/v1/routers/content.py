from typing import List, Optional
from fastapi import APIRouter, Path, Query, HTTPException, UploadFile, File
from app.models.common import BaseResponse, PaginatedResponse
from app.models.content import ContentType
from app.schemas.content import (
    ContentListRequest,
    ContentResponse,
    TouchContentResponse,
    InteractiveContentResponse,
    ViralContentResponse,
    ContentCreateRequest,
    ContentUpdateRequest
)

router = APIRouter(prefix="/content", tags=["콘텐츠"])


@router.post("/touch/list/get", response_model=PaginatedResponse)
async def get_touch_content_list(request: ContentListRequest):
    """터치콘텐츠 목록 조회"""
    contents = [
        {
            "id": 1,
            "code": "TCCT20240001",
            "type": "TCCT",
            "title": "2024년 세제개편안 가이드",
            "description": "2024년 달라지는 세제 정책을 쉽게 설명합니다",
            "category": "세무",
            "status": "발행",
            "keywords": ["세금", "세제개편", "2024"],
            "viewCount": 1234,
            "shareCount": 89,
            "downloadCount": 456,
            "fileUrl": "/files/tax_guide_2024.pdf",
            "fileSize": 2048576,
            "fileType": "application/pdf"
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": contents},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": request.page,
            "pageSize": request.size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.get("/touch/{content_id}/get", response_model=BaseResponse)
async def get_touch_content_detail(content_id: int = Path(..., description="콘텐츠 ID")):
    """터치콘텐츠 상세 조회"""
    content = {
        "id": content_id,
        "code": "TCCT20240001",
        "type": "TCCT",
        "title": "2024년 세제개편안 가이드",
        "description": "2024년 달라지는 세제 정책을 쉽게 설명합니다",
        "category": "세무",
        "status": "발행",
        "keywords": ["세금", "세제개편", "2024"],
        "thumbnailUrl": "/images/content/tax_guide_thumb.jpg",
        "viewCount": 1234,
        "shareCount": 89,
        "downloadCount": 456,
        "fileUrl": "/files/tax_guide_2024.pdf",
        "fileSize": 2048576,
        "fileType": "application/pdf",
        "createdAt": "2023-12-20T10:00:00",
        "publishedAt": "2023-12-21T09:00:00"
    }
    
    return BaseResponse(isSuccess=True, data=content)


@router.post("/touch/upload/post")
async def upload_touch_content_file(
    file: UploadFile = File(...),
    contentId: Optional[int] = Query(None)
):
    """터치콘텐츠 파일 업로드"""
    return BaseResponse(
        isSuccess=True,
        data={
            "fileUrl": f"/files/{file.filename}",
            "fileSize": 1024000,
            "fileType": file.content_type,
            "message": "파일이 성공적으로 업로드되었습니다"
        }
    )


@router.post("/interactive/list/get", response_model=PaginatedResponse)
async def get_interactive_content_list(request: ContentListRequest):
    """참여형 콘텐츠 목록 조회"""
    contents = [
        {
            "id": 1,
            "code": "INVL20240001",
            "type": "INVL",
            "title": "은퇴자금 계산 퀴즈",
            "description": "나의 은퇴 준비 상태를 점검해보세요",
            "category": "은퇴",
            "status": "발행",
            "keywords": ["은퇴", "퀴즈", "자금계산"],
            "viewCount": 2345,
            "shareCount": 123,
            "contentUrl": "/interactive/retirement_quiz",
            "questionCount": 10,
            "completionRate": 67.5,
            "avgScore": 75.3
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": contents},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": request.page,
            "pageSize": request.size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.get("/interactive/{content_id}/get", response_model=BaseResponse)
async def get_interactive_content_detail(content_id: int = Path(..., description="콘텐츠 ID")):
    """참여형 콘텐츠 상세 조회"""
    content = {
        "id": content_id,
        "code": "INVL20240001",
        "type": "INVL",
        "title": "은퇴자금 계산 퀴즈",
        "description": "나의 은퇴 준비 상태를 점검해보세요",
        "category": "은퇴",
        "status": "발행",
        "keywords": ["은퇴", "퀴즈", "자금계산"],
        "thumbnailUrl": "/images/content/retirement_quiz_thumb.jpg",
        "viewCount": 2345,
        "shareCount": 123,
        "contentUrl": "/interactive/retirement_quiz",
        "duration": 300,
        "questionCount": 10,
        "completionRate": 67.5,
        "avgScore": 75.3,
        "createdAt": "2023-12-15T10:00:00",
        "publishedAt": "2023-12-16T09:00:00"
    }
    
    return BaseResponse(isSuccess=True, data=content)


@router.post("/viral/list/get", response_model=PaginatedResponse)
async def get_viral_content_list(request: ContentListRequest):
    """전파형 콘텐츠 목록 조회"""
    contents = [
        {
            "id": 1,
            "code": "VIRL20240001",
            "type": "VIRL",
            "title": "30초로 알아보는 보험 상식",
            "description": "짧고 재미있게 보험 상식을 전달합니다",
            "category": "보험",
            "status": "발행",
            "keywords": ["보험", "상식", "카드뉴스"],
            "viewCount": 5432,
            "shareCount": 789,
            "contentUrl": "/viral/insurance_tips",
            "viralReach": 12345,
            "secondaryShares": 234,
            "engagementRate": 23.5
        }
    ]
    
    return PaginatedResponse(
        isSuccess=True,
        data={"list": contents},
        pagination={
            "totalCount": 1,
            "totalPages": 1,
            "currentPage": request.page,
            "pageSize": request.size,
            "hasNext": False,
            "hasPrevious": False
        }
    )


@router.get("/viral/{content_id}/get", response_model=BaseResponse)
async def get_viral_content_detail(content_id: int = Path(..., description="콘텐츠 ID")):
    """전파형 콘텐츠 상세 조회"""
    content = {
        "id": content_id,
        "code": "VIRL20240001",
        "type": "VIRL",
        "title": "30초로 알아보는 보험 상식",
        "description": "짧고 재미있게 보험 상식을 전달합니다",
        "category": "보험",
        "status": "발행",
        "keywords": ["보험", "상식", "카드뉴스"],
        "thumbnailUrl": "/images/content/insurance_tips_thumb.jpg",
        "viewCount": 5432,
        "shareCount": 789,
        "contentUrl": "/viral/insurance_tips",
        "viralReach": 12345,
        "secondaryShares": 234,
        "engagementRate": 23.5,
        "createdAt": "2023-12-10T10:00:00",
        "publishedAt": "2023-12-11T09:00:00"
    }
    
    return BaseResponse(isSuccess=True, data=content)


@router.post("/create/post")
async def create_content(request: ContentCreateRequest):
    """콘텐츠 생성"""
    return BaseResponse(
        isSuccess=True,
        data={
            "contentId": 123,
            "message": f"{request.type} 콘텐츠가 성공적으로 생성되었습니다"
        }
    )


@router.put("/{content_id}/update/post")
async def update_content(
    content_id: int = Path(..., description="콘텐츠 ID"),
    request: ContentUpdateRequest = ...
):
    """콘텐츠 수정"""
    return BaseResponse(
        isSuccess=True,
        data={
            "contentId": content_id,
            "message": "콘텐츠가 성공적으로 수정되었습니다"
        }
    )


@router.delete("/{content_id}/delete/post")
async def delete_content(content_id: int = Path(..., description="콘텐츠 ID")):
    """콘텐츠 삭제"""
    return BaseResponse(
        isSuccess=True,
        data={"message": "콘텐츠가 성공적으로 삭제되었습니다"}
    )


@router.get("/categories/get", response_model=BaseResponse)
async def get_content_categories():
    """콘텐츠 카테고리 목록 조회"""
    categories = [
        {"code": "INSURANCE", "name": "보험", "count": 45},
        {"code": "RETIREMENT", "name": "은퇴", "count": 32},
        {"code": "TAX", "name": "세무", "count": 28},
        {"code": "INVESTMENT", "name": "투자", "count": 51},
        {"code": "ESTATE", "name": "부동산", "count": 23},
        {"code": "EDUCATION", "name": "교육", "count": 67}
    ]
    
    return BaseResponse(isSuccess=True, data=categories)


@router.get("/keywords/get", response_model=BaseResponse)
async def get_popular_keywords():
    """인기 키워드 조회"""
    keywords = [
        {"keyword": "세금", "count": 234},
        {"keyword": "은퇴준비", "count": 189},
        {"keyword": "보험료", "count": 156},
        {"keyword": "투자전략", "count": 145},
        {"keyword": "연말정산", "count": 132}
    ]
    
    return BaseResponse(isSuccess=True, data=keywords)