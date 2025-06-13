// script.js

function getFortune() {
  const gender = document.getElementById("gender").value;
  const calendar = document.getElementById("calendar").value;
  const birthday = document.getElementById("birthday").value;
  const resultDiv = document.getElementById("result");

  // 입력 유효성 검사
  if (!gender || !calendar || !birthday) {
    resultDiv.style.display = "block";
    resultDiv.innerHTML = "⚠️ 모든 항목을 입력해 주세요.";
    resultDiv.style.color = "crimson";
    return;
  }

  // 운세 메시지 배열
  const fortunes = [
    "🌞 오늘은 밝은 기운이 가득합니다! 웃는 일이 많을 거예요.",
    "🌧 약간의 주의가 필요해요. 실수를 조심하세요.",
    "🎁 깜짝 선물 같은 일이 생길 수 있어요!",
    "🔥 당신의 열정이 최고조에 이르는 하루입니다.",
    "🧘‍♀️ 휴식과 재정비가 필요한 타이밍이에요.",
    "💖 누군가와 가까워지는 계기가 찾아옵니다."
  ];

  const randomIndex = Math.floor(Math.random() * fortunes.length);
  const selectedFortune = fortunes[randomIndex];

  // 결과 출력
  resultDiv.style.display = "block";
  resultDiv.style.color = "#333";
  resultDiv.innerHTML = `
    <strong>✅ 입력 정보</strong><br/>
    👤 성별: ${gender === "m" ? "남성" : "여성"}<br/>
    📅 양력/음력: ${calendar === "solar" ? "양력" : "음력"}<br/>
    🎂 생일: ${birthday}<br/><br/>
    <strong>🔮 오늘의 운세</strong><br/>
    ${selectedFortune}
  `;
}
