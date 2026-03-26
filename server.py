from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Coding Helper Backend Running 🚀"

@app.route("/explain", methods=["POST"])
def explain_code():
    data = request.get_json()
    code = data.get("code")

    reply = ""

    # 🔍 ERROR DETECTION
    if "==" not in code and "=" in code and "if" in code:
        reply += "⚠️ Possible mistake: Use '==' for comparison, not '='.\n"

    if ":" not in code and ("if" in code or "for" in code or "def" in code):
        reply += "⚠️ Missing ':' in statement.\n"

    if "print(" in code and ")" not in code:
        reply += "⚠️ Missing closing bracket in print().\n"

    # 🤖 CODE UNDERSTANDING
    if "def " in code:
        reply += "🔹 Function is defined.\n"

    if "for " in code or "while " in code:
        reply += "🔹 Loop is used.\n"

    if "if " in code:
        reply += "🔹 Conditional statement is used.\n"

    if "print" in code:
        reply += "🔹 Output is printed.\n"

    if "return" in code:
        reply += "🔹 Function returns a value.\n"

    if reply == "":
        reply = "This code performs some operations."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)