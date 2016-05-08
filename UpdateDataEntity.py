import EntityFileIO as efio

def updateDataEntity(entityModelFilePath, dataFilePath, attribute, value):
    entityModel = efio.getEntityModel(entityModelFilePath)
    if (attribute in entityModel) == False:
        raise Exception("There is no '{0}' field name in {1}".format(attribute,entityModelFilePath))
    dataEntities = efio.getDataEntitiesNotMatchFirstAppearance(dataFilePath, attribute, value)
    print(dataEntities)
    '''
    for entityModelField in entityModel:
        dataEntity[entityModelField] = input("{0}: ".format(entityModelField))'''
    return True