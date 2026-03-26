from flask import Flask, request, jsonify
from flask_cors import CORS   # ADD THIS

app = Flask(__name__)
CORS(app)   # ADD THIS

@app.route("/explain", methods=["POST"])
def explain_code():
    data = request.get_json()
    code = data.get("code")

    if "print" in code:
        reply = "This code prints something to the console."
    elif "for" in code:
        reply = "This code uses a loop."
    else:
        reply = "This is some code performing operations."

    return jsonify({"reply": reply})

import os

if __name__ == "__main__":
    print("Server is starting...")

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)