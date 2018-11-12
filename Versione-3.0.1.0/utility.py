'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.0.1.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

import json
from xml.dom import minidom
import os

def getConfigurationPath():
    return readJsonFile(os.path.join(os.path.realpath(''), "configuration", "pathConfiguration.json"))

'''Function for read json files'''
def readJsonFile(path):  
    with open(path, 'r') as file: 
        return json.load(file)

        
'''Configuration path'''
dict_configuration_path = getConfigurationPath()
json_templates_path = dict_configuration_path["json_templates_path"]
excel_templates_path = dict_configuration_path["excel_templates_path"]
json_files_path = dict_configuration_path["json_files_path"]
excel_files_path = dict_configuration_path["excel_files_path"]
hierarchy_path = dict_configuration_path["hierarchy_path"]

   
'''Function for save json files'''
def saveJsonFile(path, element):
    with open(path, 'w') as file:
        json.dump(element, file, indent=4)
   
'''Function for read xml files'''
def readXmlFile(path):
    return minidom.parse(path)

'''Function for create list of files'''
def createFileList(path, ext):
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
def createDirectoryList(path):
    lis = []
    for node in os.listdir(path):
        if(node.startswith(".")):
            continue
        fullpath = os.path.join(path, node)
        if(os.path.isdir(fullpath)): 
            lis.append(node)
    return lis
    
'''Function return substring'''
def getSubstring(string, start='', stop=''):  
    if(start != '' and stop != ''):
        return string[string.find(start)+len(start) : string.find(stop)]
        
    elif(start != '' and stop == ''):
        return string[string.find(start)+len(start) : ]
    
    elif(start == '' and stop != ''):
        return string[ : string.find(stop)]   
    else:
        return string
        
'''Refresh template configuration'''    
def refreshTemplateConfiguration():
    list_templates = createFileList(json_templates_path, ".json")
    add_measures_template(list_templates)
    
'''Count measures in file json template'''
def add_measures_template(list_templates):
    if(type(list_templates) == list):
        diz_templates = {}
        for template in list_templates:
            list_measures = createModelList(json_templates_path, template)     
            diz_templates[getSubstring(template, stop=".")] = {"measuressMax":len(list_measures), "measuresSelected":len(list_measures)}        
        saveJsonFile(os.path.join(os.path.realpath (''),"configuration", "meterMeasuresConfiguration.json"), diz_templates) 

'''Create dict model''' 
def createModelList(path, model):
    file_model = readJsonFile(os.path.join(path, model))
    list_measures = []
    for model in file_model["parameters"]["filter_tag"]:
        if(model["tag"] != "CommunicationCode"):
            list_measures.append(getSubstring(model["tag"], start="."))           
    return(list_measures)

