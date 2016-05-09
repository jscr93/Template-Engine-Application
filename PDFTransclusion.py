import os
import uuid

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def generatePDF(templatefilepath, resultDocumentDirectoryPath, dataEntities):
    print(templatefilepath)
    if not os.path.isfile(templatefilepath):
        return False
    TransclusionId = uuid.uuid1();
    TransclusionDocumentNumber = 1;
    for dataEntity in dataEntities:
        resultDocumentPath = "{0}\\{1}_{2}.pdf".format(resultDocumentDirectoryPath, TransclusionId, TransclusionDocumentNumber)   
        doc = SimpleDocTemplate(resultDocumentPath, pagesize=letter)
        parts = []
        style = ParagraphStyle(
            name='Normal',
            fontName='Helvetica-Bold',
            fontSize=9,
        )
        with open(templatefilepath,"r") as template_file:
            content = template_file.read().format(**dataEntity)
        parts.append(Paragraph(content, style))
        doc.build(parts)
        TransclusionDocumentNumber+=1
    return True