```markdown
# ✈️ AI Travel Planner

A full-stack AI travel recommendation app powered by CrewAI and OpenAI, served via FastAPI, with a reactive Streamlit user interface.

---

## Overview

The application accepts a city name from the user and triggers an autonomous CrewAI agent. The agent adopts the persona of a seasoned local travel curator to return exactly three tailored recommendations with actionable tips.

- **Frontend (`app.py`):** Streamlit UI to collect city input and display formatted recommendations.
- **Backend (`api.py`):** FastAPI REST API exposing a `/plan` endpoint that orchestrates the CrewAI agent execution.
- **Agent Framework:** CrewAI running on OpenAI LLMs.

---

## Project Structure

```text
travel-planner/
├── api.py              # FastAPI backend with CrewAI agent logic
├── app.py              # Streamlit frontend web interface
├── .env                # API keys and environment configuration (do not commit)
├── .gitignore          # Git exclusion rules
├── requirements.txt    # Project dependencies
└── README.md           # Documentation

```

---

## Prerequisites

* **Python:** 3.10 to 3.12 installed
* **OpenAI API Key:** Active key from platform.openai.com

---

## Getting Started

### 1. Clone & Set Up Virtual Environment

```bash
# Clone the repository
git clone <your-repo-url>
cd travel-planner

# Create virtual environment
python -m venv venv

# Activate virtual environment
# macOS / Linux:
source venv/bin/activate
# Windows (PowerShell):
# venv\Scripts\Activate.ps1

```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn streamlit requests crewai python-dotenv pydantic

```

*(Or via requirements file: `pip install -r requirements.txt`)*

### 3. Environment Variables Configuration

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL_NAME=gpt-4o-mini
OTEL_SDK_DISABLED=true
CREWAI_TELEMETRY_OPT_OUT=true

```

> **Security Note:** Never commit `.env` to version control. Add `.env` to your `.gitignore`.

---

## Running the Application

The frontend and backend run as independent services. Open two separate terminal sessions with the virtual environment activated in both.

### Terminal 1: Launch Backend (FastAPI)

```bash
uvicorn api:app --reload --port 8000

```

* **Backend Server:** `http://127.0.0.1:8000`
* **Interactive Swagger Docs:** `http://127.0.0.1:8000/docs`

### Terminal 2: Launch Frontend (Streamlit)

```bash
streamlit run app.py

```

* **Web App:** Opens automatically at `http://localhost:8501`

---

## API Reference

### `POST /plan`

Generates travel suggestions for a specified city.

**Request Body:**

```json
{
  "city": "Jaipur"
}

```

**Response (`200 OK`):**

```json
{
  "city": "Jaipur",
  "recommendations": "1. Amber Fort - hilltop fort with mirrored halls, go early\n2. Hawa Mahal - the pink facade, best in morning light\n3. City Palace - royal courtyards and a textile museum"
}

```

```

```
