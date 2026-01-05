async function compare() {
    const
        promptInput = document.getElementById("promptInput").value;

        const response = await fetch("http://127.0.001:8000/compare", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ prompt: promptInput }),
        });
        const data = await response.json();
        
        document.getElementById("openaiResponse").innerText = data.openai_response;
        document.getElementById("claudeResponse").innerText = data.claude_response; 
        document.getElementById("gemminiResponse").innerText = data.gemmini_response;
}