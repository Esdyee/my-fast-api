import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Settings:
    """애플리케이션 설정 클래스"""
    
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI App")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    API_VERSION: str = os.getenv("API_VERSION", "v1")
    
    # API 접두어
    API_V1_PREFIX: str = f"/api/{API_VERSION}"
    
    # 추가 설정은 필요에 따라 여기에 추가

# 전역 설정 객체 생성
settings = Settings()
