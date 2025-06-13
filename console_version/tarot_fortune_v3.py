# tarot_fortune_v3.py

from rich import print
from rich.panel import Panel
from rich.align import Align
import random

# 카드별 고정 메시지 (1~5번)
tarot_cards = {
    "1": "🌞 새로운 시작! 오늘은 무언가 도전해보기에 좋은 날입니다.",
    "2": "🌧 감정 기복에 유의하세요. 혼자만의 시간을 가져보는 것도 좋아요.",
    "3": "❤️ 따뜻한 인간관계가 당신을 기다리고 있어요. 연락을 기다리는 사람이 있어요.",
    "4": "🪄 직감이 강해지는 하루! 선택의 순간, 자신의 감을 믿어보세요.",
    "5": "💤 충분한 휴식이 필요합니다. 오늘은 나를 위해 시간을 써보세요.",
}

# 무작위 운세 메시지
fortunes = [
    "🌞 오늘은 밝은 에너지가 가득한 하루입니다!",
    "🌧 약간의 주의가 필요한 날이에요. 실수하지 않게 조심!",
    "❤️ 사람들과의 관계가 더 깊어질 수 있는 날입니다.",
    "🪐 우주가 당신의 편이에요. 새로운 시도를 해보세요!",
    "💤 휴식이 필요한 하루입니다. 너무 무리하지 마세요.",
    "🎁 예기치 않은 좋은 일이 생길 수 있어요!",
    "🌀 고민이 해결될 기미가 보입니다. 믿고 나아가세요.",
    "🔥 당신의 열정이 누군가에게 영감을 줍니다."
]

# 타이틀 랜덤 목록
titles = [
    "✨ 오늘의 운세 ✨",
    "🔮 당신의 타로 메시지",
    "🃏 오늘의 카드",
    "📜 운명의 한 조각",
]

# 시작 메시지
print(Panel.fit("[bold yellow]🎴 타로 운세 프로그램에 오신 걸 환영합니다![/bold yellow]", border_style="magenta"))

# 기능 선택 안내
print("\n[cyan]원하는 모드를 선택하세요:[/cyan]")
print("[green]1.[/green] 랜덤 운세 뽑기")
print("[green]2.[/green] 직접 카드 번호 선택하기")
mode = input("👉 선택 (1 또는 2): ").strip()

# 랜덤 운세 모드
if mode == "1":
    selected_fortune = random.choice(fortunes)
    selected_title = random.choice(titles)
    panel = Panel(
        Align.center(f"[bold magenta]{selected_fortune}[/bold magenta]", vertical="middle"),
        title=f"[bold yellow]{selected_title}[/bold yellow]",
        border_style="bright_cyan",
        width=60
    )
    print(panel)

# 번호 선택 모드
elif mode == "2":
    print("\n[bold cyan]1~5번 카드 중 하나를 선택해 주세요![/bold cyan]")
    selected = input("🃏 번호 입력 (1~5): ").strip()

    if selected in tarot_cards:
        message = tarot_cards[selected]
        panel = Panel(
            Align.center(f"[bold magenta]{message}[/bold magenta]", vertical="middle"),
            title=f"[bold yellow]✨ 당신이 선택한 카드 #{selected} ✨[/bold yellow]",
            border_style="bright_blue",
            width=60
        )
        print(panel)
    else:
        print("[red]⚠️ 1부터 5 사이 숫자만 입력해 주세요.[/red]")

# 잘못된 입력
else:
    print("[red]⚠️ 잘못된 입력입니다. 1 또는 2를 선택해 주세요.[/red]")
