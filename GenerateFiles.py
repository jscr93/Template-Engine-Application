import EntityFileIO as efio
import Transclusion as trs

def generateAll_TXT(dataFilePath, templatefilepath, resultDocumentDirectoryPath):
    dataEntities = efio.getDataEntities(dataFilePath)
    if not dataEntities:
        return False
    return trs.generateTXT(templatefilepath, resultDocumentDirectoryPath, dataEntities)

def generateALL_PDF(dataFilePath, templatefilepath, resultDocumentDirectoryPath):
    dataEntities = efio.getDataEntities(dataFilePath)
    if not dataEntities:
        return False
    return trs.generatePDF(templatefilepath, resultDocumentDirectoryPath, dataEntities)

def generateByAttribute_TXT(dataFilePath, templatefilepath, resultDocumentDirectoryPath, attribute, value):
    dataEntities = efio.getDataEntitiesMatch(dataFilePath, attribute, value)
    if not dataEntities:
        return False
    return trs.generateTXT(templatefilepath, resultDocumentDirectoryPath, dataEntities)

def generateByAttribute_PDF(dataFilePath, templatefilepath, resultDocumentDirectoryPath, attribute, value):
    dataEntities = efio.getDataEntitiesMatch(dataFilePath, attribute, value)
    if not dataEntities:
        return False
    return trs.generatePDF(templatefilepath, resultDocumentDirectoryPath, dataEntities)