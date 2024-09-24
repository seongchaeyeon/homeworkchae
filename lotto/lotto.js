const todaySpan = document.querySelector("#today");
const numbersDiv = document.querySelector('.numbers');
const drawButton = document.querySelector('#draw');
const resetButton = document.querySelector('#reset');
const colors = ['orange', 'skyblue', 'red', 'purple', 'green'];
const today = new Date();

// 전역 변수로 lottoNumbers 선언
let lottoNumbers = [];

let year = today.getFullYear();
let month = today.getMonth() + 1;
let date = today.getDate();
todaySpan.textContent = `${year}년 ${month}월 ${date}일 `;

function paintNumber(number) {
  const eachNumDiv = document.createElement('div');
  eachNumDiv.classList.add('eachnum');
  let colorIndex = Math.floor(number / 10);
  eachNumDiv.style.backgroundColor = colors[colorIndex];
  eachNumDiv.textContent = number;
  numbersDiv.appendChild(eachNumDiv);
}

function drawLottoNumbers() {
  // 이전에 생성된 번호 및 화면에 표시된 번호 초기화
  lottoNumbers.splice(0, lottoNumbers.length);
  numbersDiv.innerHTML = "";

  while (lottoNumbers.length < 6) {
    let ran = Math.floor(Math.random() * 45) + 1;
    if (lottoNumbers.indexOf(ran) === -1) {
      lottoNumbers.push(ran);
      paintNumber(ran);
    }
  }
}

// 추첨 버튼 클릭 이벤트
drawButton.addEventListener('click', function() {
  drawLottoNumbers(); // 번호를 새로 생성
});

// 리셋 버튼 클릭 이벤트
resetButton.addEventListener('click', function() {
  lottoNumbers.splice(0, 6); // 생성된 번호 초기화
  numbersDiv.innerHTML = ""; // 화면에 표시된 번호 초기화
});
