'''
JaSONx GUI Version
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "3.1.2.0"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

import utility
import os
import shutil

'''Configuration path'''
dict_configuration_path = utility.getConfigurationPath()
json_templates_path = dict_configuration_path["json_templates_path"]
excel_templates_path = dict_configuration_path["excel_templates_path"]
json_files_path = dict_configuration_path["json_files_path"]
excel_files_path = dict_configuration_path["excel_files_path"]
hierarchy_path = dict_configuration_path["hierarchy_path"]

'''Path for json file generated'''
def change_json_path(path):
    if(os.path.exists(os.path.join(path,"json_files")) == False):
        os.mkdir(os.path.join(path,"json_files"))
    dict_configuration_path["json_files_path"] = os.path.join(path, "json_files")
    utility.saveJsonFile(os.path.join(os.path.realpath(''), "configuration", "pathConfiguration.json"), dict_configuration_path) 
    return True
    
  
'''Path for hierarchy file'''
def change_hierarchy_path(path):
    if(os.path.exists(os.path.join(path,"hierarchy")) == False):
        os.mkdir(os.path.join(path,"hierarchy"))
    dict_configuration_path["hierarchy_path"] = os.path.join(path, "hierarchy")
    utility.saveJsonFile(os.path.join(os.path.realpath(''), "configuration", "pathConfiguration.json"), dict_configuration_path)
    return True

'''Path for template file'''
def change_template_path(path):
    if(os.path.exists(os.path.join(path,"json_templates")) == False):
        os.mkdir(os.path.join(path,"json_templates"))
    dict_configuration_path["json_templates_path"] = os.path.join(path, "json_templates")
    utility.saveJsonFile(os.path.join(os.path.realpath(''), "configuration", "pathConfiguration.json"), dict_configuration_path)
    return True
  
    
'''Path for excel file generated'''   
def change_excel_path(path):
    if(os.path.exists(os.path.join(path,"excel_files")) == False):
        os.mkdir(os.path.join(path,"excel_files"))
    dict_configuration_path["excel_files_path"] = os.path.join(path, "excel_files")
    utility.saveJsonFile(os.path.join(os.path.realpath(''), "configuration", "pathConfiguration.json"), dict_configuration_path)
    return True
    
'''Reset default path'''
def reset_path(): 
    path = os.path.realpath('')
    if(os.path.exists(os.path.join(path,"json_files")) == False):
        os.mkdir(os.path.join(path,"json_files"))  
        
    if(os.path.exists(os.path.join(path,"hierarchy")) == False):
        os.mkdir(os.path.join(path,"hierarchy"))        
        
    if(os.path.exists(os.path.join(path,"excel_files")) == False):
        os.mkdir(os.path.join(path,"excel_files"))
        
    dict_configuration_path["json_files_path"] = os.path.join(path, "json_files")
    dict_configuration_path["hierarchy_path"] = os.path.join(path, "hierarchy")
    dict_configuration_path["excel_files_path"] = os.path.join(path, "excel_files")      
    utility.saveJsonFile(os.path.join(path, "configuration", "pathConfiguration.json"), dict_configuration_path)

'''Control paths exists'''
def control_paths():
    path = os.path.realpath ('')
    if(os.path.exists(json_files_path) == False):
        if(os.path.exists(os.path.join(path,"json_files")) == False):
            os.mkdir(os.path.join(path,"json_files"))
            dict_configuration_path["json_files_path"] = os.path.join(path, "json_files_path")
        else:
            dict_configuration_path["json_files_path"] = os.path.join(path, "json_files_path")
        utility.saveJsonFile(os.path.join(path, "configuration", "pathConfiguration.json"), dict_configuration_path)  
    
    if(os.path.exists(hierarchy_path) == False):
        if(os.path.exists(os.path.join(path,"hierarchy")) == False):
            os.mkdir(os.path.join(path,"hierarchy"))
            dict_configuration_path["hierarchy_path"] = os.path.join(path, "hierarchy_path")
        else:
            dict_configuration_path["hierarchy_path"] = os.path.join(path, "hierarchy_path")      
        utility.saveJsonFile(os.path.join(path, "configuration", "pathConfiguration.json"), dict_configuration_path) 
        
    if(os.path.exists(excel_files_path) == False):
        if(os.path.exists(os.path.join(path,"excel_files")) == False):
            os.mkdir(os.path.join(path,"excel_files"))
            dict_configuration_path["excel_files_path"] = os.path.join(path, "excel_files_path")
        else:
            dict_configuration_path["excel_files_path"] = os.path.join(path, "excel_files_path")
        utility.saveJsonFile(os.path.join(path, "configuration", "pathConfiguration.json"), dict_configuration_path)       

'''Add new json template'''    
def addJsonTemplate(path):
    file_path = os.path.basename(path)  
    if(os.path.isfile(path) and utility.getSubstring(file_path, start=".") == "json"):
        path_name, file_name = os.path.splitext(file_path)
        shutil.copy(path, os.path.join(json_templates_path))
        utility.refreshTemplateConfiguration()
        return True
    elif(os.path.isdir(path)):
        list_files = utility.createFileList(path, ".json")
        for file in list_files:
            shutil.copy(os.path.join(path, file), os.path.join(json_templates_path))
        utility.add_measures_template(list_files)
        return True
    else: 
        return False
    
'''Add new hierarchy file'''
def add_file_hierarchy(path):  
    file_path = os.path.basename(path)   
    if(os.path.isfile(path) and utility.getSubstring(file_path, start=".") == "xml"):
        shutil.copy(path, hierarchy_path)  
        return True
    elif(os.path.isdir(path)):
        list_files = utility.createFileList(path, ".xml")
        for file in list_files:
            shutil.copy(os.path.join(path, file), hierarchy_path)
        return True
    else:	
        return False
    
'''Add environment prefix'''
def add_environment_prefix(string):
    path = os.path.join(os.path.realpath (''), "configuration", "environmentPrefixConfiguration.json")
    list_environment_prefix = utility.readJsonFile(path)
    if(string not in list_environment_prefix and string != ''):
        list_environment_prefix.append(string)
        utility.saveJsonFile(path, list_environment_prefix)  
        return True
    else:
        return False
    
'''Add gateway id'''    
def add_gateway_id(string):
    path = os.path.join(os.path.realpath (''), "configuration", "gatewayIdConfiguration.json")
    list_gateway_id = utility.readJsonFile(path)
    if(string not in list_gateway_id and string != ''):
        list_gateway_id.append(string)
        utility.saveJsonFile(path, list_gateway_id)  
        return True
    else:
        return False

'''Add trend id'''    
def add_trend_id(trend_id, channel, multipler):
    path = os.path.join(os.path.realpath (''), "configuration", "trendIdConfiguration.json")
    dict_trend_id = utility.readJsonFile(path)
    if(trend_id not in dict_trend_id and trend_id != ''):
        dict_trend_id[trend_id] = {"channel" : channel, "multipler" : multipler, "active" : False}
        utility.saveJsonFile(path, dict_trend_id)  
        return True
    else:
        return False