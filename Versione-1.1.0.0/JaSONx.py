'''
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "1.1"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

import os
import utility
import configuration

'''Control paths exist'''
configuration.control_paths()

'''Configuration path, open file configuration.json'''
paths = utility.readFileJSON(os.path.realpath (''), "\\configuration\\pathConfiguration.json")
templatesPath = paths["templatesPath"]
jsonPath = paths["jsonPath"]
hierarchyPath = paths["hierarchyPath"]
templatesExcelPath = paths["templatesExcelPath"]
excelPath = paths["excelPath"]

'''Constant data variables'''
user_name = ""
password = ""
match_group_value = ""
name_file_hierarchy = ""
dizMeters = {}
serial_number = ""
   
'''Setting constant data, triggered by MainInterface'''
def setConstantData(user, psw, mgvalue, nfhierarchy):  
    global user_name, password, match_group_value, name_file_hierarchy, dizMeters, serial_number
    user_name = user
    password = psw
    match_group_value = mgvalue
    name_file_hierarchy = nfhierarchy
    dizMeters, serial_number = searchMeters()
    
'''Create dict -> {"meterName":["meterMeasureType1", "meterMeasureType2", "meterMeasureTypeN"]}'''
def searchMeters():
    hierarchy = utility.readFileXML(hierarchyPath, name_file_hierarchy)
    count=0
    serial_number = ""
    dizMeters={}
    for val in hierarchy.getElementsByTagName("Meter"):
        for localId in val.getElementsByTagName("LocalId"):    
            if(localId.toxml()[localId.toxml().find(">")+1:localId.toxml().find(".")] not in dizMeters):
                dizMeters[localId.toxml()[localId.toxml().find(">")+1:localId.toxml().find(".")]] = [localId.toxml()[localId.toxml().find(".")+1 : localId.toxml().find("</LocalId>")]]
            else:
                dizMeters[localId.toxml()[localId.toxml().find(">")+1:localId.toxml().find(".")]] += [localId.toxml()[localId.toxml().find(".")+1 : localId.toxml().find("</LocalId>")]]
        if(count==0):
            for description in val.getElementsByTagName("Description"):
                serial_number = description.toxml().split("\n")[0].split("=")[1]
                count+=1 
    return(dizMeters, serial_number)
    

'''Create files json triggered by startCreateJSON function'''
def createJSON(nameMeter, folder, template):    
    file = utility.readFileJSON(templatesPath, template)
    file["parameters"]["serial_number"] = serial_number
    file["parameters"]["model"] = template[:template.find(".")]
    file["parameters"]["user_name"] = user_name
    file["parameters"]["password"] = password
    key = file["parameters"]["file_name_filter"]
    key["match_group_value"] = name_file_hierarchy.split("_")[1]+"_"+match_group_value
    file["parameters"]["meter_name"] = nameMeter
    file["parameters"]["maker"] = nameMeter
    for measureMeter in file["parameters"]["filter_tag"]:
        if(measureMeter["tag"]!="CommunicationCode"):
            measureMeter["tag"] = measureMeter["tag"].replace(measureMeter["tag"][:measureMeter["tag"].find(".")], nameMeter)
    utility.saveFileJSON(jsonPath+folder+"\\", nameMeter+".json", file)

'''Search template'''
def searchTemplate(numberMeasures):
    dizMetersConfig = utility.readFileJSON(os.path.realpath (''), "\\configuration\\meterMeasuresConfiguration.json")
    list_model = []
    for model_meter, diz_value in dizMetersConfig.items():
        for key, value in diz_value.items():
            if(key == "measuresSelected" and value==numberMeasures):
                if(model_meter not in list_model):
                    list_model.append(model_meter)   
    return(list_model)
    
             
'''Start creation json, triggered by Create JSONs button'''
def startCreateJSON(diz_name_model_meter):
    name_hierarchy = name_file_hierarchy[:name_file_hierarchy.find(".")]
    if(name_hierarchy not in os.listdir(jsonPath)):
        os.mkdir(jsonPath+name_hierarchy) 
    for meter_name, meter_model in diz_name_model_meter.items():
        if(meter_model != "Model Not Found!"):
            createJSON(meter_name, name_hierarchy, meter_model+".json")


'''Create dict model''' 
def createListModel(model):
    file_model = utility.readFileJSON(templatesPath, model+".json")
    list_measures = []
    for model in file_model["parameters"]["filter_tag"]:
        if(model["tag"] != "CommunicationCode"):
            list_measures.append(model["tag"][model["tag"].find(".")+1 :])
    return(list_measures)
 

'''Control template for meter'''
def control_template(meter_name, list_measures_meter, list_measures_template):
    for template in list_measures_template:
        count = 0
        list_measures_template = createListModel(template)
        print(sorted(list_measures_meter))
        print(template, sorted(createListModel(template)))
        for measure in list_measures_meter:
            if(measure not in list_measures_template):
                break
            else:
                if(count+1 == len(list_measures_meter)):
                    return template
                else:
                    count+=1
    return "Model Not Found!"              
                
'''Create dict meters'''    
def createDictMeters():
    diz_description_meters = {}
    for meter_name, value in dizMeters.items():
        if(searchTemplate(len(value)) != []):
            list_templates = searchTemplate(len(value))
            diz_description_meters[meter_name] = control_template(meter_name, value, list_templates)
        else:
            diz_description_meters[meter_name] = "Model Not Found!"
    return(diz_description_meters)    
                 
def getListHierarchy():
    return(utility.createListFile(hierarchyPath, ".xml"))

def getListPrefix_mgvalue():
    return(utility.readFileJSON(os.path.realpath (''), "\\configuration\\prefixMatchGroupValue.json"))