# gen-ai-resume-extractor-
🚀 AI Resume Summarizer + Skill Extractor

A fully automated pipeline using Streamlit, Gemini API, and n8n to convert PDF resumes into professional summaries and top skill insights.

✨ Overview

This project transforms raw PDF resumes into a clean, structured professional summary and Top 5 extracted skills using:

Streamlit (Frontend Web App)

n8n Workflow Automation (Resume text extraction & summarization)

Google Gemini 2.5 Flash (Skill extraction)

Webhook-based pipeline

AI-powered NLP

Users upload a PDF → The system processes the resume → Provides a summary + skills instantly.

🎯 Key Features
📄 1. PDF Resume Upload

Drag & drop PDF upload directly inside Streamlit UI.

🤖 2. Automated Resume Summarization

The uploaded PDF is sent to an n8n webhook, where:

PDF text is extracted

AI Agent produces a professional summary (150–250 words)

Summary returned via Webhook Response

(Reference: Webhook & AI Agent configuration in workflow JSON)


My workflow

🎯 3. AI Skill Extraction

After summarization, Gemini 2.5 Flash extracts exactly Top 5 skills using a custom prompt:

“Extract the top 5 professional skills from this summary.”

(Reference: Gemini configuration inside Streamlit app)


Gui

🎨 4. Clean & Modern Streamlit UI

Includes:

Status indicators

Error handling

Upload checks

Beautiful formatting

Footer branding ("built by umesh teja")

🧠 Architecture Diagram
User PDF Upload
        │
        ▼
Streamlit Frontend (Gui.py)
        │ (POST PDF)
        ▼
n8n Webhook (pdf_summary)
        │
        ├─ Extract Text from File
        │
        ├─ AI Agent (Resume Summary Generator)
        │
        ▼
Respond to Webhook → Streamlit
        │
        ▼
Gemini 2.5 Flash → Extract Top 5 Skills
        │
        ▼
Final Output → Summary + Skills

🏗️ Project Structure
📦 AI-Resume-Summarizer/
│── Gui.py
│── My workflow.json
│── requirements.txt
│── .env
│── assets/
│     └── screenshot.png (add your UI image)
│── README.md

File References

Gui.py → Streamlit frontend


Gui

My workflow.json → n8n automation workflow


My workflow

requirements.txt → Required Python libraries


requirements

.env → Secrets (Gemini API key, n8n Webhook URL)


.env

🛠️ Tech Stack
Frontend

Streamlit

Python

Backend

n8n Automation

Webhooks

Document Parsing

AI Models

Gemini 2.5 Flash (for skill extraction)

LangChain Agent inside n8n (for summarization)

APIs

Google Generative AI

Custom n8n Webhook

🔧 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/AI-Resume-Summarizer.git
cd AI-Resume-Summarizer

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Setup .env file

Add:

GEMINI_API_KEY=your_api_key
N8N_WEBHOOK_URL=your_webhook_url


(Values referenced inside your .env file


.env

)

4️⃣ Run Streamlit app
streamlit run Gui.py

🧪 How It Works (End-to-End)
Step 1 — User Uploads PDF

Streamlit receives the file using:
st.file_uploader()
(Verified in Gui.py)


Gui

Step 2 — File sent to n8n Webhook
requests.post(WEBHOOK_URL, files=files)

Step 3 — n8n Extracts Text + Summarizes

ExtractFromFile node reads PDF

AI Agent creates structured summary (150–250 words)


My workflow

Step 4 — Streamlit receives the summary
Step 5 — Gemini extracts Top 5 Skills

Using prompt defined in Gui.py (Gemini model).


Gui

Step 6 — Results displayed to user
📸 UI Preview (Add Screenshot)
![App Screenshot](assets/screenshot.png)

🌟 Why This Project Is Awesome

Fully automated AI pipeline

Real-time PDF processing

Two AI systems working together (n8n + Gemini)

Fast, clean, modern frontend

Perfect portfolio project for AI Engineer / Data Engineer / Automation Developer

👨‍💻 Developer

Created by Umesh Teja Chowdary
Passionate about AI, Automation, and Intelligent Workflow Systems.
