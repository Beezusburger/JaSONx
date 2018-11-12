'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.1.2.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''
from xml.dom import minidom
import os
import utility
import configuration

utility.refreshTemplateConfiguration()
configuration.control_paths()

class Jasonx():
    def __init__(self, username, password, hierarchy, gateway_id, environment_prefix):
        '''Configuration path'''
        dict_configuration_path = utility.getConfigurationPath()
        self.json_templates_path = dict_configuration_path["json_templates_path"]
        self.excel_templates_path = dict_configuration_path["excel_templates_path"]
        self.json_files_path = dict_configuration_path["json_files_path"]
        self.excel_files_path = dict_configuration_path["excel_files_path"]
        self.hierarchy_file_path = dict_configuration_path["hierarchy_path"]

        '''Data'''
        self.dict_configuration_path = utility.getConfigurationPath
        self.username = username
        self.password = password
        self.name_hierarchy = utility.getSubstring(os.path.basename(hierarchy), stop=".")
        self.hierarchy_path = os.path.join(self.hierarchy_file_path, self.name_hierarchy+".xml")
        self.serial_number, self.match_group_value, self.dict_meters = self.getDataFromHierarchy()
        self.gateway_id = gateway_id
        self.environment_prefix = environment_prefix
        self.match_group_value = self.name_hierarchy.split("_")[1]+"_"+self.match_group_value
        self.dict_meter_template = self.createDictMeterTemplate()

    '''Search serial_number, match_group_value and create dict_meter -> {"meter_name" : [{"name_measure" : "val", "tag_measure : "val"} , {...}, ...]'''
    def getDataFromHierarchy(self):
        file_hierarchy = minidom.parse(self.hierarchy_path) 
        dict_meters = {}    
        local_id = file_hierarchy.getElementsByTagName("LocalId")   
        name = file_hierarchy.getElementsByTagName("Name")  
        description = file_hierarchy.getElementsByTagName("Description")[0].firstChild.nodeValue
        serial_number = description[description.find("SerialNumber=")+13:description.find("\n")]
        match_group_value = name[0].firstChild.nodeValue
        if(len(match_group_value) > 15):
            match_group_value = match_group_value[0:15]
        for i in range(0, len(local_id)): 
            if(local_id[i].parentNode.nodeName == "Meter"):
                meter_name, measure = local_id[i].firstChild.nodeValue.split(".")   
                measure_eff = name[i].firstChild.nodeValue  
                if(meter_name not in dict_meters):
                    dict_meters[meter_name] = [{"measure" : measure, "name" : measure_eff}] 
                else:
                    dict_meters[meter_name].append({"measure" : measure, "name" : measure_eff})
        return serial_number, match_group_value, dict_meters

    '''Create dict -> {meter_name : template_name / not found, ...}'''
    def createDictMeterTemplate(self):
        dict_meters_template = {}
        for meter_name, list_measures in self.dict_meters.items():
            list_meter_measures = []
            for measure in list_measures:
                list_meter_measures.append(measure["measure"])
            response = self.searchTemplate(list_meter_measures) 
            if(response != False):
                dict_meters_template[meter_name] = response
            else:
                dict_meters_template[meter_name] = "Not Found"
        return dict_meters_template

    '''Match number measures-> template - meter'''
    def searchTemplate(self, list_meter_measures):
        dict_meters_config = utility.readJsonFile(os.path.join(os.path.realpath (''), "configuration", "meterMeasuresConfiguration.json"))
        list_model = []
        for model_meter, diz_value in dict_meters_config.items():
            for key, value in diz_value.items():
                if(key == "measuresSelected" and value==len(list_meter_measures)):
                    response = self.controlTemplate(model_meter+".json", list_meter_measures)               
                    if(response != False):
                        return response
        return False

    '''Match tag measures -> template - meter'''
    def controlTemplate(self, template, list_meter_measures):
        count = 0
        list_measures_template = self.createTemplateList(template)
        for measure in list_meter_measures:
            if(measure not in list_measures_template):
                break
            else:
                if(count+1 == len(list_meter_measures)):
                    return template
                else:
                    count+=1   
        return False        

    '''Create list tag measures template'''
    def createTemplateList(self, template):
        file_template = utility.readJsonFile(os.path.join(self.json_templates_path, template))
        list_measures = []
        for model in file_template["parameters"]["filter_tag"]:
            if(model["tag"] != "CommunicationCode"):
                list_measures.append(utility.getSubstring(model["tag"], start="."))           
        return(list_measures)
                
    '''Create file json'''
    def createJson(self): 
        if(self.name_hierarchy not in os.listdir(os.path.join(self.json_files_path))):
            os.mkdir(os.path.join(self.json_files_path, self.name_hierarchy))
        for meter_name, template in self.dict_meter_template.items():
            if(template != "Not Found"):
                file = utility.readJsonFile(os.path.join(self.json_templates_path, template))
                file["gateway_id"] = self.gateway_id
                file["parameters"]["environment_prefix"] = self.environment_prefix
                file["parameters"]["serial_number"] = self.serial_number
                file["parameters"]["model"] = template[:template.find(".")]
                file["parameters"]["user_name"] = self.username
                file["parameters"]["password"] = self.password
                key = file["parameters"]["file_name_filter"]
                key["match_group_value"] = self.match_group_value
                file["parameters"]["meter_name"] = meter_name
                file["parameters"]["maker"] = meter_name
                for measure_meter in file["parameters"]["filter_tag"]:
                    if(measure_meter["tag"]!="CommunicationCode"):
                        measure_meter["tag"] = measure_meter["tag"].replace(measure_meter["tag"][:measure_meter["tag"].find(".")], meter_name)                
                utility.saveJsonFile(os.path.join(self.json_files_path, self.name_hierarchy, meter_name+".json"), file) 