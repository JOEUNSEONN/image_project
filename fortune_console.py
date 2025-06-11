# fortune_console.py

from rich import print
from rich.panel import Panel
from rich.align import Align
from datetime import datetime
import random

# 1. 환영 메시지
print(Panel.fit("[bold yellow]🌟 나의 오늘의 운세 보기 🌟[/bold yellow]", border_style="bright_magenta"))

# 2. 사용자 입력 받기
gender = input("성별을 입력하세요 (m/f): ").strip().lower()
calendar = input("양력 또는 음력을 입력하세요 (solar/lunar): ").strip().lower()
birthday = input("생일을 입력하세요 (예: 2001-06-11): ").strip()

# 3. 날짜 포맷 검사
try:
    birth_date = datetime.strptime(birthday, "%Y-%m-%d")
except ValueError:
    print("[red]⚠️ 생일 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 입력해주세요.[/red]")
    exit()

# 4. 입력 확인 메시지
print(Panel.fit(
    f"[bold cyan]입력 확인:[/bold cyan]\n"
    f"성별: [green]{gender}[/green]\n"
    f"양력/음력: [green]{calendar}[/green]\n"
    f"생일: [green]{birth_date.strftime('%Y년 %m월 %d일')}[/green]",
    title="✅ 입력 완료",
    border_style="cyan"
))

# 5. 운세 메시지 예시
fortunes = [
    "🌞 오늘은 밝은 기운이 가득합니다! 웃는 일이 많을 거예요.",
    "🌧 약간의 주의가 필요해요. 실수를 조심하세요.",
    "🎁 깜짝 선물 같은 일이 생길 수 있어요!",
    "🔥 당신의 열정이 최고조에 이르는 하루입니다.",
    "🧘‍♀️ 휴식과 재정비가 필요한 타이밍이에요.",
    "💖 누군가와 가까워지는 계기가 찾아옵니다.",
]

# 6. 결과 출력
selected_fortune = random.choice(fortunes)

result_panel = Panel(
    Align.center(f"[bold magenta]{selected_fortune}[/bold magenta]", vertical="middle"),
    title="🔮 오늘의 운세",
    border_style="bright_blue",
    width=60
)

print(result_panel)
