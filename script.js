async function sendCode() {
    let code = document.getElementById("codeInput").value;

    if (code.trim() === "") return;

    let chatBox = document.getElementById("chatBox");

    // 🟢 USER MESSAGE
    let userMsg = document.createElement("div");
    userMsg.className = "message user";
    userMsg.innerText = code;
    chatBox.appendChild(userMsg);

    // Clear input
    document.getElementById("codeInput").value = "";

    // 🔄 LOADING MESSAGE
    let loading = document.createElement("div");
    loading.className = "message ai";
    loading.innerText = "⏳ Checking code...";
    chatBox.appendChild(loading);

    try {
        let response = await fetch("https://ai-coding-helper-2b9k.onrender.com/explain", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ code: code })
        });

        let data = await response.json();

        // Remove loading
        chatBox.removeChild(loading);

        // 🤖 AI RESPONSE
        let aiMsg = document.createElement("div");
        aiMsg.className = "message ai";
        aiMsg.innerText = data.reply;
        chatBox.appendChild(aiMsg);

    } catch (error) {
        chatBox.removeChild(loading);

        let errMsg = document.createElement("div");
        errMsg.className = "message ai";
        errMsg.innerText = "❌ Error connecting to server";
        chatBox.appendChild(errMsg);
    }

    // Auto scroll
    chatBox.scrollTop = chatBox.scrollHeight;
}