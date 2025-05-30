from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        print("Request received:", request.data)
        data = request.get_json()
        print("Parsed JSON:", data)

        name = data.get("name", "")
        email = data.get("email", "")
        message = data.get("message", "")

        if not name or not email:
            return jsonify({"success": False, "message": "All fields are required."}), 400

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] Name: {name}, Email: {email}, Message: {message}\n"

        with open("messages.txt", "a", encoding="utf-8") as file:
            file.write(entry)

        return jsonify({"success": True, "message": "Submitted. Thank You for your response!"})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False, "message": "Server error."}), 500

