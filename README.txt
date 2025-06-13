# 🌟 오늘의 운세 프로젝트 (웹 + 콘솔)

**사용자의 정보 입력에 따라 오늘의 운세를 제공하는 감성 운세 프로그램입니다.**

* 웹 기반 인터랙션 버전
* 콘솔 기반 Rich 스타일 프로그램 두 가지 버전 통합

---

## 🔮 웹 버전: 오늘의 운세 뽑기

[👉 웹페이지 바로가기](https://joeunseonn.github.io/image_project/)
사용자가 성별, 생년월일, 양력/음력을 선택하면 오늘의 운세 메시지가 출력됩니다.

### 🧙 주요 기능

* 성별/생일/양력 입력 기반 운세 제공
* 버튼 클릭 시 맞춤형 운세 출력
* 감성 카드 스타일 디자인
* 이모지와 색상 강조로 가독성 향상

### 📸 실행 예시

```
✅ 입력 정보
👤 성별: 여성
📅 양력/음력: 양력
🎂 생일: 2002-06-29

🔮 오늘의 운세
🎁 깜짝 선물 같은 일이 생길 수 있어요!
```

---

## 🖥 콘솔 기반 프로그램 (Rich 활용)

Python 콘솔에서 Rich 라이브러리를 활용한 감성 카드 스타일의 운세 뽑기!

### 🧾 제공 파일

* `fortune_console.py` – 생년월일 입력 기반 운세 출력
* `tarot_fortune_v3.py` – 타로카드 번호 선택 기반 운세 출력

### 📦 Rich 라이브러리 특징

* 컬러풀한 패널 UI 출력
* 이모지 활용으로 사용자 친화적
* 텍스트 정렬, 박스 스타일 등 시각적 연출 탁월

### 💻 실행 예시

```bash
$ python fortune_console.py
성별을 입력하세요 (m/f): f
양력 또는 음력을 입력하세요 (solar/lunar): solar
생일을 입력하세요 (예: 2002-06-29)

🔮 오늘의 운세
🎁 깜짝 선물 같은 일이 생길 수 있어요!
```

---

## 📁 프로젝트 폴더 구조

```
📂 today-fortune-project
├── index.html               # 웹 소개 페이지
├── style.css                # 웹 스타일 파일
├── script.js                # 운세 로직 JS
├── images/                  # 실행 결과 예시 이미지
├── fortune_console.py       # 콘솔 입력 기반 운세
├── tarot_fortune_v3.py      # 콘솔 번호 선택 기반 운세
└── README.md                # 프로젝트 소개 문서
```

---

## 🛠️ 실행 방법

### 1. 콘솔 프로그램 실행

```
pip install rich
python fortune_console.py
```

### 2. 웹 프로그램 실행

* GitHub Pages로 업로드하거나
* `index.html` 파일을 더블 클릭해 브라우저에서 열기

---

## 👩‍💻 제작자

* 이름: 조은선 (Joeun Seon)
* GitHub: [@joeunseonn](https://github.com/joeunseonn)

---

✨ 이 프로젝트는 Python과 HTML/CSS를 활용해
콘솔과 웹을 모두 아우르는 운세 추천 시스템을 구현한 예시입니다.
