import boto3
from requests_aws4auth import AWS4Auth
import requests
import JaSONx
import os
import time
from utility import getSubstring, binary_to_dict
from PyQt5 import QtCore
import os
import sys, os, base64, datetime, hashlib, hmac

import activation

### FUNCTIONs FOR SIGNATURE
def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

def getSignatureKey(key, date_stamp, region, service):
    kDate = sign(('AWS4' + key).encode('utf-8'), date_stamp)
    kRegion = sign(kDate, region)
    kService = sign(kRegion, service)
    kSigning = sign(kService, 'aws4_request')
    return kSigning

### INPUT: credentials (dict), endpoint(str), payload(json)
### RETURN request response (tuple)
def post(credentials, endpoint, payload):

    #VARIABLE DECLARATION
    service = 'execute-api'
    method = 'POST'
    host = getSubstring(endpoint, start = "'https://", stop = '/dev/')
    uri = getSubstring(endpoint, start = host, stop = '')
    content_type = 'application/json'

    ##CREDENTIALS
    dict_credentials = credentials
    region = dict_credentials['region']
    securitytoken = dict_credentials['aws_security_token']

    ###ACCESS AND SECRET CONTROL
    secretkey = dict_credentials['aws_secret_access_key']
    accesskey = dict_credentials['aws_access_key_id']
    if accesskey is None or secretkey is None:
        print('No access key is available.')
        sys.exit()
    
    t = datetime.datetime.utcnow()
    amz_date = t.strftime('%Y%m%dT%H%M%SZ')
    date_stamp = t.strftime('%Y%m%d')

    ### CREATE A CANONICAL REQUEST
    canonical_uri = uri
    canonical_querystring = ''
    canonical_headers = 'content-type:' + content_type + '\n' + 'host:' + host + '\n' + 'x-amz-date:' + amz_date + '\n'
    signed_headers = 'content-type;host;x-amz-date'
    payload_hash = hashlib.sha256(payload.encode('utf-8')).hexdigest()

    canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

    ### CREATE THE STRING TO SIGN
    algorithm = 'AWS4-HMAC-SHA256'
    credential_scope = date_stamp + '/' + region + '/' + service + '/' + 'aws4_request'

    string_to_sign = algorithm + '\n' +  amz_date + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()

    ### CALCULATE THE SIGNATURE
    signing_key = getSignatureKey(secretkey, date_stamp, region, service)

    signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

    ### ADD SIGNING INFORMATION TO THE REQUEST
    authorization_header = algorithm + ' ' + 'Credential=' + accesskey + '/' + credential_scope + ', ' +  'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

    headers = {'Content-Type':content_type,
            'x-amz-date':amz_date,
            'x-amz-security-token': securitytoken,
            'Authorization':authorization_header}
    
    # RESPONSE OF THE REQUEST
    r = requests.post(endpoint, data=payload, headers=headers)
    post_response = (r.status_code, r._content)

    return post_response



### INPUT: credentials(dict), endpoint(str), commandId(str)
### RETURN: 
def get(credentials, endpoint, commandId):

    # VARIABLES DECLARATION
    service = 'execute-api'
    method = 'GET'
    endpoint_g = endpoint + commandId
    host = getSubstring(endpoint, start = "'https://", stop = '/dev/')
    uri = getSubstring(endpoint, start = host, stop = "") + commandId
    content_type = 'application/json'
    request_parameters = '' 

    ## CREDENTIALS
    dict_credentials = credentials
    region = dict_credentials['region']
    securitytoken = dict_credentials['aws_security_token']

    ###ACCESS AND SECRET CONTROL
    secretkey = dict_credentials['aws_secret_access_key']
    accesskey = dict_credentials['aws_access_key_id']
    if accesskey is None or secretkey is None:
        print('No access key is available.')
        sys.exit()

    t = datetime.datetime.utcnow()
    amzdate = t.strftime('%Y%m%dT%H%M%SZ')
    datestamp = t.strftime('%Y%m%d')

    ### CREATE A CANONICAL REQUEST
    canonical_uri = uri
    canonical_querystring = request_parameters
    canonical_headers = 'content-type:' + content_type + '\n' + 'host:' + host + '\n' + 'x-amz-date:' + amzdate + '\n'
    signed_headers = 'content-type;host;x-amz-date'
    payload_hash = hashlib.sha256(('').encode('utf-8')).hexdigest()

    canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

    ### CREATE THE STRING TO SIGN
    algorithm = 'AWS4-HMAC-SHA256'
    credential_scope = datestamp + '/' + region + '/' + service + '/' + 'aws4_request'

    string_to_sign = algorithm + '\n' +  amzdate + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()

    ### CALCULATE THE SIGNATURE
    signing_key = getSignatureKey(secretkey, datestamp, region, service)

    signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()

    ### ADD SIGNING INFORMATION TO THE REQUEST
    authorization_header = algorithm + ' ' + 'Credential=' + accesskey + '/' + credential_scope + ', ' +  'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

    headers = {'Content-Type': content_type,
        'host':host,
        'x-amz-security-token':securitytoken, 
        'x-amz-date':amzdate,
        'Authorization':authorization_header
        }

    request_url = endpoint_g + canonical_querystring

    # RESPONSE OF THE REQUEST
    response_g = requests.get(request_url, headers=headers)

    ## RESPONSE CONTROLS
    if(response_g.status_code == 404):
        return get(credentials, endpoint, commandId) 
    elif(response_g.status_code == 200):
        commandstat = binary_to_dict(response_g._content)["command_status"]
        commandProcessDet = binary_to_dict(response_g._content)["command_process_details"]
        rejected = commandProcessDet['rejected']
        failed = commandProcessDet['failed']
        succeed = commandProcessDet['succeed']
        inprogress = commandProcessDet['in_progress']
        removed = commandProcessDet['removed']
        queued = commandProcessDet['queued']

        if(rejected == '1'):
            rejected_msg = "GET PROCESS DETAIL: REJECTED"
            response = (commandstat,rejected_msg)
            return response

        elif(failed == '1'):
            failed_msg = "GET PROCESS DETAIL: FAILED"
            response = (commandstat,failed_msg)
            return response

        elif(succeed == '1'):
            succeed_msg = "GET PROCESS DETAIL: SUCCEED"
            response = (commandstat,succeed_msg)
            return response

        elif(inprogress == '1'):
            inprogress_msg = "GET PROCESS DETAIL: IN PROGRESS"
            response = (commandstat,inprogress_msg)
            return response

        elif(removed == '1'):
            removed_msg = "GET PROCESS DETAIL: REMOVED"
            response = (commandstat, removed_msg)
            return response

        elif(queued == '1'):
            queued_msg = "GET PROCESS DETAIL: QUEUED"
            response = (commandstat, queued_msg)
            return response
        else:
            message = binary_to_dict(response_g._content)["command_status"]
            response = (response_g.status_code,message)
            return response
    else:
        message = binary_to_dict(response_g._content)["message"]
        response = (response_g.status_code,message)
        return response