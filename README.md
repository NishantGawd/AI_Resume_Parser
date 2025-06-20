Resume Parser App
An AI-powered Resume Parser App developed as part of my internship at Pinnacle Labs. This tool helps automate resume data extraction, enabling faster and more accurate processing for recruitment workflows.

🚀 Features

✅ Upload resumes in PDF or DOCX formats

✅ Automatically extract key information:

Name

Email

Phone number

Education

Skills

Work experience

✅ Export parsed data to JSON or Excel

✅ Simple and interactive Streamlit interface

✅ Lightweight and easy to deploy

🛠 Technologies Used

Streamlit

spaCy

NLTK

PyPDF2

pdfminer.six

python-docx

pandas

openpyxl

⚙️ Installation

Clone the repo:

bash

git clone https://github.com/your-username/resume-parser-app.git

cd resume-parser-app

pip install -r requirements.txt

Or manually install:

bash
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

▶️ How to Run

bash

streamlit run app.py

Open the browser link shown in your terminal.

Upload resumes (PDF/DOCX).

View and download the extracted data.

💡 Future Improvements

Add support for image-based PDFs using OCR

Improve skill and experience extraction with advanced models

Build REST API for integration

