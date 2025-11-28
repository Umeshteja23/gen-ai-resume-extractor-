import streamlit as st
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load secrets (Webhook + Gemini)

load_dotenv()
WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# 🎨 Streamlit UI

st.set_page_config(page_title="AI Resume Summarizer + Skills", page_icon="🤖")
st.title("📄 AI Resume Summarizer + Skill Extractor")

# PDF Upload
uploaded_file = st.file_uploader("📤 Upload Resume (PDF only)", type=["pdf"])

# Generate Summary + Skills

if st.button("✨ Generate Summary + Skills"):
    if not uploaded_file:
        st.warning("⚠️ Please upload a PDF file first.")
    elif not WEBHOOK_URL:
        st.error("❌ Webhook URL not found. Please set it in your .env file.")
    else:
        st.info("⏳ Sending your resume to n8n for summary generation...")

        # Send file to n8n webhook
        files = {'file': (uploaded_file.name, uploaded_file.getvalue(), 'application/pdf')}
        try:
            response = requests.post(WEBHOOK_URL, files=files, timeout=180)

            if response.status_code == 200:
                st.success("✅ Summary received successfully!")

                # Try JSON parse; fallback to text
                try:
                    result = response.json()
                    if isinstance(result, list) and len(result) > 0:
                        summary = result[0].get("output", "")
                    elif isinstance(result, dict):
                        summary = result.get("output", "") or result.get("summary", "")
                    else:
                        summary = response.text
                except:
                    summary = response.text

                # Display Summary
                st.subheader("🧾 Professional Summary:")
                st.write(summary.strip())

                # -----------------------------
                # 🎯 Gemini Skill Extraction
                # -----------------------------
                with st.spinner("Extracting top 5 skills using Gemini 2.5 Flash..."):
                    try:
                        prompt = f"Extract the top 5 professional skills from this text:\n\n{summary}\n\nReturn only the skill names, comma-separated."
                        model = genai.GenerativeModel("gemini-2.5-flash")
                        gemini_response = model.generate_content(prompt)
                        skills = gemini_response.text.strip()

                        st.subheader("💡 Top 5 Skills (Gemini 2.5 Flash):")
                        st.write(skills)

                    except Exception as e:
                        st.error(f"⚠️ Gemini API Error: {e}")

            else:
                st.error(f"❌ n8n request failed (Status: {response.status_code})")
                st.text_area("Error Details:", response.text, height=150)

        except Exception as e:
            st.error(f"⚠️ Connection Error: {e}")

# ----------------------------------
# 🧩 Footer
# ----------------------------------
st.markdown("---")
st.caption("built by umesh teja ")
