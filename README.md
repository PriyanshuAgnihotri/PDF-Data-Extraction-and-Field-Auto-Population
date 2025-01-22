# PDF Data Extraction and Field Auto-Population

## Overview
This project is designed to extract specific details (such as names, phone numbers, and addresses) from PDF documents and automatically populate fields in a frontend application. It includes a Python-based backend using Flask and pdfplumber for PDF parsing, along with regex-based text extraction for structured data.

## Features
- **PDF Parsing**: Extract raw text from uploaded PDF files using the `pdfplumber` library.
- **Data Extraction**: Identify and extract names, phone numbers, and addresses using regular expressions and heuristics.
- **REST API**: Expose an API endpoint for uploading PDFs and receiving extracted data.

## Technologies Used
- Python
- Flask
- pdfplumber
- Regular Expressions (Regex)

## Setup Instructions

### Prerequisites
1. Python 3.6 or later installed on your system.
2. Required Python packages:
   - `Flask`
   - `pdfplumber`

Install dependencies using:
```bash
pip install flask pdfplumber
```

### Running the Application
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Run the Flask application:
   ```bash
   python <script-name>.py
   ```
4. The application will be accessible at `http://127.0.0.1:5000`.

## API Usage

### Endpoint: `/upload`
**Method**: `POST`

**Description**: Upload a PDF file to extract details.

**Request**:
- `file`: PDF file to be processed.

**Response**:
- `names`: List of extracted names.
- `phone_numbers`: List of extracted phone numbers.
- `addresses`: List of extracted addresses.

**Example**:
```bash
curl -X POST -F "file=@sample.pdf" http://127.0.0.1:5000/upload
```

## Project Structure
```
project-directory/
├── <script-name>.py      # Main Python script for the Flask app
├── README.md             # Project documentation
```

## Future Enhancements
- Add support for additional data types (e.g., email addresses).
- Improve address extraction with NLP models.
- Create a frontend application for easier user interaction.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Feel free to fork this repository and submit pull requests for any enhancements or bug fixes.

