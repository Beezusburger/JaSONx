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
site_name = ""
number_thing = ""

'''SETTING CONSTANT DATA'''
'''Richiamata da bottone "send data"'''
def setConstantData(site, number):  
    global site_name, number_thing
    site_name = site
    number_thing = number
    
'''CREATE DIZ METERS'''
'''Crea un dizionario come segue -> {"nomeMeter":}'''
def search_json(path):
    global environment_prefix
    file_list = utility.createListFile(path)
    diz_meters={}
    for file in file_list:
        file_json = utility.readFileJSON(path+"\\",file)
        meter_name = file_json["parameters"]["meter_name"]
        for key in file_json["parameters"]["filter_tag"]:
            environment_prefix = file_json["parameters"]["environment_prefix"]
            if(key["tag"]!="CommunicationCode"):
                if(meter_name not in diz_meters):
                    diz_meters[meter_name] = []
                else:
                    diz_meters[meter_name] += [{key["tag"] [key["tag"].find(".")+1:] : {"id":key["id"], "period":key["period"]}}]
    return(diz_meters)   


def search_hierarchy(path, name_file):
    file_hierarchy = utility.readFileXML(path+"\\", name_file)
    diz_meters_hierarchy = {}
    for val in file_hierarchy.getElementsByTagName("Meter"):
        for localId in val.getElementsByTagName("LocalId"):   
            print(val.toxml()[val.toxml().find("<Factor>")+8 : val.toxml().find("</Factor>")])
            if(localId.toxml()[localId.toxml().find(">")+1:localId.toxml().find(".")] not in diz_meters_hierarchy):
                diz_meters_hierarchy[localId.toxml()[localId.toxml().find(">")+1:localId.toxml().find(".")]] = [{localId.toxml()[localId.toxml().find(".")+1:localId.toxml().find("</LocalId>")]}]
            else:
                diz_meters_hierarchy[localId.toxml()[localId.toxml().find(">")+1:localId.toxml().find(".")]] += [{localId.toxml()[localId.toxml().find(".")+1:localId.toxml().find("</LocalId>")]}]
        break
        #for factor in val.getElementsByTagName("Factor"):
           # print(factor.toxml())
        
    



#def start(folder):
    '''
    diz_meters_json = search_json(jsonPath+folder)
    
    for meter in diz_meters_json:
        for list_measures in diz_meters_json[meter]:
            for measure in list_measures:
                print(meter+"."+measure)
                #(hierarchyPath, folder+".xml")
                
                
            #print(list_measures,"\n")
        break
     
    
    #diz_meters_hierarchy = search_hierarchy(hierarchyPath, folder+".xml")
'''
    
    
def getListFolderJSON():
    return(utility.createListFile(jsonPath))

if __name__ == '__main__':
    start("Hierarchy_ComX510_FOG_Q02_GW02_00055016379168_20181005141203")
    search_hierarchy(hierarchyPath, "Hierarchy_ComX510_FOG_Q02_GW02_00055016379168_20181005141203.xml")