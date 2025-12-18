# 📄 AI PDF Designer | Premium

An intelligent web application that transforms descriptive text into professionally designed, print-ready PDF documents. It leverages **Google Gemini** for high-quality content and layout generation, combined with **Playwright** for high-fidelity PDF rendering.

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)

---

## ✨ Features

* **Intelligent Layout Engine**: Uses Gemini models to generate structured HTML documents styled with Tailwind CSS.
* [cite_start]**Multiple Document Profiles**: Specialized support for Business Reports, Executive Summaries, Academic Essays, and Project Proposals.
* **Rich Media Integration**: Includes an option for AI to source and embed relevant visuals using online images.
* **Pixel-Perfect PDFs**: Uses Playwright (Chromium) to render content into A4 format, ensuring no text is cut off and sections are properly aligned.
* [cite_start]**Modern Glassmorphic UI**: A sleek, responsive dashboard featuring glassmorphism effects and Tailwind CSS styling.
* **Real-time Logging**: Includes a built-in logging system to track requests, AI responses, and generation times.

---

## 🏗️ Architecture

1.  [cite_start]**Frontend**: A Tailwind-based dashboard (FastAPI + Jinja2) collects document requirements.
2.  **Backend**: FastAPI handles form data and coordinates the generation logic.
3.  **Intelligence**: The Gemini API generates sanitized HTML/CSS strings based on user prompts.
4.  **Rendering**: Playwright launches a headless browser to convert the HTML output into a professional A4 PDF.

---

## 🚀 Quick Start

### Prerequisites
* Python 3.9+
* A Google Gemini API Key

### 1. Clone the Repository
```bash
git clone [https://github.com/umar178/AI-PDF-Generator.git](https://github.com/umar178/AI-PDF-Generator.git)
cd AI-PDF-Generator
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
playwright install chromium
```
### 2. Set your gemini API Key in generator.py
```python
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

### 3. Run the application
```bash
python main.py
```
The server will start at http://127.0.0.1:8000.

### 🛠️ Configuration & Customization
Supported Models
You can select between different Gemini engines in the UI:

Gemini 1.5 Flash: Optimized for speed (Standard).

Gemini 2.5 Flash: Fast generation (Default).

Gemini 2.5 Pro: High-reasoning (Ultra).

Gemini 3 Pro: Latest experimental features.

Document Styling
The system uses a BASE_PROMPT in generator.py to define global styles. You can modify this prompt to change default fonts (like Arial or Helvetica), margins, or color schemes.

### 📂 Project Structure
```text
├── main.py              # FastAPI server and route handling
├── generator.py         # AI logic and Playwright PDF conversion
├── pages/
│   └── index.html       # Modern UI Dashboard 
├── requirements.txt     # Project dependencies
└── output.pdf           # The generated document output
```

### 👨‍💻 Author

Umer Karim - https://github.com/umar178