#Template Engine Application
#Epydoc Documentation Syntaxis

import os 
import sys

import TEA_routing as routing
import Transclusion


'''
def generateTxtAll():
    datafile = input("Data File Name: ")
    datafilepath = os.path.abspath("Data/" + datafile )

    resultDocumentDirectoryPath = os.path.abspath("Documents");

    dataEntities = ReadFromFile.generateEntitiesDictionaryList(datafilepath)
    if dataEntities==False:
        print("The file {0} could not be located".format(datafilepath))
        sys.exit()

    templatefile = input("Template File Name: ")
    templatefilepath = os.path.abspath("Templates/" + templatefile)
    transclusionResult = Transclusion.executeTransclusion(templatefilepath, resultDocumentDirectoryPath, dataEntities)
    if transclusionResult==False:
        print("The file {0} could not be located".format(templatefilepath))
        sys.exit()
'''

routing.routeParams()