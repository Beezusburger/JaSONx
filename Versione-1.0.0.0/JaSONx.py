'''
@author = "Jury Francia, Simone Olivieri"
@version = "1.0"
@email = "j.francia@reply.it, s.olivieri@reply.it"
'''

import os
import utility

'''CONFIGURATION'''
'''Legge il file di configurazione in cui sono presenti i path per le cartelle -> templates, hierarchy, json'''
paths = utility.readFileJSON(os.path.realpath (''), "\\configuration\\pathConfiguration.json")
templatesPath = paths["templatesPath"]
jsonPath = paths["jsonPath"]
hierarchyPath = paths["hierarchyPath"]

'''CONSTANT DATA'''
'''Dati inseriti manualmente tramite GUI, valorizzati con la funzione setConstantData()'''
user_name = ""
password = ""
match_group_value = ""
name_file_hierarchy = ""
dizMeters = {}
serial_number = ""
prefix_match_group_value = ""

'''SETTING CONSTANT DATA'''
'''Richiamata da bottone "send data"'''
def setConstantData(user, psw, mgvalue, nfhierarchy, prefix_mgvalue):  
    global user_name, password, match_group_value, name_file_hierarchy, dizMeters, serial_number, prefix_match_group_value
    user_name = user
    password = psw
    match_group_value = mgvalue
    name_file_hierarchy = nfhierarchy
    prefix_match_group_value = prefix_mgvalue
    dizMeters, serial_number = searchMeters()
    
'''CREATE DIZ METERS'''
'''Crea un dizionario come segue -> {"nomeMeter":["misuraMeter.tipo1", "misuraMeter.tipo2", "misuraMeter.tipoN"]}'''
def searchMeters():
    hierarchy = utility.readFileXML(hierarchyPath, name_file_hierarchy)
    count=0
    serial_number = ""
    dizMeters={}
    for val in hierarchy.getElementsByTagName("Meter"):
        for localId in val.getElementsByTagName("LocalId"):    
            if(localId.toxml()[localId.toxml().find(">")+1:localId.toxml().find(".")] not in dizMeters):
                dizMeters[localId.toxml()[localId.toxml().find(">")+1:localId.toxml().find(".")]] = [localId.toxml().strip("</LocalId>")]
            else:
                dizMeters[localId.toxml()[localId.toxml().find(">")+1:localId.toxml().find(".")]] += [localId.toxml().strip("</LocalId>")] 
        if(count==0):
            for description in val.getElementsByTagName("Description"):
                serial_number = description.toxml().split("\n")[0].split("=")[1]
                count+=1       
    return(dizMeters, serial_number)
    
'''CREATE FILES JSON'''
'''Richiamata dalla funzione startCreateJSON"'''
def createJSON(nameMeter, folder, template):    
    file = utility.readFileJSON(templatesPath, template)
    file["parameters"]["serial_number"] = serial_number
    file["parameters"]["model"] = template[:template.find(".")]
    file["parameters"]["user_name"] = user_name
    file["parameters"]["password"] = password
    key = file["parameters"]["file_name_filter"]
    key["match_group_value"] = prefix_match_group_value+match_group_value
    file["parameters"]["meter_name"] = nameMeter
    file["parameters"]["maker"] = nameMeter
    for measureMeter in file["parameters"]["filter_tag"]:
        if(measureMeter["tag"]!="CommunicationCode"):
            measureMeter["tag"] = measureMeter["tag"].replace(measureMeter["tag"][:measureMeter["tag"].find(".")], nameMeter)
    utility.saveFileJSON(jsonPath+folder+"\\", nameMeter+".json", file)

'''Cerca template in base al numero di misure presenti nella lista in input confrontate 
con le misure selezionate nel file di configurazione dei meter'''
def searchTemplate(numberMeasures):
    dizMetersConfig = utility.readFileJSON(os.path.realpath (''), "\\configuration\\meterMeasuresConfiguration.json")
    for model_meter, diz_value in dizMetersConfig.items():
        for key, value in diz_value.items():
            if(key == "measuresSelected" and value==numberMeasures):
                return(model_meter+".json", value)
             
'''Richiamara dal bottone "Create JSONs'''
def startCreateJSON():
    name_hierarchy = name_file_hierarchy[:name_file_hierarchy.find(".")]
    if(name_hierarchy not in os.listdir(jsonPath)):
        os.mkdir(jsonPath+name_hierarchy) 
    for meter_name, value in dizMeters.items():
        if(searchTemplate(len(value)) != None):
            meter_model, measures_selected = searchTemplate(len(value))
            createJSON(meter_name, name_hierarchy, meter_model)
    
def createDictMeters():
    diz_description_meters={}    
    for meter_name, value in dizMeters.items():
        if(searchTemplate(len(value)) != None):
            meter_model, measures_selected = searchTemplate(len(value))
            if(meter_name not in diz_description_meters):
                diz_description_meters[meter_name]={"meter_model":meter_model, "n_measures_sel":measures_selected}   
        else:
            if(meter_name not in diz_description_meters):
                diz_description_meters[meter_name]={"meter_model":"Model not found!", "n_measures_sel":"---"}
    return(diz_description_meters)    
        
def getListHierarchy():
    return(utility.createListFile(hierarchyPath))

def getListPrefix_mgvalue():
    return(utility.readFileJSON(os.path.realpath (''), "\\configuration\\prefixMatchGroupValue.json"))