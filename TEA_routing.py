import sys

from tabulate import tabulate

import TEA_config as config
import CreateDataEntity as create
import DeleteDataEntity as delete
import PrintDataEntity as printd
import UpdateDataEntity as update
import GenerateFiles as generate

def routeParams():
    """
        Application's Entry Point
        It reads the command line first parameter and decides which function to call
        
        @rtype: boolean
        @return: False if there is no first parameter.
    """
    args = sys.argv
    if len(args) > 1:
        args.pop(0)
        switcher = {
            "-new":      routeNew,
            "-delete":   routeDelete,
            "-print":    routePrint,
            "-update":   routeUpdate,
            "-generate": routeGenerate
        }
        routeFunction = switcher.get(args[0], routeFailed)
        routeFunction(args)
        return True
    else:
        routeHelp(args)
        return False

def routeNew(args):
    args.pop(0)
    try:
        entity_id = create.createDataEntity(config.PATHS["entity_model_file_path"], config.PATHS["data_file_path"])
        if entity_id:
            print("The entity was successfully added with the id: {0}".format(entity_id))
        else:
            print("Data entity could not saved")
    except Exception as err:
        print(err)

def routeDelete(args):
    if len(args) > 1:
        args.pop(0)
        switcher = {
            "all":      deleteAll
        }
        routeFunction = switcher.get(args[0], deleteByAttribute)
        routeFunction(args)
        return True
    else:
        routeHelp(args)
        return False

def routePrint(args):
    if len(args) > 1:
        args.pop(0)
        switcher = {
            "all":      printAll
        }
        routeFunction = switcher.get(args[0], printByAttribute)
        routeFunction(args)
        return True
    else:
        routeHelp(args)
        return False

def routeUpdate(args):
    if len(args) > 1:
        args.pop(0)
        if len(args) > 1:
            attribute = args.pop(0);
            value = args.pop(0);
            try:
                entity_id = update.updateDataEntity(config.PATHS["entity_model_file_path"],config.PATHS["data_file_path"],attribute,value)
                if entity_id:
                    print("Data Entity updated successfully on id: {0}".format(entity_id))
                else:
                    print("Data Entity could not be updated")
            except Exception as err:
                print(err)
        else:
            routeFailed(args)
    else:
        routeHelp(args)

def routeGenerate(args):
    if len(args) > 1:
        args.pop(0)
        switcher = {
            "TXT": generateTXT,
            "PDF": generatePDF,
            "DOCX": generateDOCX
        }
        routeFunction = switcher.get(args[0], routeFailed)
        routeFunction(args)
    else:
        routeHelp(args)

    
def deleteAll(args):
    args.pop(0)
    try:
        if delete.deleteDataEntities(config.PATHS["data_file_path"]):
            print("All entities were deleted")
        else:
            print("No data entities were deleted")
    except Exception as err:
        print(err)
        
def deleteByAttribute(args):
    if len(args) > 1:
        attribute = args.pop(0);
        value = args.pop(0);
        try:
            if delete.deleteDataEntityByAttribute(config.PATHS["entity_model_file_path"],config.PATHS["data_file_path"],attribute,value):
                print("The data entities that matches the condition {0} = {1} have been deleted".format(attribute, value))
            else:
                print("No data entities were deleted")
        except Exception as err:
            print(err)
    else:
        routeFailed(args)
        
def printAll(args):
    args.pop(0)
    try:
        if not printd.printDataEntities(config.PATHS["data_file_path"]):
            print("No data entities to print")
    except Exception as err:
        print(err)
        
def printByAttribute(args):
    if len(args) > 1:
        attribute = args.pop(0);
        value = args.pop(0);
        try:
            if not printd.printDataEntityByAttribute(config.PATHS["entity_model_file_path"],config.PATHS["data_file_path"],attribute,value):
                print("No data entities to print")
        except Exception as err:
            print(err)
    else:
        routeFailed(args)

def generateTXT(args):
    if len(args) > 1:
        args.pop(0)
        switcher = {
            "all": generateAll_TXT
        }
        routeFunction = switcher.get(args[0], generateById_TXT)
        routeFunction(args)
    else:
        routeHelp(args)

def generatePDF(args):
    if len(args) > 1:
        args.pop(0)
        switcher = {
            "all": generateAll_PDF
        }
        routeFunction = switcher.get(args[0], generateById_PDF)
        routeFunction(args)
    else:
        routeHelp(args)
        
def generateDOCX(args):
    if len(args) > 1:
        args.pop(0)
        switcher = {
            "all": generateAll_DOCX
        }
        routeFunction = switcher.get(args[0], generateById_DOCX)
        routeFunction(args)
    else:
        routeHelp(args)
        
def generateAll_TXT(args):
    args.pop(0)
    try:
        if generate.generateAll_TXT(config.PATHS["data_file_path"], config.PATHS["template_file_path"], config.PATHS["documents_directory_path"]):
            print("Documents generated successfully")
        else:
            print("No documents were generated")
    except Exception as err:
        print(err)        
        
def generateAll_PDF(args):
    args.pop(0)
    try:
        if generate.generateAll_PDF(config.PATHS["data_file_path"], config.PATHS["template_file_path"], config.PATHS["documents_directory_path"]):
            print("Documents generated successfully")
        else:
            print("No documents were generated")
    except Exception as err:
        print(err)
        
def generateAll_DOCX(args):
    args.pop(0)
    try:
        if generate.generateAll_DOCX(config.PATHS["data_file_path"], config.PATHS["template_file_path"], config.PATHS["documents_directory_path"]):
            print("Documents generated successfully")
        else:
            print("No documents were generated")
    except Exception as err:
        print(err)
        
def generateById_TXT(args):
    try:
        if generate.generateById_TXT(config.PATHS["data_file_path"],config.PATHS["template_file_path"],config.PATHS["documents_directory_path"], args):
            print("Documents generated successfully")
        else:
            print("No documents were generated")
    except Exception as err:
        print(err)
            

def generateById_PDF(args):
    if generate.generateById_PDF(config.PATHS["data_file_path"],config.PATHS["template_file_path"],config.PATHS["documents_directory_path"], args):
        print("Documents generated successfully")
    else:
        print("No documents were generated")
        
def generateById_DOCX(args):
    if generate.generateById_DOCX(config.PATHS["data_file_path"],config.PATHS["template_file_path"],config.PATHS["documents_directory_path"], args):
        print("Documents generated successfully")
    else:
        print("No documents were generated")
        
        
        
def routeFailed(args):
    print("Syntax error near '{0}'".format(args[0]))
        
def routeHelp(args):
    switcher = {      
        "-delete": [["all","Deletes all data entities"],["\"{Attribute}\" \"{value}\"","Deletes the data entity that matches the input"]],
        "-print": [["all","Prints all data entities"],["\"{Attribute}\" \"{value}\"","Prints the data entity that matches the input"]],
        "-update": [["\"{Attribute}\" \"{value}\"","Updates the first data entity that matches the input"]],
        "-generate": [["TXT","Generates plain text documents with the data inserted on the template"],
                      ["PDF","Generates PDF documents with the data inserted on the template"]],
        "TXT": [["all","Generates TXT documents for all data entities"],["{id1} {id2} {id3} ...","Generates TXT documents for data entities with matched ids"]],
        "PDF": [["all","Generates PDF documents for all data entities"],["{id1} {id2} {id3} ...","Generates PDF documents for data entities with matched ids"]],
        "DOCX": [["all","Generates DOCX documents for all data entities"],["{id1} {id2} {id3} ...","Generates DOCX documents for data entities with matched ids"]]
    }
    appHelp = switcher.get(args[0], [["-new","Create a new data entity"],["-delete","Deletes one or more entities"],["-print","Prints one or more entities"],["-generates","Generate the specified format files for one or more entities"]])
    try:
        print(tabulate(appHelp))
    except Exception:
        for helpRow in appHelp:
            print("{0}\t\t{1}".format(helpRow[0], helpRow[1]))