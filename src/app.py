import os
from flask import Flask, request, jsonify, send_from_directory
from IDCalculator import IDCalculator


app = Flask(__name__, static_folder=None)


UI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ui"))


@app.route("/")
def index():
    return send_from_directory(UI_DIR, "index.html")


@app.route("/<path:filename>")
def ui_files(filename):
    return send_from_directory(UI_DIR, filename)


@app.route("/api/checkdigit", methods=["POST"])
def checkdigit():
    data = request.get_json(silent=True) or {}
    id_number = data.get("id_number") or request.form.get("id_number") or ""
    try:
        calc = IDCalculator()
        result = calc.calculate(id_number)
        return jsonify({"ok": True, "check_digit": result})
    except TypeError as e:
        return jsonify({"ok": False, "error": str(e)}), 400
    except Exception as e:
        app.logger.exception("Unexpected error in /api/checkdigit")
        return jsonify({"ok": False, "error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
