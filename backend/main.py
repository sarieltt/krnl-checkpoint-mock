
from flask import Flask, request, jsonify
app = Flask(__name__)

KEYS = {
    "ABC123": {"type": "Lifetime", "hwid": None},
    "TRIAL456": {"type": "Trial", "hwid": None}
}

@app.route("/verify")
def verify():
    key = request.args.get("key")
    hwid = request.args.get("hwid")
    entry = KEYS.get(key)
    if entry:
        if entry["hwid"] is None:
            entry["hwid"] = hwid
        if entry["hwid"] == hwid:
            return jsonify({"valid": True, "type": entry["type"]})
    return jsonify({"valid": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
