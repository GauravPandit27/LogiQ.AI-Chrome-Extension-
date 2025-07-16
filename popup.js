document.getElementById("solve").addEventListener("click", async () => {
  const question = document.getElementById("question").value.trim();
  if (!question) {
    alert("Please enter a question first!");
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/solve", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });

    const data = await response.json();
    document.getElementById("answer").innerText = data.answer || "No answer found.";
  } catch (error) {
    console.error("Error:", error);
    document.getElementById("answer").innerText = "Server error or GenAI unavailable.";
  }
});

