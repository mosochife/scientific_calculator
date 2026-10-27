const exprInput = document.getElementById("expression");
const resultEl = document.getElementById("result");
const errorEl = document.getElementById("error");
const modeBtn = document.getElementById("mode");
const historyEl = document.getElementById("history");

let angleMode = "deg";
const history = []; // newest first, max 10

function insertText(text) {
  const start = exprInput.selectionStart;
  const end = exprInput.selectionEnd;
  const value = exprInput.value;
  exprInput.value = value.slice(0, start) + text + value.slice(end);
  const pos = start + text.length;
  exprInput.setSelectionRange(pos, pos);
  exprInput.focus();
}

function backspace() {
  let start = exprInput.selectionStart;
  const end = exprInput.selectionEnd;
  if (start === end && start > 0) start -= 1;
  exprInput.value = exprInput.value.slice(0, start) + exprInput.value.slice(end);
  exprInput.setSelectionRange(start, start);
  exprInput.focus();
}

function clearAll() {
  exprInput.value = "";
  resultEl.textContent = "";
  errorEl.textContent = "";
  exprInput.focus();
}

function renderHistory() {
  historyEl.replaceChildren();
  for (const item of history) {
    const li = document.createElement("li");
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = `${item.expression} = ${item.result}`;
    button.addEventListener("click", () => {
      exprInput.value = item.expression;
      exprInput.focus();
    });
    li.appendChild(button);
    historyEl.appendChild(li);
  }
}

function addHistory(expression, result) {
  history.unshift({ expression, result });
  if (history.length > 10) history.pop();
  renderHistory();
}

async function calculate() {
  const expression = exprInput.value.trim();
  errorEl.textContent = "";
  if (!expression) return;

  try {
    const response = await fetch("/calculate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ expression, angle_mode: angleMode }),
    });
    const data = await response.json();

    if (!response.ok) {
      resultEl.textContent = "";
      errorEl.textContent = data.error || "Something went wrong";
      return;
    }
    resultEl.textContent = "= " + data.result;
    addHistory(expression, data.result);
  } catch (err) {
    resultEl.textContent = "";
    errorEl.textContent = "Could not reach the server";
  }
}

// Button clicks (one listener for the whole keypad)
document.querySelector(".keys").addEventListener("click", (event) => {
  const button = event.target.closest("button");
  if (!button) return;

  if (button.dataset.insert) insertText(button.dataset.insert);
  else if (button.dataset.action === "back") backspace();
  else if (button.dataset.action === "clear") clearAll();
  else if (button.dataset.action === "equals") calculate();
});

// Keyboard: Enter calculates, Escape clears
exprInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    event.preventDefault();
    calculate();
  } else if (event.key === "Escape") {
    clearAll();
  }
});

// Degrees / radians toggle
modeBtn.addEventListener("click", () => {
  angleMode = angleMode === "deg" ? "rad" : "deg";
  modeBtn.textContent = angleMode.toUpperCase();
  exprInput.focus();
});

exprInput.focus();
