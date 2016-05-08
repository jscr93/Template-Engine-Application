import os

"""
    Returns a list of dictionaries in which every dictionary represents a Data Entity (e.g. a person record)
    
    @type dataFilePath: string
    @param dataFilePath: the path of the file that contains the data entity records
"""
def getDataEntities(dataFilePath):
    if os.path.isfile(dataFilePath) == False:
        raise FileNotFoundError("The file {0} was not found".format(dataFilePath))
    dataEntities = []
    with open(dataFilePath,"r") as data_file:
        for line in data_file:
            line = line.rstrip()
            if line == ">":
                dataEntity = {}
                dataEntities.append(dataEntity)
            else:
                line = line.split(":",1)
                dataEntity[line[0]] = line[1]
    if len(dataEntities) == 0:
        return False
    return dataEntities

def getDataEntitiesMatch(dataFilePath, attribute, value):
    allDataEntities = getDataEntities(dataFilePath);
    if allDataEntities == False:
        return False
    dataEntities = []
    for dataEntity in allDataEntities:
        if dataEntity[attribute] == value:
            dataEntities.append(dataEntity)
    if len(dataEntities) == 0:
        return False
    return dataEntities

def getDataEntitiesNotMatch(dataFilePath, attribute, value):
    allDataEntities = getDataEntities(dataFilePath)
    if allDataEntities == False:
        return False
    dataEntities = []
    for dataEntity in allDataEntities:
        if dataEntity[attribute] != value:
            dataEntities.append(dataEntity)
    if len(dataEntities) == 0:
        return False
    return dataEntities

def getDataEntitiesNotMatchFirstAppearance(dataFilePath, attribute, value):
    allDataEntities = getDataEntities(dataFilePath)
    if allDataEntities == False:
        return False
    dataEntities = []
    found = False;
    for dataEntity in allDataEntities:
        if (dataEntity[attribute] != value) or found:
            dataEntities.append(dataEntity)
            found = True
    if len(dataEntities) == 0:
        return False
    return dataEntities


"""
    Returns the entity model - the field names for every data entity records (e.g. name, phone, etc.)
    
    @type dataFilePath: string
    @param dataFilePath: the path of the file that contains the entity model
"""
def getEntityModel(dataFilePath):
    if os.path.isfile(dataFilePath) == False:
        raise FileNotFoundError("The file {0} was not found".format(dataFilePath))
    dataTemplateModel = []
    with open(dataFilePath,"r") as data_file:
        for line in data_file:
            line = line.rstrip()
            dataTemplateModel.append(line)
    if len(dataTemplateModel) == 0:
        return False
    return dataTemplateModel


def writeDataEntities(dataFilePath,dataEntities):
    if os.path.isfile(dataFilePath) == False:
        raise FileNotFoundError("The file {0} was not found".format(dataFilePath))
    if len(dataEntities) == 0:
        return False
    with open(dataFilePath,"w") as data_file:
        for dataEntity in dataEntities:
            data_file.write(">\n")
            for key, val in dataEntity.items():
                data_file.write("{0}:{1}\n".format(key,val))
    return True

def deleteDataEntities(dataFilePath):
    if os.path.isfile(dataFilePath) == False:
        raise FileNotFoundError("The file {0} was not found".format(dataFilePath))
    if os.stat(dataFilePath).st_size == 0:
        return False
    with open(dataFilePath,"w") as data_file:
        data_file.seek(0)
        data_file.truncate()
    return True