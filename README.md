# My FastAPI Application

FastAPI를 이용한 간단한 API 프로젝트입니다.

## 설치 방법

```bash
# 필요한 패키지 설치
pip install -r requirements.txt
```

## 실행 방법

```bash
# 개발 서버 실행
python main.py
```

또는 uvicorn을 직접 사용:

```bash
uvicorn main:app --reload
```

## API 문서

서버 실행 후 다음 URL에서 자동 생성된 API 문서를 확인할 수 있습니다:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 프로젝트 구조

```
my-fast-api/
├── app/                    # 애플리케이션 코드
│   ├── api/                # API 엔드포인트
│   │   └── v1/            # API 버전 1
│   ├── core/              # 핵심 기능 (설정 등)
│   ├── models/            # 데이터베이스 모델
│   └── schemas/           # Pydantic 모델 (데이터 검증)
├── .env                    # 환경 변수
├── main.py                 # 애플리케이션 진입점
└── requirements.txt        # 의존성 패키지
```
