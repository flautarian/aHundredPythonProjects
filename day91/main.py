import PyPDF2
import pyttsx3
import os

def pdf_to_speech(pdf_file):
    # Open the PDF file
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)

        # Initialize Text-to-Speech engine
        speaker = pyttsx3.init()

        # Loop through each page and extract text
        for page_num in range(total_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            # Convert text to speech
            speaker.say(text)

        # Run the speech engine
        speaker.runAndWait()

# Replace 'your_pdf_file.pdf' with your actual PDF file name

script_dir = os.path.dirname(__file__)

pdf_to_speech(f'{script_dir}/lorem-ipsum.pdf')