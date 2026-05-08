import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configure Gemini
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/journey")
def journey():
    return render_template("journey.html")

@app.route("/api/ask", methods=["POST"])
def ask_ai():
    """AI-powered Q&A about elections using Gemini."""
    data = request.get_json(silent=True) or {}
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "No question provided"}), 400

    if not GOOGLE_API_KEY:
        return jsonify({"answer": "AI assistant is not configured. Please set GOOGLE_API_KEY environment variable."}), 200

    try:
        from google import genai

        prompt = f"""You are ElectionBot, a friendly and knowledgeable educator about democratic election processes.
        
Answer the following question about elections in a clear, engaging, educational way suitable for all ages.
Keep your answer concise (2-4 sentences) and factual. Focus on Indian elections when relevant, but also cover global democratic processes.

Question: {question}

Answer:"""
        client = genai.Client(api_key=GOOGLE_API_KEY)
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
        )
        answer = (response.text or "").strip()
        if not answer:
            raise ValueError("Empty response from Gemini API")
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"Sorry, I couldn't process that right now. Please try again. ({str(e)})"}), 200

@app.route("/api/quiz/check", methods=["POST"])
def check_quiz():
    """Check quiz answer and provide explanation."""
    data = request.get_json()
    question_id = data.get("question_id")
    user_answer = data.get("answer")

    quiz_data = get_quiz_questions()
    q = next((q for q in quiz_data if q["id"] == question_id), None)
    if not q:
        return jsonify({"error": "Question not found"}), 404

    correct = user_answer == q["correct"]
    return jsonify({
        "correct": correct,
        "correct_answer": q["correct"],
        "explanation": q["explanation"]
    })

def get_quiz_questions():
    return [
        {
            "id": 1,
            "question": "What is the minimum age to vote in Indian General Elections?",
            "options": ["16 years", "18 years", "21 years", "25 years"],
            "correct": "18 years",
            "explanation": "The 61st Amendment to the Indian Constitution in 1988 lowered the voting age from 21 to 18 years, giving millions of young citizens a voice in democracy."
        },
        {
            "id": 2,
            "question": "Which body conducts elections in India?",
            "options": ["Supreme Court", "Parliament", "Election Commission of India", "President of India"],
            "correct": "Election Commission of India",
            "explanation": "The Election Commission of India (ECI) is an autonomous constitutional authority responsible for administering Union and State election processes in India."
        },
        {
            "id": 3,
            "question": "What does EVM stand for in Indian elections?",
            "options": ["Electronic Voting Machine", "Electoral Verification Module", "Election Validity Measure", "Electronic Vote Monitor"],
            "correct": "Electronic Voting Machine",
            "explanation": "EVMs (Electronic Voting Machines) replaced paper ballots in Indian elections to make the process faster, more accurate, and tamper-resistant."
        },
        {
            "id": 4,
            "question": "How often are Lok Sabha elections held in India?",
            "options": ["Every 3 years", "Every 4 years", "Every 5 years", "Every 6 years"],
            "correct": "Every 5 years",
            "explanation": "Members of the Lok Sabha (House of the People) are elected every 5 years through a general election, unless the house is dissolved earlier."
        },
        {
            "id": 5,
            "question": "What is NOTA in the context of Indian elections?",
            "options": ["None Of The Above", "National Opposition To All", "No Official Tally Allowed", "Neutral Open Transparent Agenda"],
            "correct": "None Of The Above",
            "explanation": "NOTA (None Of The Above) was introduced in 2013 by the Supreme Court. It allows voters to reject all candidates without abstaining, expressing dissatisfaction with available choices."
        },
        {
            "id": 6,
            "question": "What is a constituency in an election?",
            "options": ["A political party", "A geographic area that elects one representative", "A type of ballot", "The election headquarters"],
            "correct": "A geographic area that elects one representative",
            "explanation": "A constituency (or electoral district) is a geographic division where voters elect a representative. India has 543 Lok Sabha constituencies."
        },
        {
            "id": 7,
            "question": "What is the Model Code of Conduct?",
            "options": ["A law passed by Parliament", "Guidelines for parties & candidates during elections", "A voters' rights document", "A manual for EVM operation"],
            "correct": "Guidelines for parties & candidates during elections",
            "explanation": "The Model Code of Conduct is a set of guidelines issued by the ECI for political parties and candidates during elections to ensure free and fair elections."
        },
        {
            "id": 8,
            "question": "Which voting system does India use for Lok Sabha elections?",
            "options": ["Proportional Representation", "First-Past-The-Post (FPTP)", "Ranked Choice Voting", "Two-Round System"],
            "correct": "First-Past-The-Post (FPTP)",
            "explanation": "India uses the First-Past-The-Post system where the candidate with the most votes (not necessarily majority) in a constituency wins the seat."
        }
    ]

@app.route("/api/quiz/questions")
def quiz_questions():
    questions = get_quiz_questions()
    # Don't send correct answers to frontend
    safe_questions = [{"id": q["id"], "question": q["question"], "options": q["options"]} for q in questions]
    return jsonify(safe_questions)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
