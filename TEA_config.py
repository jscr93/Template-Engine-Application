import os;

def getPaths():
    PATHS = {
        "data_file_path": "{0}\{1}".format(dataDirectoryPath,dataFileName),
        "template_file_path": "{0}\{1}".format(templatesDirectoryPath,templateFileName),
        "entity_model_file_path": "{0}\{1}".format(entityModelsDirectoryPath, entityModelFileName),
        "documents_directory_path": documentsDirectoryPath
    }
    return PATHS

appName = "TEA.py"

dataFileName                =   "Data_2"
templateFileName            =   "Template_1"
entityModelFileName         =   "EntityModel_1"

dataDirectoryPath           =   os.path.abspath("Data")
templatesDirectoryPath      =   os.path.abspath("Templates")
entityModelsDirectoryPath   =   os.path.abspath("EntityModels")
documentsDirectoryPath      =   os.path.abspath("Documents")

PATHS = getPaths()