'''
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "1.5"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

import os
import utility
import configuration

'''Control paths exist'''
configuration.control_paths()

'''Configuration path, open file configuration.json'''
paths = utility.readFileJSON(os.path.join(os.path.realpath (''), "configuration\\pathConfiguration.json"))
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
gateway_id = ""
environment_prefix = ""

'''Setting constant data, triggered by MainInterface'''
def setConstantData(user, psw, nameFileHierarchy, gatewayId, environmentPrefix):  
    global user_name, password, name_file_hierarchy, dizMeters, serial_number, match_group_value, gateway_id, environment_prefix
    user_name = user
    password = psw
    gateway_id = gatewayId
    environment_prefix = environmentPrefix
    name_file_hierarchy = utility.getSubstring(nameFileHierarchy, stop=".")
    dizMeters = utility.createDictMeterMeasures(os.path.join(hierarchyPath, name_file_hierarchy+".xml"))
    serial_number, match_group_value = utility.getSerialNumberMgValueHierarchy(os.path.join(hierarchyPath, name_file_hierarchy+".xml"))
    if(len(match_group_value) > 15):
        match_group_value = match_group_value[0:15]
    
'''Create files json triggered by startCreateJSON function'''
def createJSON(nameMeter, folder, template): 
    file = utility.readFileJSON(os.path.join(templatesPath, template))
    file["gateway_id"] = gateway_id
    file["parameters"]["environment_prefix"] = environment_prefix
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
    utility.saveFileJSON(os.path.join(jsonPath,folder, nameMeter), file)

'''Search template'''
def searchTemplate(numberMeasures):
    dizMetersConfig = utility.readFileJSON(os.path.join(os.path.realpath (''), "configuration\\meterMeasuresConfiguration.json"))
    list_model = []
    for model_meter, diz_value in dizMetersConfig.items():
        for key, value in diz_value.items():
            if(key == "measuresSelected" and value==numberMeasures):
                if(model_meter not in list_model):
                    list_model.append(model_meter)   
    return(list_model)    
             
'''Start creation json, triggered by Create JSONs button'''
def startCreateJSON(diz_name_model_meter):
    if(name_file_hierarchy not in os.listdir(jsonPath)):
        os.mkdir(os.path.join(jsonPath,name_file_hierarchy)) 
    for meter_name, meter_model in diz_name_model_meter.items():
        if(meter_model != "Model Not Found!"):
            createJSON(meter_name, name_file_hierarchy, meter_model+".json")

'''Create dict model''' 
def createListModel(model):
    file_model = utility.readFileJSON(os.path.join(templatesPath, model+".json"))
    list_measures = []
    for model in file_model["parameters"]["filter_tag"]:
        if(model["tag"] != "CommunicationCode"):
            list_measures.append(utility.getSubstring(model["tag"], start="."))           
    return(list_measures)
 
'''Control template for meter'''
def control_template(meter_name, list_measures_meter, list_template):
    for template in list_template:
        count = 0
        list_measures_template = createListModel(template)
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