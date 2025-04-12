---

# 🔡 Morse Code Translator

A sleek web application built with *Django* that lets you:

- ✏️ Convert English text to Morse Code  
- 🕵️ Decode Morse Code back to English  
- 🖼️ Extract text from images using OCR and convert it to Morse  
- 🌐 Enjoy a beautiful, glassmorphism-inspired user interface

---

## ✨ Features

- *Text to Morse* conversion with support for alphabets, numbers, and punctuation  
- *Morse to Text* decoding with error handling  
- *OCR Integration* using Tesseract to extract text from uploaded images  
- *Clean UI/UX* using Tailwind CSS and minimalistic styling  
- *Supports future extensions* like voice input and pixel-to-morse conversion

---

## 🚀 Getting Started (Run Locally)

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/morse-code-translator.git
cd morse-code-translator

2. Set Up Virtual Environment

python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run Migrations

python manage.py makemigrations
python manage.py migrate

5. Install Tesseract-OCR

Download from: https://github.com/tesseract-ocr/tesseract

Set the path in views.py:


pytesseract.pytesseract.tesseract_cmd = r"C:\path\to\tesseract.exe"

6. Start the Server

python manage.py runserver

Then visit http://127.0.0.1:8000 in your browser.


---

✍️ Credits

Project by:

S. Sharanya

R. Ramya



---

🚧 Work in Progress

This project is actively being developed. New features such as voice-to-morse translation and advanced image encoding are planned!


---

📃 License

This project is licensed under the MIT License.

---