from app.domain.interfaces import PDFGeneratorInterface

class ConvertHTMLToPDFUseCase:
    def __init__(self, generator: PDFGeneratorInterface):
        self.generator = generator

    def execute(self, html: str) -> str:
        return self.generator.generate_pdf(html).decode('utf-8')
