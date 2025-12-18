import os
import re
import asyncio
from datetime import datetime
from google import genai
from playwright.async_api import async_playwright

# Configuration
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
client = genai.Client(api_key=GEMINI_API_KEY)

BASE_PROMPT = """
You are a professional document designer. Generate a clean, modern, and well-structured HTML 
document based on the content provided. Use inline CSS for styling. You may use tailwind for styling.
Your html generated page will be used in playwright to convert to pdf. The page size should be A4.
make sure the formatting has no errors and is visually appealing. The pages are properly formatted and have proper aligned sections.
Like no overlapping of pages and elements like images, no text being cut of into half because page ending etc.
Ensure it looks like a professional {pdf_type}.
Include margins, clear headings, and use standard fonts like Arial or Helvetica.
"""


def log(message, level="INFO"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")


async def generate_pdf(content_desc, pdf_type, model_name="gemini-2.5-flash", use_images=False):
    try:
        # 1. AI Generation Step
        image_instruction = ""
        if use_images:
            image_instruction = "\nYou are allowed to use images from the web online but make sure the images do not have any 404 error and are correct and relevant images"

        full_prompt = f"{BASE_PROMPT}{image_instruction}\n\nPDF Type: {pdf_type}\n\nContent details: {content_desc}"

        log(f"Requesting AI ({model_name}) to generate a {pdf_type}...")

        response = client.models.generate_content(
            model=model_name,
            contents=full_prompt
        )
        raw_html = response.text
        log(f"Received response from {model_name}.")

        # 2. Sanitization Step
        log("Sanitizing HTML code...")
        match = re.search(r'<!DOCTYPE html>.*</html>', raw_html, re.DOTALL | re.IGNORECASE)
        if match:
            clean_html = match.group(0)
            log("Successfully extracted HTML using Regex.")
        else:
            log("Regex failed to find tags. Cleaning Markdown code blocks manually.", "WARNING")
            clean_html = raw_html.strip().replace("```html", "").replace("```", "")

        # 3. File Preparation
        html_path = "temp_output.html"
        pdf_path = "output.pdf"
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(clean_html)
        log(f"Temporary HTML saved to {html_path}")

        # 4. PDF Rendering Step
        log("Launching Playwright browser...")
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            log("Rendering PDF (A4 Format)...")
            await page.set_content(clean_html)
            await page.pdf(path=pdf_path, format="A4", print_background=True)
            await browser.close()

        log(f"PDF successfully generated: {pdf_path}")
        return pdf_path

    except Exception as e:
        log(f"Error in generator.py: {str(e)}", "ERROR")
        raise e