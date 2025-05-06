from fastapi import APIRouter

from app.api.v1.endpoints import router as endpoints_router

# API v1의 메인 라우터
api_router = APIRouter()

# 엔드포인트 라우터 포함
api_router.include_router(endpoints_router, tags=["general"])

# 추가 라우터는 필요에 따라 여기에 추가
