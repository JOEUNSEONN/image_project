# 🔮 Rich 타로 운세 콘솔 프로그램

콘솔에서 감성적으로 운세를 확인할 수 있는 **Python 기반 미니 프로그램**입니다.  
`Rich` 라이브러리를 활용해 🎴 타로 카드 느낌의 텍스트 스타일과 패널을 구성하고,  
사용자가 **번호 선택 or 생년월일 입력**을 통해 **오늘의 운세**를 확인할 수 있습니다.

---

## ✨ 주요 기능

- ✅ 번호 선택 기반 타로 카드 운세 출력
- ✅ 성별·양력/음력·생일 기반 맞춤 운세 출력
- ✅ 이모지와 색상 강조로 감성적인 콘솔 스타일 구현
- ✅ 웹 소개 페이지 포함 (📄 `index.html`)

---

## 💻 실행 예시

### 📍 타로 카드 뽑기 (랜덤 or 번호 선택)
```python
from rich.panel import Panel
from rich.align import Align
print(Panel(Align.center("오늘의 카드 메시지"), title="🔮 타로 운세"))
