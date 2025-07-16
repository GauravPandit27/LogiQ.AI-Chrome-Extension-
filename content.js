function detectQuestion(text) {
  const regex = /(solve|calculate|what is|write a function|output of this code)/i;
  return regex.test(text);
}

// Scan visible text on page
let bodyText = document.body.innerText;
if (detectQuestion(bodyText)) {
  chrome.runtime.sendMessage({
    type: "QUESTION_DETECTED",
    text: bodyText
  });
}

