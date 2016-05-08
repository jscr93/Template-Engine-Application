import os
import uuid
def executeTransclusion(templatefilepath, resultDocumentDirectoryPath, dataEntities):
    if os.path.isfile(templatefilepath) == False:
        return false
    TransclusionId = uuid.uuid1();
    TransclusionDocumentNumber = 1;
    for dataEntity in dataEntities:
        resultDocumentPath = "{0}\\{1}_{2}.txt".format(resultDocumentDirectoryPath, TransclusionId, TransclusionDocumentNumber)
        with open(templatefilepath,"r") as template_file, open(resultDocumentPath,"w") as result_file:
            result_file.write(template_file.read().format(**dataEntity));
        TransclusionDocumentNumber+=1
    return True
