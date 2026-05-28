# Python AI Showcase

Welcome to the Python AI Showcase demo project! This dashboard demonstrates both Classical Machine Learning and Generative AI using clean, modern Python code.

## 🚀 Quick Start Guide

Follow these steps to set up and run the demo application locally on Windows.

### Step 1: Open a terminal & Navigate to this folder
Open PowerShell or Command Prompt, and change directory to this folder:
```powershell
cd "C:\Users\jetad\.gemini\antigravity\scratch\python_ai_demo"
```

### Step 2: Create a Virtual Environment (Recommended)
Creating a virtual environment ensures dependencies don't conflict with your other projects.
```powershell
python -m venv venv
```

### Step 3: Activate the Virtual Environment
Activate the environment to start using it:
```powershell
# In PowerShell:
.\venv\Scripts\Activate.ps1

# In Command Prompt (cmd.exe):
.\venv\Scripts\activate.bat
```

### Step 4: Install Dependencies
Install all required libraries using pip:
```powershell
pip install -r requirements.txt
```

### Step 5: (Optional) Set up your Gemini API Key
To use the Generative AI features, set your API key as an environment variable, or paste it directly in the app.
```powershell
# Set it for the current terminal session:
$env:GEMINI_API_KEY="your-api-key-here"
```
*(You can get a free API Key from [Google AI Studio](https://aistudio.google.com/))*

### Step 6: Run the App
Launch the Streamlit app:
```powershell
streamlit run app.py
```

The application will build, start up, and automatically open in a web browser window (usually at `http://localhost:8501`).

---

## 📂 Project Structure

- `app.py`: The main entrypoint. Handles page layouts, sidebar navigation, the machine learning pipeline, and the Generative AI client integration.
- `requirements.txt`: Manages python dependencies.
- `README.md`: This file.
