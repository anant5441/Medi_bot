# 🧠 SafeSpace (Medi-Bot) - AI Mental Health Therapist

**SafeSpace** is an advanced AI-powered mental health assistant designed to provide empathetic support, therapeutic guidance, and crisis intervention. It leverages local LLMs (MedGemma via Ollama), Google Maps for finding local professionals, and Twilio for emergency contact integration.

## ✨ Features

- **Empathetic AI Therapist**: Conversational AI (MedGemma) that offers emotional attunement, normalization, and practical guidance.
- **Crisis Intervention**: Automatically detects crisis situations (e.g., self-harm ideation) and triggers an emergency call via Twilio.
- **Find Nearby Help**: Locates psychotherapists near a user-provided location using Google Maps.
- **Hybrid AI Logic**: Uses **LangGraph** to coordinate between the therapeutic LLM and external tools.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **AI/LLM**: Ollama (`alibayram/medgemma:4b`), LangChain, LangGraph, Google Gemini (Flash Lite for tool orchestration)
- **APIs**: Twilio (Voice, WhatsApp), Google Maps (Geocoding & Places)
- **Dependency Management**: `uv`

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have the following installed:

- **Python 3.11+**
- **[Ollama](https://ollama.com/)** (running locally)

You also need API accounts for:
- **Google Cloud Platform** (Maps Javascript API, Places API, Geocoding API, and Vertex AI/Gemini API key)
- **Twilio** (Account SID, Auth Token, and a verified phone number)

### 2. Clone the Repository

```bash
git clone <repository-url>
cd med_bot
```

### 3. Setup Environment & Dependencies

This project relies on `uv` for fast and reliable package management.

#### Using `uv`:

```bash
# Sync dependencies (creates .venv automatically)
uv sync

# OR install individually including optional extras if any
uv run main.py
```

`uv` automatically manages the virtual environment and dependencies defined in `pyproject.toml`.

### 4. Configure `config.py`

The project requires a configuration file with API keys. 

1. Navigate to the `backend/` directory.
2. Create a file named `config.py`.
3. Add the following Python variables to it:

**`backend/config.py`**
```python
# Google API Keys
GOOGLE_API_KEY = "your_google_gemini_api_key"
GOOGLE_MAPS_API_KEY = "your_google_maps_api_key"

# Twilio Configuration for Emergency Calls
TWILIO_ACCOUNT_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number" # Format: +1234567890

# Emergency Contact (The number to call in case of crisis)
EMERGENCY_CONTACT_NUMBER = "+19876543210" 
```

> **⚠️ Security Note:** Never commit your `config.py` file to version control. It is already included in `.gitignore`.

### 5. Setup Ollama Model

The bot uses the `alibayram/medgemma:4b` model. You must pull this model before running the app.

```bash
ollama pull alibayram/medgemma:4b
```
Make sure Ollama is running in the background (`ollama serve`).

---

## 🏃‍♂️ How to Run

You need to run both the backend server and the frontend interface.

### Step 1: Start the Backend

Open a terminal and run the FastAPI server:

```bash
# From the root directory
uvicorn backend.main:app --port 8000 --reload
```
*The backend will start at `http://localhost:8000`.*

### Step 2: Start the Frontend

Open a new terminal window/tab and run the Streamlit app:

```bash
# From the root directory
streamlit run frontend.py
```
*The application should automatically open in your browser at `http://localhost:8501`.*

---

## 📂 Project Structure

```
med_bot/
├── backend/
│   ├── ai_agent.py      # LangGraph agent definitions & tool binding
│   ├── config.py        # Configuration & API Keys (You create this)
│   ├── main.py          # FastAPI application entry point
│   └── tools.py         # Tool implementations (Ollama, Twilio, etc.)
├── frontend.py          # Streamlit user interface
├── main.py              # (Optional/Legacy entry point)
├── pyproject.toml       # Python dependencies configuration
└── README.md            # Project documentation
```


---
