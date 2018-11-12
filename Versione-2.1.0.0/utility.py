'''
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "2.1"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

import json
from xml.dom import minidom
import os
import JaSONx

'''Function for read json files'''
def readFileJSON(path):   
    with open(path, 'r') as file: 
        return json.load(file)
    
'''Function for save json files'''
def saveFileJSON(path, element):
    with open(path, 'w') as file:
        json.dump(element, file, indent=4)
        
'''Function for read xml files'''
def readFileXML(path):
    return minidom.parse(path)

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

'''Return serial number and match group value from hierarchy'''
def getSerialNumberMgValueHierarchy(path):
    hierarchy = readFileXML(path)
    for val in hierarchy.getElementsByTagName("Site"):
        match_group_value = getSubstring(val.toxml(), "<Name>", "</Name>")
    for val in hierarchy.getElementsByTagName("Description"):
        serial_number = val.toxml().split("\n")[0].split("=")[1]
    return(serial_number, match_group_value)

'''Create dict -> {"meterName":["meterMeasureType1", "meterMeasureType2", "meterMeasureTypeN"]}'''
def createDictMeterMeasures(path):
    hierarchy = readFileXML(path)
    diz_meters={}
    for val in hierarchy.getElementsByTagName("Meter"):
        local_id = getSubstring(val.toxml(), "<LocalId>", "</LocalId>")
        meter_local_id = getSubstring(local_id, ">", ".")
        measure_local_id = getSubstring(local_id, start=".") 
        if(meter_local_id not in diz_meters):
                diz_meters[meter_local_id] = [measure_local_id]           
        else:
                diz_meters[meter_local_id] += [measure_local_id]
    return(diz_meters)    
        
'''Search value tag'''    
def searchXML(first_tag, second_tag, path):
    hierarchy = readFileXML(path)
    for val in hierarchy.getElementsByTagName(first_tag):
        return(getSubstring(val.toxml(), "<"+second_tag+">", "</"+second_tag+">"))
    
'''Get list hierarchy files'''     
def getListHierarchy():
    return(createListFile(JaSONx.hierarchyPath, ".xml"))  
    
'''Refresh template configuration'''    
def refreshTemplateConfiguration():
    paths = readFileJSON(os.path.join(os.path.realpath (''), "configuration\\pathConfiguration.json"))
    list_templates = createListFile(paths["templatesPath"], ".json")
    add_measures_template(list_templates)
    
'''Count measures in file json template'''
def add_measures_template(file_name):
    if(type(file_name) == str):
        list_measures = JaSONx.createListModel(file_name)
        diz_templates = readFileJSON(os.path.join(os.path.realpath (''), "configuration\\meterMeasuresConfiguration.json"))
        if(file_name not in diz_templates):
            diz_templates[getSubstring(file_name, stop=".")] = {"measuressMax":len(list_measures), "measuresSelected":len(list_measures)}
        saveFileJSON(os.path.join(os.path.realpath (''),"configuration", "meterMeasuresConfiguration.json"), diz_templates) 
    
    elif(type(file_name) == list):
        diz_templates = {}
        for template in file_name:
            list_measures = JaSONx.createListModel(template)     
            diz_templates[getSubstring(template, stop=".")] = {"measuressMax":len(list_measures), "measuresSelected":len(list_measures)}        
        saveFileJSON(os.path.join(os.path.realpath (''),"configuration", "meterMeasuresConfiguration.json"), diz_templates) 