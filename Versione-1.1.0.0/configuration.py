'''
@author = "Jury Francia, Simone Olivieri, Vic Zagranowski"
@version = "1.1"
@email = "j.francia@reply.it, s.olivieri@reply.it, v.zagranowski@reply.it"
'''

import utility
import os
import shutil
import JaSONx


'''Configuration'''
paths = utility.readFileJSON(os.path.realpath (''), "\\configuration\\pathConfiguration.json")
templatesPath = paths["templatesPath"]
jsonPath = paths["jsonPath"]
hierarchyPath = paths["hierarchyPath"]
templatesExcelPath = paths["templatesExcelPath"]
excelPath = paths["excelPath"]

'''Path for json file generated'''
def change_json_path(path):
    if(os.path.exists(path+"\\json_files") == False):
        os.mkdir(path+"\\json_files")
        paths["jsonPath"] = path + "\\json_files"
        utility.saveFileJSON(os.path.realpath (''), "\\configuration\\pathConfiguration.json", paths)
    
  
'''Path for hierarchy file'''
def change_hierarchy_path(path):
    if(os.path.exists(path+"\\hierarchy") == False):
        os.mkdir(path+"\\hierarchy")
        paths["hierarchyPath"] = path + "\\hierarchy"
        utility.saveFileJSON(os.path.realpath (''), "\\configuration\\pathConfiguration.json", paths)
        
'''Path for excel file generated'''   
def change_excel_path(path):
    if(os.path.exists(path+"\\excel_files") == False):
        os.mkdir(path+"\\excel_files")
        paths["excelPath"] = path + "\\excel_files"
        utility.saveFileJSON(os.path.realpath (''), "\\configuration\\pathConfiguration.json", paths)
        
'''Reset default path'''
def reset_path():   
    path = os.path.realpath ('')
    if(os.path.exists(path+"\\json_files") == False):
        os.mkdir(path+"\\json_files")  
        
    if(os.path.exists(path+"\\hierarchy") == False):
        os.mkdir(path+"\\hierarchy")        
        
    if(os.path.exists(path+"\\excel_files") == False):
        os.mkdir(path+"\\excel_files")
        
    paths["jsonPath"] = path+ "\\json_files\\"
    paths["hierarchyPath"] = path+ "\\hierarchy\\"
    paths["excelPath"] = path+ "\\excel_files\\"      
    utility.saveFileJSON(path, "\\configuration\\pathConfiguration.json", paths)

'''Control paths exists'''
def control_paths():
    path = os.path.realpath ('')
    if(os.path.exists(jsonPath) == False):
        if(os.path.exists(path+"\\json_files") == False):
            os.mkdir(path+"\\json_files")
            paths["jsonPath"] = path+ "\\json_files\\"
        else:
            paths["jsonPath"] = path+ "\\json_files\\"
        utility.saveFileJSON(path, "\\configuration\\pathConfiguration.json", paths)  
    
    if(os.path.exists(hierarchyPath) == False):
        if(os.path.exists(path+"\\hierarchy") == False):
            os.mkdir(path+"\\hierarchy")
            paths["hierarchyPath"] = path+ "\\hierarchy\\"
        else:
            paths["hierarchyPath"] = path+ "\\hierarchy\\"      
        utility.saveFileJSON(path, "\\configuration\\pathConfiguration.json", paths) 
        
    if(os.path.exists(excelPath) == False):
        if(os.path.exists(path+"\\excel_files") == False):
            os.mkdir(path+"\\excel_files")
            paths["excelPath"] = path+ "\\excel_files\\"
        else:
            paths["excelPath"] = path+ "\\excel_files\\"
        utility.saveFileJSON(path, "\\configuration\\pathConfiguration.json", paths)       
        
'''Count measures in file json template'''
def count_measures_template(file_name):
    list_measures = JaSONx.createListModel(file_name)
    diz_templates = utility.readFileJSON(os.path.realpath (''), "\\configuration\\meterMeasuresConfiguration.json")
    if(file_name not in diz_templates):
        diz_templates[file_name] = {"measuressMax":len(list_measures), "measuresSelected":len(list_measures)}
    utility.saveFileJSON(os.path.realpath ('')+"\\configuration\\", "meterMeasuresConfiguration.json", diz_templates) 

'''Add new json template'''    
def add_json_template(path):
    path_name, file_name = os.path.split(path)
    shutil.copy(path, templatesPath)
    count_measures_template(file_name.split(".")[0])


'''Add new hierarchy file'''
def add_file_hierarchy(path):    
    shutil.copy(path, hierarchyPath)   
    