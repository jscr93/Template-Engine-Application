import EntityFileIO as efio
import Transclusion as trs

def generateAll_TXT(dataFilePath, templatefilepath, resultDocumentDirectoryPath):
    dataEntities = efio.getDataEntities(dataFilePath)
    if not dataEntities:
        return False
    return trs.transclusionTXT(templatefilepath, resultDocumentDirectoryPath, dataEntities)

def generateAll_PDF(dataFilePath, templatefilepath, resultDocumentDirectoryPath):
    dataEntities = efio.getDataEntities(dataFilePath)
    if not dataEntities:
        return False
    return trs.transclusionPDF(templatefilepath, resultDocumentDirectoryPath, dataEntities)

def generateAll_DOCX(dataFilePath, templatefilepath, resultDocumentDirectoryPath):
    dataEntities = efio.getDataEntities(dataFilePath)
    if not dataEntities:
        return False
    return trs.transclusionDOCX(templatefilepath, resultDocumentDirectoryPath, dataEntities)

def generateById_TXT(dataFilePath, templatefilepath, resultDocumentDirectoryPath, ids):
    dataEntities = efio.getDataEntitiesById(dataFilePath, ids)
    if not dataEntities:
        return False
    return trs.transclusionTXT(templatefilepath, resultDocumentDirectoryPath, dataEntities)

def generateById_PDF(dataFilePath, templatefilepath, resultDocumentDirectoryPath, ids):
    dataEntities = efio.getDataEntitiesById(dataFilePath, ids)
    if not dataEntities:
        return False
    return trs.transclusionPDF(templatefilepath, resultDocumentDirectoryPath, dataEntities)

def generateById_DOCX(dataFilePath, templatefilepath, resultDocumentDirectoryPath, ids):
    dataEntities = efio.getDataEntitiesById(dataFilePath, ids)
    if not dataEntities:
        return False
    return trs.transclusionDOCX(templatefilepath, resultDocumentDirectoryPath, dataEntities)