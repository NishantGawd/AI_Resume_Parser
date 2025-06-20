# 🚀 Resume Parser App | Pinnacle Labs Internship

During my internship at **Pinnacle Labs**, I developed an **AI-powered Resume Parser App** designed to automate resume data extraction. This tool helps streamline recruitment workflows by extracting structured data from resumes in PDF and DOCX formats.

---

## 🛠 Technologies Used

* **Streamlit** — Interactive app interface
* **spaCy** — NLP for entity and information extraction
* **NLTK** — Text processing and tokenization
* **PyPDF2** — PDF parsing
* **pdfminer.six** — PDF text extraction
* **python-docx** — DOCX file parsing
* **pandas** — Data handling and export
* **openpyxl** — Excel file generation

---

## 💡 Features

✅ Upload and process resumes in **PDF** or **DOCX** formats
✅ Extract key details:

* Name
* Email
* Phone number
* Education
* Skills
* Work experience

✅ Export parsed data to **JSON** or **Excel**
✅ Lightweight and easy to deploy

---

## ⚙️ Installation

📌 **Clone the repository**

```bash
git clone https://github.com/your-username/resume-parser-app.git
cd resume-parser-app
```

📌 **Install dependencies**

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit==1.33.0
pip install python-docx==0.8.11
pip install pdfminer.six==20221105
pip install PyPDF2==3.0.1
pip install openpyxl==3.1.2
pip install spacy==3.7.4
pip install nltk==3.8.1
pip install pandas==2.0.3
pip install python-magic==0.4.27
pip install "en-core-web-sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.0/en_core_web_sm-3.7.0-py3-none-any.whl"
```

---

## ▶️ How to Run

```bash
streamlit run app.py
```

* Open the browser link provided in your terminal
* Upload resumes
* View extracted data and download as JSON or Excel

---

## 💡 Future Improvements

* Add OCR support for scanned/image-based PDFs
* Improve extraction of skills and experience with advanced models
* Build API for integration into ATS systems
