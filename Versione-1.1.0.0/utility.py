'''
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "1.1"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

import json
from xml.dom import minidom
import os

'''Function for read json files'''
def readFileJSON(path, fileName):
    with open(path+fileName, 'r') as file:
        return json.load(file)
    
'''Function for save json files'''
def saveFileJSON(path, fileName, element):
    with open(path+fileName, 'w+') as file:
        json.dump(element, file, indent=4)
        
'''Function for read xml files'''
def readFileXML(path, fileName):
    return minidom.parse(path+fileName)

'''Function for create list of files'''
def createListFile(path, ext):
    lis = []
    for node in os.listdir(path):
        if(node.startswith(".")):
            continue
        if(node.endswith(ext)):
            fullpath = os.path.join(path, node)
            if(os.path.isfile(fullpath)): 
                lis.append(node)
    return lis

'''Function for create list of directories'''
def createListDirectory(path):
    lis = []
    for node in os.listdir(path):
        if(node.startswith(".")):
            continue
        fullpath = os.path.join(path, node)
        if(os.path.isdir(fullpath)): 
            lis.append(node)
    return lis