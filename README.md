# 🗳️ VoteWise – Election Process Education Platform

**An AI-powered, interactive web application that educates citizens about India's democratic election process.**

Built for PromptWars Challenge 1 using Google Cloud + Gemini AI.

---

## 🌟 Features

- **Interactive Election Journey** – Step-by-step visual timeline of India's entire election process
- **AI-Powered Q&A (ElectionBot)** – Ask any election-related question, powered by Google Gemini
- **Knowledge Quiz** – 8 randomized questions with explanations to test your understanding
- **Voter Registration Guide** – Documents needed, how to register, key deadlines
- **Responsive Design** – Works beautifully on mobile and desktop

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + Flask |
| AI | Google Gemini 1.5 Flash |
| Frontend | Vanilla HTML/CSS/JS (no framework) |
| Deployment | Google Cloud Run |
| Containerization | Docker |

---

## 🚀 Local Development

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/election-edu.git
cd election-edu
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set environment variables
```bash
export GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4. Run locally
```bash
python app.py
```

Visit `http://localhost:8080`

---

## ☁️ Deploy to Google Cloud Run

### Prerequisites
- Google Cloud SDK installed
- A GCP project with billing enabled
- Google AI Studio API key (free at https://aistudio.google.com)

### Step 1: Authenticate
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

### Step 2: Enable required APIs
```bash
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

### Step 3: Build & Deploy
```bash
gcloud run deploy election-edu \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=your_api_key_here
```

Your app will be live at a `*.run.app` URL!

---

## 📁 Project Structure

```
election-edu/
├── app.py                  # Flask application & API routes
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
├── .gitignore
├── README.md
└── templates/
    ├── index.html          # Home page with AI chat
    ├── journey.html        # Interactive election timeline
    └── quiz.html           # Knowledge quiz
```

---

## 🔑 API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/journey` | GET | Election journey timeline |
| `/quiz` | GET | Interactive quiz |
| `/api/ask` | POST | AI Q&A (Gemini-powered) |
| `/api/quiz/questions` | GET | Fetch quiz questions |
| `/api/quiz/check` | POST | Validate quiz answer |

---

## 🎯 Educational Content Covered

- Voter eligibility and registration process
- Role of Election Commission of India (ECI)
- How EVMs (Electronic Voting Machines) work
- Model Code of Conduct
- First-Past-The-Post voting system
- NOTA (None Of The Above) option
- Vote counting and result declaration
- VVPAT paper trail system

---
