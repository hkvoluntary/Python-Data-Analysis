import urllib.request
import fitz  # pip install PyMuPDF
from datetime import datetime

def download_pdf(url, output_path):
    try:
        # Download the PDF file
        urllib.request.urlretrieve(url, output_path)
        print(f"PDF successfully downloaded and saved as {output_path}")
    except Exception as e:
        print(f"Failed to download PDF: {e}")

# Example usage
pdf_url = "https://www.gld.gov.hk/egazette/tc_chi/gazette/file.php?year=2025&vol=29&no=6&extra=0&type=0&number=788"  # Replace with your PDF URL
output_file = "./downloaded_file.pdf"  # Path to save the downloaded PDF
download_pdf(pdf_url, output_file)


def pdf_to_text(pdf_path, output_txt_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    
    # Extract text from each page
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    
    # Save the extracted text to a text file
    with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)
    
    print(f"Text extracted and saved to {output_txt_path}")

# Example usage
pdf_path = "./downloaded_file.pdf"  # Path to your PDF file



now = datetime.now() # Get the current datetime object
# Convert the datetime object to a string with a specific format
formatted_time = now.strftime("%Y-%m-%d")

output_txt_path = "./output_" + formatted_time + ".txt"  # Path to save the text file
pdf_to_text(pdf_path, output_txt_path)
