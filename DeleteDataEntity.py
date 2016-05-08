import EntityFileIO as efio

def deleteDataEntities(dataFilePath):
    return efio.deleteDataEntities(dataFilePath)

def deleteDataEntityByAttribute(entityModelFilePath, dataFilePath, attribute, value):
    entityModel = efio.getEntityModel(entityModelFilePath)
    if (attribute in entityModel) == False:
        raise Exception("There is no '{0}' field name in {1}".format(attribute,entityModelFilePath))
    dataEntities = efio.getDataEntitiesNotMatch(dataFilePath, attribute, value)
    if dataEntities == False:
        return deleteDataEntities(dataFilePath)
    return efio.writeDataEntities(dataFilePath, dataEntities)