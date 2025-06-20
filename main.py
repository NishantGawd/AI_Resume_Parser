import streamlit as st
from parser.nlp_parser import ResumeParser
import tempfile
import os
import time
import pandas as pd
import json
import io
from datetime import datetime

# --- Scoring Function ---
def resume_score(data):
    score = 0
    if data.get('name'): score += 10
    if data.get('email'): score += 10
    if data.get('phone'): score += 10

    skills = data.get('skills', [])
    score += min(len(skills) * 5, 30)  # Up to 6 skills max for 30 pts

    if data.get('education'): score += 20
    if data.get('experience'): score += 20

    return min(score, 100)

# --- Format file info ---
def format_file_info(file):
    return f"**{file.name}** ({round(len(file.getvalue()) / 1024, 2)} KB)"

# --- Main App ---
def main():
    st.set_page_config(page_title="Resume Parser AI", page_icon="🧠", layout="centered")
    st.markdown("<style>body { background-color: #0e1117; color: #f0f0f0; }</style>", unsafe_allow_html=True)

    st.title("🧠 AI Resume Parser")
    st.markdown("Upload multiple resumes and extract structured info using NLP.")
    st.divider()

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Instructions")
        st.info("🔹 Upload `.pdf` or `.docx` files\n🔹 Click **Process Resumes**\n🔹 Download results below.")
        st.caption("Made with 💻 Streamlit + spaCy")

    uploaded_files = st.file_uploader(
        "📤 Upload Resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.markdown("### 📁 Files to Process")
        for file in uploaded_files:
            st.markdown(f"✅ {format_file_info(file)}")

    if st.button("🚀 Process Resumes"):
        if not uploaded_files:
            st.warning("⚠️ Please upload at least one file.")
            return

        results = []
        progress = st.progress(0)
        status_placeholder = st.empty()

        for i, file in enumerate(uploaded_files):
            try:
                status_placeholder.info(f"Processing: `{file.name}`")
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.name)[1]) as tmp:
                    tmp.write(file.getvalue())
                    tmp_path = tmp.name

                time.sleep(0.1)

                text = parser.extract_text(tmp_path)
                if text:
                    with st.spinner(f"Parsing with LLaMA: {file.name}"):
                        data = parser.parse_resume(text)

                if data:
                    data['filename'] = file.name
                    data['parsed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    data['resume_score'] = resume_score(data)
                    results.append(data)
                else:
                    st.warning(f"⚠️ Failed to parse resume for: {file.name}")

                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)

            except Exception as e:
                st.error(f"⚠️ Error processing {file.name}: {str(e)}")
                continue

            progress.progress((i + 1) / len(uploaded_files))

        status_placeholder.empty()

        if results:
            st.success(f"🎉 Processed {len(results)} file(s) successfully!")

            st.markdown("### 🔍 Parsed Results")
            st.dataframe(results, use_container_width=True)

            st.markdown("### 🏆 Resume Scores")
            for res in results:
                score = res['resume_score']
                color = "🟢" if score >= 70 else ("🟡" if score >= 40 else "🔴")
                st.markdown(f"- **{res['filename']}** → {color} Score: **{score} / 100**")

            # Excel download
            excel_buffer = io.BytesIO()
            pd.DataFrame(results).to_excel(excel_buffer, index=False)
            excel_buffer.seek(0)
            st.download_button(
                label="📥 Download Excel",
                data=excel_buffer,
                file_name="parsed_resumes.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

            # JSON download
            json_str = json.dumps(results, indent=2)
            st.download_button(
                label="📥 Download JSON",
                data=json_str,
                file_name="parsed_resumes.json",
                mime="application/json"
            )

if __name__ == "__main__":
    parser = ResumeParser()
    main()
