# API Endpoints Analysis from server-demo.json

## API Categories

### 1. 이벤트 (Events) - `/api/cos/adm/evnt*`
- **Event List**: `GET /api/cos/adm/evntPageList/get`
- **Event Detail**: `GET /api/cos/adm/evntDetl/:id/get`
- **Event Winner List**: `GET /api/cos/adm/selectAplnEvntWinrPageList/get`

### 2. 뉴스레터 (Newsletter) - `/api/cos/adm/nslt*`
- **Newsletter List**: `GET /api/cos/adm/nslt/list/get`
- **Newsletter Detail**: `GET /api/cos/adm/nslt/:id/get`

### 3. 통계 (Statistics) - `/api/cos/adm/stst*`

#### 접속통계 (Access Statistics)
- **Accumulated Users**: `GET /api/cos/adm/stst/cnnc/acml-cnus/get`
- **Total Accumulated Users**: `GET /api/cos/adm/stst/cnnc/tot-acml-cnus/get`
- **Connection Statistics**: `GET /api/cos/adm/stst/cnnc/get`

#### 이벤트 통계 (Event Statistics)
- **Event List Stats**: `GET /api/cos/adm/stst/evnt/list/get`
- **Event Application Stats**: `GET /api/cos/adm/stst/evnt/aplt/page/get`
- **Event Daily Stats**: `GET /api/cos/adm/stst/evnt/dily/page/get`
- **Event Prize Stats**: `GET /api/cos/adm/stst/evnt/gvaw-crst/page/get`
- **Event Share Stats**: `GET /api/cos/adm/stst/evnt/shre/page/get`

#### 뉴스레터 통계 (Newsletter Statistics)
- **Newsletter List Stats**: `GET /api/cos/adm/stst/nslt/list/get`
- **Newsletter Daily Stats**: `GET /api/cos/adm/stst/nslt/dily/page/get`
- **Newsletter Share Stats**: `GET /api/cos/adm/stst/nslt/shre/page/get`

#### FP 활동 통계 (FP Activity Statistics)
- **FP Newsletter Activity**: `GET /api/cos/adm/stst/fp/actt/nslt/get`
- **FP Touch Content Activity**: `GET /api/cos/adm/stst/fp/actt/tcct/get`

#### 미션 통계 (Mission Statistics)
- **Mission List**: `GET /api/cos/adm/stst/mssn/list/get`
- **Mission Detail**: `GET /api/cos/adm/stst/mssn/6/get`

#### 서비스 활용 통계 (Service Usage Statistics)
- **Service Usage Stats**: `GET /api/cos/adm/stst/srvc/utlz-crst/list/get`

### 4. 터치콘텐츠 (Touch Content) - `/api/cos/adm/tcct*`
- **Touch Content List**: `GET /api/cos/adm/tcctCntsPageList/get`
- **Touch Content Detail**: `GET /api/cos/adm/tcctCntsDetlInfo/:id/get`
- **Touch Content Recommendation**: `GET /api/cos/adm/tcct/rcmd/get`
- **Touch Content Daily Stats**: `GET /api/cos/adm/stst/tcct/daly/get`

### 5. 참여형 콘텐츠 (Interactive Content) - `/api/cos/adm/invl*`
- **Interactive Content List**: `GET /api/cos/adm/invlCntsPageList/get`
- **Interactive Content Detail**: `GET /api/cos/adm/invlCntsDetl/:id/get`
- **Interactive Customer List**: `GET /api/cos/adm/invlCustList/get`

### 6. 전파형 콘텐츠 (Viral Content) - `/api/cos/adm/pldp*`
- **Viral Content List**: `GET /api/cos/adm/pldpPageList/get`
- **Viral Content Detail**: `GET /api/cos/adm/pldpDetl/:id/get`

### 7. 발송 관리 (Sending Management) - `/api/cos/adm/hqdt*`
- **Send Group List**: `GET /api/cos/adm/hqdt/send-grop/list/get`
- **Send List**: `GET /api/cos/adm/hqdt/send-grop/send-list/get`
- **Send Status Count**: `GET /api/cos/adm/hqdt/send-grop/stts-cnt/get`
- **Customer Reception List**: `GET /api/cos/adm/hqdt/send-grop/cust-rctn-list/get`
- **Customer Reception Detail**: `GET /api/cos/adm/hqdt/send-grop/cust-rctn-detl/get`
- **Target Count**: `GET /api/cos/adm/hqdt/send-grop/tctg-cnt/get`
- **Target List**: `GET /api/cos/adm/hqdt/send-grop/tctg-list/get`

### 8. 엑셀 다운로드 (Excel Download) - `/api/cos/adm/excl*`
- Various statistics excel downloads for events, newsletters, connections, etc.

### 9. 기타 관리 (Other Management)
- **Banner Management**: `POST /api/cos/adm/banr/post`
- **Calendar Management**: `POST /api/cos/adm/cldr/post`
- **File Upload**: `POST /api/cos/adm/file/upload/pub/single/post`
- **Category List**: `GET /api/cos/adm/cntsCgryList/get`
- **Keyword Category List**: `GET /api/cos/adm/kwdCgryList/get`
- **Keyword List**: `GET /api/cos/adm/kwdList/get`
- **Customer Content List**: `GET /api/cos/adm/customerContentList/get`

## POST Endpoints

### File Management
- **Single File Upload**: `POST /api/cos/adm/file/upload/pub/single/post`
  - Returns file details including ID, path, size

### Content Management
- **Banner Registration**: `POST /api/cos/adm/banr/post`
- **Calendar Registration**: `POST /api/cos/adm/cldr/post`
- **Touch Target Event Registration**: `POST /api/cos/adm/hqdt/toch-trgt/evnt-rgst-altr/post`
- **Touch Content Registration**: `POST /api/cos/adm/hqdt/toch-trgt/toch-cnts-rgst-altr/post`

### Excel Export
- **FP Newsletter Activity Excel**: `POST /api/cos/adm/excl/stst/fp/actt/nslt/post`
- **FP Touch Content Activity Excel**: `POST /api/cos/adm/excl/stst/fp/actt/tcct/post`
- **Service Usage Statistics Excel**: `POST /api/cos/adm/excl/stst/srvc/utlz-crst/list/post`
- **Send Target Excel**: `POST /api/cos/adm/excl/hqdt/send-grop/send-trgt/post`

## Sample Response Structures

### 1. Event List Response
```json
{
  "isSuccess": true,
  "data": {
    "pagination": {
      "pageNum": 1,
      "pageSize": 10,
      "totalElements": 7,
      "totalPages": 1
    },
    "list": [
      {
        "sqnb": 20,
        "cuosCntsId": 349,
        "cuosPrizMthoDvsnCode": "APLN", // 응모형
        "cuosPrizMthoDvsnCodeNm": "응모형",
        "titlNm": "응모형 상세조회",
        "kwd": "운전자보험",
        "prgsStts": "진행중",
        "prmrEndYn": "N",
        "aplnStarDttm": "2024-09-28 00:00:00",
        "aplnEndDttm": "2024-09-30 00:00:00",
        "rgstDttm": "2024-09-28",
        "rgstTme": "11:19:03"
      }
    ]
  }
}
```

### 2. Event Detail Response
```json
{
  "isSuccess": true,
  "data": {
    "evntInfo": {
      "cuosCntsId": 339,
      "evntNm": "고객님께 당첨 소식을 전해보세요!",
      "cuosPrizMthoDvsnCode": "IMDT", // 즉시당첨형
      "oppbStarDttm": "2024-01-01 00:00:00",
      "oppbEndDttm": "2024-12-31 00:00:00"
    },
    "fpDetlInfo": {
      // FP specific details
    },
    "custDetlInfo": {
      // Customer specific details
    },
    "invlAltn": {
      // Interactive alternative details
    },
    "prizAltn": {
      // Prize alternative details
    },
    "gvam": {
      // Gift management details
    },
    "shre": {
      // Share details
    }
  }
}
```

### 3. Newsletter List Response
```json
{
  "isSuccess": true,
  "data": {
    "pagination": {
      "pageNum": 1,
      "pageSize": 10,
      "totalElements": 1
    },
    "list": [
      {
        "cuosCntsId": 99,
        "oppbStarDttm": "2024-09-24 00:00:00",
        "titlNm": "life&9월호",
        "cuosRprsImgeFileId": 337,
        "cuosRprsImgeFilePath": "public/20240923/b8e872bb0a424957ab2e9042842cd4c0.png"
      }
    ]
  }
}
```

### 4. Statistics Response
```json
{
  "isSuccess": true,
  "data": {
    "acmlCnusCnt": 23
  }
}
```

### 5. Touch Content List Response
```json
{
  "isSuccess": true,
  "data": {
    "pagination": {
      "pageNum": 1,
      "pageSize": 10,
      "totalElements": 145,
      "totalPages": 15
    },
    "list": [
      {
        "sqnb": "145",
        "cuosCntsId": 1162,
        "cntsCgryNm": "상품 안내 콘텐츠",
        "cntsCgryCntn": "암보험",
        "titlNm": "[삭제예정] gif 테스트",
        "kwdList": [
          {
            "cuosKwdId": 10,
            "cuosKwdNm": "암보험",
            "hgrnCuosKwdId": 1,
            "hgrnCuosKwdNm": "보험",
            "sortOrdr": 1
          }
        ],
        "kwd": "암보험",
        "clckCnt": 8,
        "shreCnt": 4,
        "bltnYn": "Y",
        "oppbStarDttm": "2024-11-01 00:00:00"
      }
    ]
  }
}
```

### 6. File Upload Response
```json
{
  "isSuccess": true,
  "data": {
    "cuosFileId": 2660,
    "ogtxFileNm": "640_640_T.png",
    "filePathNm": "public/20241003/af12fccb745d4534a859fe8c15b5acdd.png",
    "fileSaveNm": "af12fccb745d4534a859fe8c15b5acdd.png",
    "fileSize": 212585,
    "cuosFileGropId": 275,
    "sortOrdr": 1
  }
}
```

### 7. Interactive Content List Response
```json
{
  "isSuccess": true,
  "data": [
    {
      "id": 10,
      "titlNm": "[서술형_테스트] 오점뭐",
      "rgstDttm": "2024-09-25 09:10:03",
      "cntsType": "INVL",
      "cntsCgryNm": "터치콘텐츠+뉴스레터형",
      "invl": {
        "ptnlCustEvntId": "ID008"
      }
    }
  ]
}
```

## Key Data Models

### Event Types
- **APLN**: 응모형 (Application type)
- **IMDT**: 즉시당첨형 (Instant win type)

### Content Types
- **EVNT**: 이벤트 (Event)
- **TCCT**: 터치콘텐츠 (Touch Content)
- **INVL**: 참여형 (Interactive)
- **NSLT**: 뉴스레터 (Newsletter)

### Status Types
- **진행중**: In Progress
- **종료**: Ended
- **예정**: Scheduled

## Touch Content Categories (터치콘텐츠 카테고리)
1. **상품 안내 콘텐츠** - Product information content
2. **FP님 전용 교육자료** - FP exclusive educational materials
3. **영업이 쉬워지는 콘텐츠** - Content that makes sales easier
4. **보험니즈** - Insurance needs

## Keyword Categories (키워드 카테고리)
1. **보험** - Insurance (암보험, 운전자보험, etc.)
2. **보험니즈 터치하기** - Touch insurance needs
3. **재테크/자기개발** - Financial tech/Self-development
4. **취미/레져** - Hobby/Leisure
5. **헬스/뷰티** - Health/Beauty

## API Patterns
1. Most GET endpoints end with `/get`
2. POST endpoints end with `/post`
3. PUT endpoints end with `/put`
4. DELETE endpoints end with `/delete`
5. Excel download endpoints contain `/excl/` in the path
6. Detail endpoints use `/:id/get` pattern
7. List endpoints typically have pagination support
8. All responses follow a standard format with `isSuccess` field
9. List responses include pagination object
10. Korean terms are used in field names (e.g., 통계, 이벤트, 뉴스레터)

## Summary
This API system appears to be a comprehensive content management system for:
- Managing marketing events and campaigns
- Distributing newsletters
- Tracking user engagement and statistics
- Managing touch content for FP (Financial Planners)
- Handling file uploads and content distribution
- Providing detailed analytics and reporting capabilities

The system supports both admin operations and content delivery with robust tracking and analytics features.