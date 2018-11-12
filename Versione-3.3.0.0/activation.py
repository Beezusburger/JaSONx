import boto3
from requests_aws4auth import AWS4Auth
import requests
import JaSONx 
import os
import time
from utility import binary_to_dict, createFileList
from PyQt5 import QtCore
import httpReq
import os
import sys, os, base64, datetime, hashlib, hmac 

dict_credentials = {}
dict_response = {}
r = ''
def readCredentials(account):
    pathcredentials = QtCore.QDir.homePath() + '/.aws/credentials'
    with open( pathcredentials , 'r') as fin:
        credentials = fin.read()
    list_credentials = credentials.split("[")
    for lis in list_credentials:
        if( account in lis):
            for attr in lis.split("\n"):
                if("region" in attr or "aws_access_key_id" in attr or "aws_secret_access_key" in attr or "aws_session_token" in attr or "aws_security_token" in attr):
                        key, val =attr.split(" = ")
                        dict_credentials[key] = val                    
    return dict_credentials

def readfilejson(path):   
        with open(path, 'r') as json_file: 
            return json_file.read()

def activateThing(hierarchy_name, file, dict_credentials, api_id):

    payload = readfilejson(os.path.join(os.path.realpath(''),'json_files', hierarchy_name, file))
    endpoint = 'https://' + api_id + '.execute-api.eu-central-1.amazonaws.com/dev/v1/gateways/conad-eig1/command'
    post_response = httpReq.post(dict_credentials, endpoint, payload)

    if(post_response[0] == 200):
        endpoint = 'https://' + api_id + '.execute-api.eu-central-1.amazonaws.com/dev/v1/gatewayCommands/'
        response = httpReq.get(dict_credentials,
            endpoint, 
            binary_to_dict(post_response[1])["command_id"]
            )
        return response
    else:
        status = post_response[0]
        message = binary_to_dict(post_response[1])["errors"][0]["error_message"]
        response = (status,message)
        return response

#Initialize the activations getting the credentials with readCredentials() and posting all the payloads in list_json_file with activateThing()
def initializeActivations(hierarchy_name, list_json_file, account, api_id):
    
    #Populate dict_credentials with STS from .\.aws\credentials for the account selected
    dict_credentials = readCredentials(account)  

    #Initialize response dictionary
    dict_response = {}    
    if(list_json_file != []):
        for file in list_json_file:
            response = activateThing(hierarchy_name, file, dict_credentials, api_id)
            dict_response[file] = "STATUS:" + str(response[0]) + ";" + "MESSAGE:" + response[1]
    print(dict_response)
    return dict_response