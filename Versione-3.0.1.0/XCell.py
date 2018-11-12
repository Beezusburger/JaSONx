'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.0.1.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

import os
import utility
import openpyxl 

class XCell():
    def __init__(self, site_name, hierarchy_name, environment_prefix, dict_meters):
        '''Set path'''
        dict_configuration_path = utility.getConfigurationPath()
        self.json_templates_path = dict_configuration_path["json_templates_path"]
        self.excel_templates_path = dict_configuration_path["excel_templates_path"]
        self.json_files_path = dict_configuration_path["json_files_path"]
        self.excel_files_path = dict_configuration_path["excel_files_path"]
        self.hierarchy_file_path = dict_configuration_path["hierarchy_path"]

        '''Set Data'''
        self.site_name = site_name
        self.hierarchy_name = hierarchy_name
        self.environment_prefix = environment_prefix

        '''Dict'''
        self.dict_from_template = self.getTemplateData(hierarchy_name)
        self.dict_from_json_configuration = utility.readJsonFile(os.path.join(os.path.realpath(''), "configuration", "trandIdConfiguration.json"))
        self.dict_meters = self.createDictMeterData(dict_meters)
        self.createExcelSheet()

    def createDictMeterData(self, dict_meters):    
        for meter_name, list_measures in dict_meters.items():
            for dict_measure in list_measures:
                try:
                    trend_id, period = self.dict_from_template[meter_name+"."+dict_measure["measure"]]
                    dict_measure["trend_id"] = trend_id
                    dict_measure["period"] = period
                    if(str(trend_id) in self.dict_from_json_configuration):
                        dict_measure.update(self.dict_from_json_configuration[str(trend_id)])
                except:
                    pass
        return dict_meters

    def getTemplateData(self, hierarchy_name):
        list_json_file = utility.createFileList(os.path.join(self.json_files_path, hierarchy_name), ".json")
        dict_measures = {}
        for file in list_json_file:
            file_json = utility.readJsonFile(os.path.join(self.json_files_path, hierarchy_name, file))           
            for measure in file_json["parameters"]["filter_tag"]:
                if(measure["tag"] != "CommunicationCode"):
                    dict_measures[measure["tag"]] = [measure["id"], measure["period"]]       
        return(dict_measures)

    '''Create excel file'''    
    def createExcelSheet(self):
        excel_document = openpyxl.load_workbook(os.path.join(self.excel_templates_path, "Meter Upload Template LEONARDO.xlsx"))
        sheet = excel_document.active
        number_cell = 7  
        for meter_name, list_measures in self.dict_meters.items():
            for dict_measure in list_measures:
                try:
                    if(dict_measure["active"] == "True" or dict_measure["active"] == "true"):
                        sheet['A'+str(number_cell)] = self.site_name
                        sheet['B'+str(number_cell)] = utility.getSubstring(dict_measure["name"], stop=".")
                        sheet['C'+str(number_cell)] = self.environment_prefix+"_veig1_thing§_"+str(dict_measure["trend_id"])
                        sheet['E'+str(number_cell)] = dict_measure["period"]/60 
                        sheet['G'+str(number_cell)] = "True"
                        sheet['D'+str(number_cell)] = dict_measure["channel"]
                        sheet['F'+str(number_cell)] = dict_measure["multipler"]
                        number_cell+=1 
                except:
                    pass
        excel_document.save(os.path.join(self.excel_files_path,self.hierarchy_name+".xlsx"))