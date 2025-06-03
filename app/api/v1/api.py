from fastapi import APIRouter

from app.api.v1.endpoints import router as endpoints_router
from app.api.v1.routers.event import router as event_router
from app.api.v1.routers.newsletter import router as newsletter_router
from app.api.v1.routers.statistics import router as statistics_router
from app.api.v1.routers.content import router as content_router
from app.api.v1.routers.sending import router as sending_router
from app.api.v1.routers.hq_direct_touch import router as hq_direct_touch_router

# API v1의 메인 라우터
api_router = APIRouter()

# 엔드포인트 라우터 포함
api_router.include_router(endpoints_router, tags=["general"])

# COS Admin API 라우터들
api_router.include_router(event_router, prefix="/cos/adm")
api_router.include_router(newsletter_router, prefix="/cos/adm")
api_router.include_router(statistics_router, prefix="/cos/adm")
api_router.include_router(content_router, prefix="/cos/adm")
api_router.include_router(sending_router, prefix="/cos/adm")
api_router.include_router(hq_direct_touch_router, prefix="/cos/adm")

# 추가 라우터는 필요에 따라 여기에 추가
