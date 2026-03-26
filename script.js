async function sendCode() {
    let code = document.getElementById("codeInput").value;

    let response = await fetch("http://127.0.0.1:5000/explain", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ code: code })
    });

    let data = await response.json();

    document.getElementById("responseBox").innerText = data.reply;
}