from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.convert_html import ConvertHTMLToPDFUseCase
from app.infrastructure.pdf_generator import PDFGenerator

router = APIRouter()

class HTMLRequest(BaseModel):
    html: str

@router.post("/convert")
def convert_html_to_pdf(request: HTMLRequest):
    try:
        use_case = ConvertHTMLToPDFUseCase(PDFGenerator())
        pdf_base64 = use_case.execute(request.html)
        return { "pdf_base64": pdf_base64 }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
