import PyPDF2

def extract_text(pdf_file):

    text = ""

    pdf = PyPDF2.PdfReader(pdf_file)

    for page in pdf.pages:

        content = page.extract_text()

        if content:
            text += content

    return text