'''
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "1.1"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

import os
import utility
import JaSONx
import openpyxl 

'''Configuration path, open file configuration.json'''
paths = utility.readFileJSON(os.path.realpath (''), "\\configuration\\pathConfiguration.json")
templatesPath = paths["templatesPath"]
jsonPath = paths["jsonPath"]
hierarchyPath = paths["hierarchyPath"]
templatesExcelPath = paths["templatesExcelPath"]
excelPath = paths["excelPath"]

'''Constant data variables'''
site_name = ""
environment_prefix = ""


'''Setting constant data, triggered by MainInterface'''
def setConstantData(site, folder):  
    global site_name
    site_name = site   
    start(folder)
    
    
'''Create dict meters'''
def search_json(path, diz_xml):
    global environment_prefix
    file_list = utility.createListFile(path)
    diz_meters={}
    environment_prefix = ""   
    count = 0  
    for file in file_list:
        file_json = utility.readFileJSON(path+"\\",file)
        
        if(count == 0):
            environment_prefix = file_json["parameters"]["environment_prefix"]
            count+=1
        meter_name = file_json["parameters"]["meter_name"]
        for key in file_json["parameters"]["filter_tag"]:      
            if(key["tag"]!="CommunicationCode"):
                if(meter_name not in diz_meters):
                    diz_meters[meter_name] = []
                diz_meters[meter_name] += [{key["tag"] [key["tag"].find(".")+1:] : {"id":key["id"], "period":key["period"], "name":diz_xml[key["tag"]]}}]        
    return([diz_meters, environment_prefix])

'''Create dict meters from xml'''
def create_dict_xml(name_hierarchy):
    diz_xml = {}
    hierarchy = utility.readFileXML(hierarchyPath, name_hierarchy)
    for val in hierarchy.getElementsByTagName("Meter"):
        diz_xml[val.toxml()[val.toxml().find("<LocalId>")+9 : val.toxml().find("</LocalId>")]] = val.toxml()[val.toxml().find("<Name>")+6 : val.toxml().find("</Name>")]   
    return(diz_xml) 

'''Create excel file'''    
def createExcelSheet(list_meters_json):
    diz_json = list_meters_json[0]
    environment_prefix = list_meters_json[1] 
    excel_document = openpyxl.load_workbook(templatesExcelPath+"Meter Upload Template LEONARDO.xlsx")
    sheet = excel_document.active
    number_cell = 7       
    for meter in diz_json.values():       
        for lst in meter:                       
            for diz, val in lst.items():
                sheet['A'+str(number_cell)] = site_name
                sheet['B'+str(number_cell)] = val["name"]
                sheet['C'+str(number_cell)] = environment_prefix+"_veig1_thing§_"+str(val["id"])
                sheet['E'+str(number_cell)] = val["period"]/60 
                number_cell+=1               
    excel_document.save(excelPath+JaSONx.name_file_hierarchy[:JaSONx.name_file_hierarchy.find(".")]+".xlsx")
    
def start(folder_json):  
    createExcelSheet(search_json(jsonPath+folder_json, create_dict_xml(JaSONx.name_file_hierarchy)))
    
    
def getListFolderJSON():
    return(utility.createListDirectory(jsonPath))
