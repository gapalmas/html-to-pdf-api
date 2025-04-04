import pdfkit
import base64
from app.domain.interfaces import PDFGeneratorInterface

class PDFGenerator(PDFGeneratorInterface):
    def generate_pdf(self, html: str) -> bytes:
        pdf_bytes = pdfkit.from_string(html, False)
        return base64.b64encode(pdf_bytes)
