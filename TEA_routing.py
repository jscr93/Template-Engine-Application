import sys

from tabulate import tabulate

import TEA_config as config
import CreateDataEntity as create
import DeleteDataEntity as delete
import PrintDataEntity as printd
import UpdateDataEntity as update
import Transclusion as generate

def routeParams():
    """
        Application's Entry Point
        It reads the command line first parameter and decides which function to call
        
        @rtype: boolean
        @return: False if there is no first parameter. True on success.
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
    args.pop(0)
    
    
    
def routeFailed(args):
    print("Syntax error near '{0}'".format(args[0]))

def routeHelp(args):
    switcher = {
        config.appName: [["-new","Create a new data entity"],["-delete","Deletes one or more entities"],["-print","Prints one or more entities"],["-generates","Generate the specified format files for one or more entities"]],
        
        "-delete": [["all","Deletes all data entities"],["\"{Attribute}\" \"{value}\"","Deletes the data entity that matches the input"]],
        "-print": [["all","Prints all data entities"],["\"{Attribute}\" \"{value}\"","Prints the data entity that matches the input"]],
        "-update": [["\"{Attribute}\" \"{value}\"","Updates the first data entity that matches the input"]]
    }
    appHelp = switcher.get(args[0], routeFailed)
    try:
        print(tabulate(appHelp))
    except Exception:
        for helpRow in appHelp:
            print("{0}\t\t{1}".format(helpRow[0], helpRow[1]))
    
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