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
        data = request.get_json()
        name = data.get("name", "")
        email = data.get("email", "")
        message = data.get("message", "")

        if not name or not email or not message:
            return jsonify({"success": False, "message": "All fields are required."}), 400

        # Prepare the message to write to file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] Name: {name}, Email: {email}, Message: {message}\n"

        # Save the message to a file
        with open("messages.txt", "a", encoding="utf-8") as file:
            file.write(entry)

        return jsonify({"success": True, "message": "Thank you! Your message has been saved."})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"success": False, "message": "Server error. Could not save your message."}), 500

if __name__ == "__main__":
    app.run(debug=True)
