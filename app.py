from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    email_text = data.get("email_text", "")
    if not email_text:
        return jsonify({"error": "No email text provided"}), 400
    
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Summarize this email:\n{email_text}")
    return jsonify({"summary": response.text if response else "Could not generate summary."})

if __name__ == "__main__":
    app.run(debug=True)
