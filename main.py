from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.api import api_router

def create_app() -> FastAPI:
    """
    FastAPI 애플리케이션 인스턴스를 생성합니다.
    """
    # FastAPI 인스턴스 생성
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG
    )

    # CORS 미들웨어 설정
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 실제 환경에서는 구체적인 도메인 지정 권장
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # API 라우터 포함
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)

    return app

app = create_app()

@app.get("/")
async def root():
    """
    루트 엔드포인트 - API 문서로 리디렉션합니다.
    """
    return {"message": "Welcome to FastAPI application", "docs": "/docs"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
