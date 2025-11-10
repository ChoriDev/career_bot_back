# Career Bot

## 프로젝트 소개

Career Bot은 진로문장완성검사 진단 웹 서비스입니다. 사용자가 제공된 검사 문항에 대해 답변을 제시했을 때 전문가의 해석이 생성되고 수검자의 진로 성숙도를 판별합니다. 이 레포지토리는 Career Bot 서비스의 Django 기반 백엔드 서버입니다.

## 기능

- **답변 제출:** 학생들이 질문에 대한 답변을 제출할 수 있습니다.
- **AI 기반 채점 및 코멘트:** 외부 AI 서비스(BERT 및 Polyglot)와 통합하여 답변에 점수를 매기고 코멘트를 제공합니다.
- **결과 생성:** 각 학생에 대한 결과 페이지를 생성하여 답변, AI 생성 코멘트 및 다양한 카테고리별 평균 점수를 표시합니다.

## 기술 스택

- **백엔드:** Python, Django, Django REST Framework
- **데이터베이스:** SQLite
- **AI 통합:** 채점 및 코멘트를 위해 외부 AI 서비스와 통신합니다.

## 시작하기

### 요구 사항

- Python 3.x
- Django
- Django REST Framework

### 설치

1.  **저장소 복제:**
    ```bash
    git clone https://github.com/your-username/career-bot-back.git
    cd career-bot-back
    ```

2.  **의존성 설치:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **데이터베이스 마이그레이션 실행:**
    ```bash
    python manage.py migrate
    ```

4.  **개발 서버 시작:**
    ```bash
    python manage.py runserver
    ```

서버는 `http://127.0.0.1:8000/` 에서 실행됩니다.

## API 엔드포인트

- `GET /questions/`: 모든 질문 목록을 가져옵니다.
- `POST /students/<str:student_id>/questions/<int:question_id>/answers/`: 특정 질문에 대한 답변을 제출합니다.
  - **요청 본문:**
    ```json
    {
      "answer1": "첫 번째 답변",
      "answer2": "두 번째 답변"
    }
    ```
- `GET /students/<str:student_id>/result/`: 특정 학생의 결과를 가져옵니다.

## 프로젝트 구조

```
career-bot-back/
├── career_bot/         # Django 프로젝트 설정
├── server/             # 메인 로직을 위한 Django 앱
│   ├── migrations/
│   ├── models.py       # 데이터베이스 모델 (Question, Answer)
│   ├── views.py        # API 뷰
│   ├── urls.py         # 앱별 URL 라우팅
│   ├── serializers.py  # 데이터 시리얼라이저
│   └── request_func.py # 외부 AI 서비스와 통신하는 기능
├── db.sqlite3          # SQLite 데이터베이스
└── manage.py           # Django의 명령줄 유틸리티
```
