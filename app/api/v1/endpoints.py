from fastapi import APIRouter, HTTPException

# API 라우터 생성
router = APIRouter()

# 샘플 엔드포인트
@router.get("/")
async def root():
    """
    루트 엔드포인트는 API가 작동 중임을 확인합니다.
    """
    return {"message": "Welcome to My FastAPI Application"}

@router.get("/health")
async def health_check():
    """
    서버 상태 체크 엔드포인트
    """
    return {"status": "healthy"}

# 추가 엔드포인트는 필요에 따라 여기에 추가
