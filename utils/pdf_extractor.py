import PyPDF2
import io

def extract_text_from_pdf(file_bytes):
    """
    Takes PDF as bytes and returns extracted text as string.
    """
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    except Exception as e:
        print(f"Error extracting PDF text: {e}")
        return None
    return text