import os
import pdfplumber
import re
from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define regex patterns for name, phone number, and address extraction
NAME_PATTERN = re.compile(r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)+\b')
PHONE_PATTERN = re.compile(r'\b\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b')
ADDRESS_KEYWORDS = ["street", "road", "avenue", "lane", "drive", "apartment", "building"]

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Function to extract specific details using regex and heuristics
def extract_details(text):
    # Extract names (heuristic approach for names with capitalized words)
    names = NAME_PATTERN.findall(text)

    # Extract phone numbers
    phone_numbers = PHONE_PATTERN.findall(text)

    # Extract addresses (simplistic heuristic using keywords)
    sentences = text.split(".\n")
    addresses = [sentence for sentence in sentences if any(keyword in sentence.lower() for keyword in ADDRESS_KEYWORDS)]

    return {
        "names": names,
        "phone_numbers": phone_numbers,
        "addresses": addresses
    }

# API endpoint to process the PDF
@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        # Save the uploaded file temporarily
        file_path = os.path.join("/tmp", file.filename)
        file.save(file_path)

        # Extract text and details
        text = extract_text_from_pdf(file_path)
        details = extract_details(text)

        # Clean up temporary file
        os.remove(file_path)

        return jsonify(details)

    return jsonify({"error": "File processing failed"}), 500

if __name__ == '__main__':
    app.run(debug=True)
