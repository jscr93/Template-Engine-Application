from tabulate import tabulate

import EntityFileIO as efio

def printDataEntities(dataFilePath):
    dataEntities = efio.getDataEntities(dataFilePath)
    if dataEntities == False:
        return False
    printDataEntitiesByDictionaryList(dataEntities)
    return True

def printDataEntityByAttribute(entityModelFilePath, dataFilePath, attribute, value):
    entityModel = efio.getEntityModel(entityModelFilePath)
    if (attribute in entityModel) == False:
        raise Exception("There is no '{0}' field name in {1}".format(attribute,entityModelFilePath))
    dataEntities = efio.getDataEntitiesMatch(dataFilePath, attribute, value)
    if dataEntities == False:
        return False
    printDataEntitiesByDictionaryList(dataEntities)
    return True
    
    
def printDataEntitiesByDictionaryList(dataEntities):
    try:
        print(tabulate(dataEntities,headers="keys"))
    except Exception:
        for dataEntity in dataEntities:
            print("\n>")
            for key, val in dataEntity.items():
                print("{0}:{1}".format(key,val))