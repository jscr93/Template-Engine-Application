import os

def getDataEntities(dataFilePath):
    """
        Retrieves from the data file a list of Data Entities (e.g. a person record)

        @type dataFilePath: string
        @param dataFilePath: the path of the file that contains the data entity records

        @rtype: a list of dictionaries if found, otherwise False
        @return: a list of dictionaries in which every dictionary represents a Data Entity
    """
    if not os.path.isfile(dataFilePath):
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
    """
        Returns a list of dictionaries that match a specific value of a dataEntity attribute. The function asumes that the attribute exists in the Entity Model

        @type dataFilePath: string
        @param dataFilePath: the path of the file that contains the data entity records
        
        @type attribute: string
        @param attribute: the attribute of the dataEntity which is going to be compared
        
        @type value: string
        @param value: the value of the attribute wich is going to be compared
        
        @rtype: list of dictionaries if found, otherwise False
        @return: list of data entities
    """
    allDataEntities = getDataEntities(dataFilePath);
    if not allDataEntities:
        return False
    dataEntities = []
    for dataEntity in allDataEntities:
        if dataEntity[attribute] == value:
            dataEntities.append(dataEntity)
    if len(dataEntities) == 0:
        return False
    return dataEntities

def getDataEntitiesNotMatch(dataFilePath, attribute, value):
    """
        Returns a list of dictionaries that don't match a specific value of a dataEntity attribute. The function asumes that the attribute exists in the Entity Model

        @type dataFilePath: string
        @param dataFilePath: the path of the file that contains the data entity records
        
        @type attribute: string
        @param attribute: the attribute of the dataEntity which is going to be compared
        
        @type value: string
        @param value: the value of the attribute wich is going to be compared
        
        @rtype: list of dictionaries if found, otherwise False
        @return: list of data entities
    """
    allDataEntities = getDataEntities(dataFilePath)
    if not allDataEntities:
        return False
    dataEntities = []
    for dataEntity in allDataEntities:
        if dataEntity[attribute] != value:
            dataEntities.append(dataEntity)
    if len(dataEntities) == 0:
        return False
    return dataEntities

def getDataEntitiesById(dataFilePath, ids):
    """
        Returns a list of dictionaries that match a specific id

        @type dataFilePath: string
        @param dataFilePath: the path of the file that contains the data entity records
        
        @type ids: list of strings
        @param attribute: the ids of the data entities to retrieve
        
        @rtype: list of dictionaries if found, otherwise False
        @return: list of data entities
    """
    allDataEntities = getDataEntities(dataFilePath)
    if not allDataEntities:
        return False
    dataEntities = []
    for dataEntity in allDataEntities:
        if dataEntity["id"] in ids:
            dataEntities.append(dataEntity)
    if len(dataEntities) == 0:
        return False
    return dataEntities


"""
    Returns the entity model - the field names for every data entity records (e.g. name, phone, etc.)
    
    @type dataFilePath: string
    @param dataFilePath: the path of the file that contains the entity model
    
    @rtype: list of strings
    @return: the list of the entity model fields
"""
def getEntityModel(dataFilePath):
    if not os.path.isfile(dataFilePath):
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
    """
        Writes in the data file the list of dataEntities passed as parameter
    
        @type dataFilePath: string
        @param dataFilePath: the path of the file that contains the entity model

        @type dataEntities: list of dictionaries
        @param dataEntities: The data entities that are going to be written
        
        @rtype: Boolean
        @return: True on success
    """
    if not os.path.isfile(dataFilePath):
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
    """
        Deletes all data entities from the file
    
        @type dataFilePath: string
        @param dataFilePath: the path of the file that contains the entity model

        @rtype: Boolean
        @return: True on success
    """
    if not os.path.isfile(dataFilePath):
        raise FileNotFoundError("The file {0} was not found".format(dataFilePath))
    if os.stat(dataFilePath).st_size == 0:
        return False
    with open(dataFilePath,"w") as data_file:
        data_file.seek(0)
        data_file.truncate()
    return True