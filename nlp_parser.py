import spacy
import nltk
from nltk.corpus import stopwords
import re
import pandas as pd
from pdf2image import convert_from_path
import pytesseract
import os
import docx2txt
import fitz

# Download NLTK data
nltk.download('stopwords')
nltk.download('punkt')

class ResumeParser:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.stop_words = set(stopwords.words('english'))
        self.skills_db = [
            'python', 'java', 'sql', 'excel', 'machine learning',
            'data analysis', 'project management', 'word', 'powerpoint'
        ]  # Extend this list

    def extract_text(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()

        try:
            if ext == '.pdf':
                try:
                    text = ""
                    with fitz.open(file_path) as doc:
                        for page in doc:
                            text += page.get_text()
                    if text.strip():
                        return text
                    else:
                        raise ValueError("Empty PDF text, trying OCR...")
                except Exception:
                # Fallback to OCR
                    from pdf2image import convert_from_path
                    import pytesseract

                    images = convert_from_path(file_path)
                    text = ""
                    for img in images:
                        text += pytesseract.image_to_string(img)
                        return text

            elif ext == '.docx':
                return docx2txt.process(file_path)

        except Exception as e:
            print(f"Text extraction failed: {str(e)}")
            return ""

    
    def parse_resume(self, text):
        text = text.lower()
        doc = self.nlp(text)

    # Extract Name using NER
        name = None
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                name = ent.text.title()
                break

    # Email & Phone
        email = re.search(r'[\w\.-]+@[\w\.-]+', text)
        phone = re.search(r'\+?\d[\d\s\-().]{7,}\d', text)

    # Skills Matching (vector similarity or exact)
        skills = []
        for token in doc:
            if token.text in self.skills_db and token.text not in skills:
                skills.append(token.text)

    # Education
        education = []
        edu_keywords = ['bachelor', 'master', 'phd', 'degree', 'university', 'college', 'b.tech', 'm.tech']
        for sent in nltk.sent_tokenize(text):
            if any(keyword in sent for keyword in edu_keywords):
                education.append(sent.strip())

    # Experience
        experience = []
        exp_keywords = ['experience', 'worked', 'company', 'responsibilities', 'employment', 'internship']
        for sent in nltk.sent_tokenize(text):
            if any(keyword in sent for keyword in exp_keywords):
                experience.append(sent.strip())

        return {
            "name": name or "N/A",
            "email": email.group(0) if email else None,
            "phone": phone.group(0) if phone else None,
            "skills": skills,
            "education": education,
            "experience": experience
    }
