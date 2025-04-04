import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyDqbSbRCSCyyqHyy-e-RCE9mQy91AF-nIw"

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def summarize_email(email_text):
    """Summarizes the given email text using Gemini API."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Summarize this email:\n{email_text}")
    return response.text if response else "Could not generate summary."

if __name__ == "__main__":
    email_text = input("Paste the email content:\n")
    summary = summarize_email(email_text)
    print("\nEmail Summary:\n", summary)
