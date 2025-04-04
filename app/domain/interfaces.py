from abc import ABC, abstractmethod

class PDFGeneratorInterface(ABC):
    @abstractmethod
    def generate_pdf(self, html: str) -> bytes:
        pass
