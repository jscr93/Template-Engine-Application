import EntityFileIO as efio

def createDataEntity(entityModelFilePath, dataFilePath):
    dataEntities = efio.getDataEntities(dataFilePath)
    if dataEntities == False:
        dataEntities = []
        entity_id = 1
    else:
        entity_id = int(dataEntities[len(dataEntities)-1]["id"]) + 1
    entityModel = efio.getEntityModel(entityModelFilePath)
    if entityModel == False:
        raise Exception("The entity model file {0} does not contain any field name".format(entityModelFilePath))
    dataEntity = {}
    dataEntity["id"] = entity_id
    for entityModelField in entityModel:
        dataEntity[entityModelField] = input("{0}: ".format(entityModelField))
    dataEntities.append(dataEntity)
    result = efio.writeDataEntities(dataFilePath, dataEntities)
    if result == False:
        return False
    return entity_id
    
    