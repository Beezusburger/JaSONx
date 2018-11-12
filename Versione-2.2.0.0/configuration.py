'''
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "2.1"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

import utility
import os
import shutil

'''Configuration'''
paths = utility.readFileJSON(os.path.join(os.path.realpath (''), "configuration\\pathConfiguration.json"))
templatesPath = paths["templatesPath"]
jsonPath = paths["jsonPath"]
hierarchyPath = paths["hierarchyPath"]
templatesExcelPath = paths["templatesExcelPath"]
excelPath = paths["excelPath"]

'''Path for json file generated'''
def change_json_path(path):
    if(os.path.exists(os.path.join(path,"json_files")) == False):
        os.mkdir(os.path.join(path,"json_files"))
        paths["jsonPath"] = os.path.join(path, "json_files")
        utility.saveFileJSON(os.path.join(os.path.realpath(''), "configuration\\pathConfiguration.json"), paths) 
        return True
    else: 
        return False
  
'''Path for hierarchy file'''
def change_hierarchy_path(path):
    if(os.path.exists(os.path.join(path,"hierarchy")) == False):
        os.mkdir(os.path.join(path,"hierarchy"))
        paths["hierarchyPath"] = os.path.join(path, "hierarchy")
        utility.saveFileJSON(os.path.join(os.path.realpath(''), "configuration\\pathConfiguration.json"), paths)
        return True
    else:
        return False
    
'''Path for excel file generated'''   
def change_excel_path(path):
    if(os.path.exists(os.path.join(path,"excel_files")) == False):
        os.mkdir(os.path.join(path,"excel_files"))
        paths["excelPath"] = os.path.join(path, "excel_files")
        utility.saveFileJSON(os.path.join(os.path.realpath(''), "configuration\\pathConfiguration.json"), paths)
        return True
    else:
        return False
    
'''Reset default path'''
def reset_path(): 
    path = os.path.realpath('')
    if(os.path.exists(os.path.join(path,"json_files")) == False):
        os.mkdir(os.path.join(path,"json_files"))  
        
    if(os.path.exists(os.path.join(path,"hierarchy")) == False):
        os.mkdir(os.path.join(path,"hierarchy"))        
        
    if(os.path.exists(os.path.join(path,"excel_files")) == False):
        os.mkdir(os.path.join(path,"excel_files"))
        
    paths["jsonPath"] = os.path.join(path, "json_files")
    paths["hierarchyPath"] = os.path.join(path, "hierarchy")
    paths["excelPath"] = os.path.join(path, "excel_files")      
    utility.saveFileJSON(os.path.join(path, "configuration\\pathConfiguration.json"), paths)

'''Control paths exists'''
def control_paths():
    path = os.path.realpath ('')
    if(os.path.exists(jsonPath) == False):
        if(os.path.exists(os.path.join(path,"json_files")) == False):
            os.mkdir(os.path.join(path,"json_files"))
            paths["jsonPath"] = os.path.join(path, "json_files")
        else:
            paths["jsonPath"] = os.path.join(path, "json_files")
        utility.saveFileJSON(os.path.join(path, "configuration\\pathConfiguration.json"), paths)  
    
    if(os.path.exists(hierarchyPath) == False):
        if(os.path.exists(os.path.join(path,"hierarchy")) == False):
            os.mkdir(os.path.join(path,"hierarchy"))
            paths["hierarchyPath"] = os.path.join(path, "hierarchy")
        else:
            paths["hierarchyPath"] = os.path.join(path, "hierarchy")      
        utility.saveFileJSON(os.path.join(path, "configuration\\pathConfiguration.json"), paths) 
        
    if(os.path.exists(excelPath) == False):
        if(os.path.exists(os.path.join(path,"excel_files")) == False):
            os.mkdir(os.path.join(path,"excel_files"))
            paths["excelPath"] = os.path.join(path, "excel_files")
        else:
            paths["excelPath"] = os.path.join(path, "excel_files")
        utility.saveFileJSON(os.path.join(path, "configuration\\pathConfiguration.json"), paths)       
        

'''Add new json template'''    
def add_json_template(path):
    file_path = os.path.basename(path)   
    if(os.path.isfile(path) and utility.getSubstring(path, start=".") == "json"):
        path_name, file_name = os.path.splitext(file_path)
        shutil.copy(path, templatesPath)
        utility.add_measures_template(file_path)
        return True
    elif(os.path.isdir(path)):
        list_files = utility.createListFile(path, ".json")
        for file in list_files:
            shutil.copy(os.path.join(path, file), templatesPath)
        utility.add_measures_template(list_files)
        return True
    else: 
        return False
    
    
'''Add new hierarchy file'''
def add_file_hierarchy(path):         
    if(os.path.isfile(path) and utility.getSubstring(path, start=".") == "xml"):
        shutil.copy(path, hierarchyPath)  
        return True
    elif(os.path.isdir(path)):
        list_files = utility.createListFile(path, ".xml")
        for file in list_files:
            shutil.copy(os.path.join(path, file), hierarchyPath)
        return True
    else:
        return False
    
'''Add environment prefix'''    
def add_environment_prefix(string):
    path = os.path.join(os.path.realpath (''), "configuration\\environmentPrefixConfiguration.json")
    list_environment_prefix = utility.readFileJSON(path)
    if(string not in list_environment_prefix and string != ''):
        list_environment_prefix.append(string)
        utility.saveFileJSON(path, list_environment_prefix)  
        return True
    else:
        return False
    
'''Add gateway id'''    
def add_gateway_id(string):
    path = os.path.join(os.path.realpath (''), "configuration\\gatewayIdConfiguration.json")
    list_gateway_id = utility.readFileJSON(path)
    if(string not in list_gateway_id and string != ''):
        list_gateway_id.append(string)
        utility.saveFileJSON(path, list_gateway_id)  
        return True
    else:
        return False
