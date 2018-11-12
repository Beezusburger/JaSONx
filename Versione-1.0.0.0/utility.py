'''
@author = "Jury Francia, Simone Olivieri"
@version = "1.0"
@email = "j.francia@reply.it, s.olivieri@reply.it"
'''

import json
from xml.dom import minidom
import os

'''funzione per aprire file json'''
def readFileJSON(path, nomeFile):
    with open(path+nomeFile, 'r') as file:
        return json.load(file)
    
'''funzione per salvare file json'''
def saveFileJSON(path, nomeFile, element):
    with open(path+nomeFile, 'w') as file:
        json.dump(element, file, indent=4)
        
'''funzione per aprire file'''
def readFileXML(path, nomeFile):
    return minidom.parse(path+nomeFile)

'''Funzione che prende in input un percorso e restituisce una lista contente tutti i file presenti all'interno della cartella'''
def createListFile(path):
    lista = []
    for nodo in os.listdir(path):
        if(nodo.startswith(".")):
            continue
        fullpath = os.path.join(path, nodo)
        if(os.path.isfile(fullpath)): 
            lista.append(nodo)
    return lista
            
'''
def creaDizionarioMeterMisure(dizionarioMeter):
    count=0
    serial_number = ""
    for val in topologica.getElementsByTagName("Meter"):
        for localId in val.getElementsByTagName("LocalId"):
            if(localId.toxml().strip("</LocalId>").split(".")[0] not in dizionarioMeter):
                dizionarioMeter[localId.toxml().strip("</LocalId>").split(".")[0]] = [localId.toxml().strip("</LocalId>")]
            else:
                dizionarioMeter[localId.toxml().strip("</LocalId>").split(".")[0]] += [localId.toxml().strip("</LocalId>")]  
        if(count==0):
            for description in val.getElementsByTagName("Description"):
                serial_number = description.toxml().split("\n")[0].split("=")[1]
                count+=1

    return(dizionarioMeter, serial_number)
dizionarioMeter, serial_number = ricercaMeter({})
'''


'''
 listMeters = []
    for value in topologica.getElementsByTagName("Meter"):
        for localId in value.getElementsByTagName("LocalId"):
            if(localId.toxml().strip("</LocalId>").split(".")[0] not in listMeters):
                listMeters.append(localId.toxml().strip("</LocalId>").split(".")[0])
            else:
                pass
        if(count==0):
            for description in value.getElementsByTagName("Description"):
                serial_number = description.toxml().split("\n")[0].split("=")[1]
                count+=1
'''