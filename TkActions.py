#!/usr/bin/python3

import requests
import json
import base64
from configparser import ConfigParser
import logging
import sys
import traceback
from Tkconfig import *
from lxml import etree

# logging.basicConfig(filename='caas_interface.log',level=logging.DEBUG,\
#       format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')

stateless_header={"Content-Type": 'application/json', "X-API-Key" : token, "X-Account-Name" : username} # Header for statless requests 



def encode_body (body):
    body_bytes = body.encode('ascii')
    encoded_body_bytes = base64.b64encode(body_bytes)
    encoded_body = encoded_body_bytes.decode('ascii')
    return (encoded_body)

def get_report(id,*params):
    print(" Retrieving your report ... ")
    logging.info('Retreiving report number %s', id)

    tries  =  0
    OFFSET =  int(parser.get('settings', 'OFFSET'))
    dict_result = {}
    test_rest= True
    iteration = 1

    parameters = ""
    if (len(params) != 0) :

        parameters =   "##" + str(PARAM1_ID) + "#" + str(params[0]) +"##" + str(PARAM2_ID) + "#" + str(params[1]) 


    while (test_rest):
        
        data = {
            "id": 0,
            "params": {
                "REPORTID": id,
                "valuesByParams":  str(OFFSET_ID) + "#" + str( OFFSET) + "##" + str(COUNT_ID) + "#" + str(COUNT) + parameters
            },
            "objects": None}
           
        print(data)
        body = encode_body(str(data))
        try :
            report_req = requests.get(
                domain+"/triskell/service/rest/proxy/operation/execute/ReportService/GetReportDataToPanel/"+body, headers=stateless_header)

            json_req =   json.loads(report_req.text) 
            success = json_req["success"]
            message = json_req['message']
            error = json_req["ret_i18n_code"]   
            if success == False :
                print(message)
                sys.exit("aa! errors!")

            if success and iteration == 1 :
                 
                  res = json_req["data"]
                  for key in res.keys() : 
                        dict_result[key] =  []                
                  iteration +=1 
                  continue


            
            if success and iteration > 1:
                      
                  res = json_req["data"]
                             
                  for key in res.keys() : 
                        dict_result[key] =  dict_result[key] + res[key]['res']
            
                
                  table_rest = []
                  d = json_req['description'].split("#")
                  c = len(json_req['description'].split("#"))
                  for i in range (0, c , 4):
                        table_rest.append ( d[i+2].split(',')[0] )
                  if not('1000' in table_rest) :
                        test_rest = False
                  
                  OFFSET = str (int(OFFSET)+int(COUNT))
                  


            
            if tries > 5 : 
                logging.critical("Server Time Out. Eroor message : %s",error)
                error = "We were unable to retrieve report's id " + id +" During this process"+"\nerror message : "+error 
                              
                break

            elif error.upper() in ERRORS : 
                tries += 1
                logging.error('%s',error," We will try again !")

        except BaseException as ex:
            # Get current system exception
            ex_type, ex_value, ex_traceback = sys.exc_info()

            # Extract unformatter stack traces as tuples
            trace_back = traceback.extract_tb(ex_traceback)

            # Format stacktrace
            stack_trace = list()

            for trace in trace_back:
                stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
            
            print("Exception type : %s " % ex_type.__name__)
            print("Exception message : %s" %ex_value)
            print("Stack trace : %s" %stack_trace)
            logging.critical("Stack trace : %s" %stack_trace)
            print("Unable to retrieve report's id", id,'\nerror message : ', message,'\n')
            logging.error("Unable to retrieve report's id; %s, error message : %s ", id, message)
   
            break 
    if success :
        logging.info("Report's id ,%s, is successfully retrieved", id) 

    return(dict_result)   

def update_dataobject_att (dataobeject_id, att_id, value):
    
    tries = 0
    logging.info('accessing update_dataobject_att function for dataobjject_id %s',dataobeject_id)

    data ={
    "id" : 0 ,
    "params" :
    {    "DATAOBJECT_ID": dataobeject_id,
         "attr_"+ att_id : value
    } ,
    "objects" : None
    }
    body = encode_body(str(data))
    print(data)
    try : 
        resp = requests.get(domain +"/triskell/service/rest/proxy/operation/execute/CustomAttrPanelAS/CustomAttrPanelPutValues/" + body, headers = stateless_header)
        json_req = json.loads(resp.text)
        print(json_req)
        success = json_req["success"]
        message = json_req['message']
        error = json_req["ret_i18n_code"]
        
        if success :
            return (True)


    except BaseException as ex:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
        print("We were unable to complete the action  During this process"+"\nerror message : "+message )
          
        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" %ex_value)
        print("Stack trace : %s" %stack_trace)
        logging.critical("Stack trace : %s" %stack_trace)

def add_dataobject_relation (obj1_id, obj2_id, rel_id):
    
    tries = 0
    logging.info('accessing add_dataobject_relation function ')

    data ={
    "id" : 0 ,
    "params" :
    {    "rel1": obj1_id +'|'+obj2_id,
         "numAssignements":"1",
         "objectRelationId": rel_id
    } ,
    "objects" : None
    }
    body = encode_body(str(data))
    print(data)
    try : 
        resp = requests.get(domain +"/triskell/service/rest/proxy/operation/execute/TkRelatedObjectAssignerAS/SaveDataobjectRelationship/" + body, headers = stateless_header)
        json_req = json.loads(resp.text)
        
        success = json_req["success"]
        message = json_req['message']
        error = json_req["ret_i18n_code"]
        
        if success :
            print("relation succefully established !")
            return (True)
        else :
            print("A problem has occured !")


    except BaseException as ex:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
        print("We were unable to complete the action  During this process"+"\nerror message : "+message )
          
        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" %ex_value)
        print("Stack trace : %s" %stack_trace)
        logging.critical("Stack trace : %s" %stack_trace)

def add_role (user_id, dataobject_id, role_id):
    user_id = str(user_id)
    tries = 0
    logging.info('accessing add_role function ')

    data ={
    "id" : 0 ,
    "params" :
    {    "user_id": user_id,
         "dataobject_id": dataobject_id,
         "role_id": role_id
    } ,
    "objects" : None
    }
    body = encode_body(str(data))
    print(data)
    try : 
        resp = requests.get(domain +"/triskell/service/rest/proxy/operation/execute/UsersRestService/AddRole/" + body, headers = stateless_header)
        json_req = json.loads(resp.text)
        
        success = json_req["success"]
        message = json_req['message']
        error = json_req["ret_i18n_code"]
        
        if success :
            print("Role has been succefully added !")
            return (True)
        else :
            print("A problem has occured !")


    except BaseException as ex:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
        print("We were unable to complete the action  During this process"+"\nerror message : "+message )
          
        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" %ex_value)
        print("Stack trace : %s" %stack_trace)
        logging.critical("Stack trace : %s" %stack_trace)

def delete_role (user_id, dataobject_id, role_id):
    user_id = str(user_id)
    tries = 0
    logging.info('accessing add_role function ')

    data ={
    "id" : 0 ,
    "params" :
    {    "user_id": user_id,
         "dataobject_id": dataobject_id,
         "role_id": role_id
    } ,
    "objects" : None
    }
    body = encode_body(str(data))
    print(data)
    try : 
        resp = requests.get(domain +"/triskell/service/rest/proxy/operation/execute/UsersRestService/RemoveRole/" + body, headers = stateless_header)
        json_req = json.loads(resp.text)
        
        success = json_req["success"]
        message = json_req['message']
        error = json_req["ret_i18n_code"]
        
        if success :
            print("Role has been succefully added !")
            return (True)
        else :
            print("A problem has occured !")


    except BaseException as ex:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
        print("We were unable to complete the action  During this process"+"\nerror message : "+message )
          
        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" %ex_value)
        print("Stack trace : %s" %stack_trace)
        logging.critical("Stack trace : %s" %stack_trace)


def SaveTimephasedData( dataobject_id, attr_id, version_id, timephased_item_id,period_id, units):
    data ={
    "id" : 0 ,
    "params" :
    {    "dataObjectId": str(dataobject_id),
         "attrId": str(attr_id),
         "versionId": str(version_id),
         "ID": str(timephased_item_id),
         "PERIODID": str(period_id), 
         "UNITS": str(units),
         
         "currencyId": str(currency_id)
    } ,
    "objects" : None
    }

    body = encode_body(str(data))

    try : 
        resp = requests.get(domain +"/triskell/service/rest/proxy/operation/execute/TimephasedAttributeAS/SaveTimephasedData/" + body, headers = stateless_header)
        json_req = json.loads(resp.text)
        success = json_req["success"]
        message = json_req['message']
        error = json_req["ret_i18n_code"]
        
        if success :
            print("TPA for dataobject_id = ",dataobject_id,"has been succefully updated !")
            logging.info("TPA for dataobject_id = ",dataobject_id,"has been succefully updated !")
            return (True)
        else :
            print("A problem has occured !")


    except BaseException as ex:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
        print("We were unable to complete the action  During this process"+"\nerror message : "+message )
          
        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" %ex_value)
        print("Stack trace : %s" %stack_trace)
        logging.critical("Stack trace : %s" %stack_trace)


def AddTimephasedItem (dataobject_id,attr_id, version_id, cust_attr_1, cust_attr_2):
    
    tries = 0
    logging.info('accessing add_dataobject_relation function ')

    data ={
    "id" : 0 ,
    "params" :
    {    "dataObjectId": str(dataobject_id) ,
         "attrId": attr_id,
         "versionId": version_id,
         "ATTRID_622": str(cust_attr_1),
         "ATTRID_486": str(cust_attr_2)
    } ,
    "objects" : None
    }
    body = encode_body(str(data))
    print(data)
    try : 
        resp = requests.get(domain +"/triskell/service/rest/proxy/operation/execute/TimephasedAttributeAS/AddTimephasedItem/" + body, headers = stateless_header)
        json_req = json.loads(resp.text)
        success = json_req["success"]
        message = json_req['message']
        error = json_req["ret_i18n_code"]
        
        if success :
            print("Tpa Item has been succefully created")
            timephased_id = json_req['data'][0]['timephasedItemId']
            return (timephased_id)
        else :
            print("A problem has occured !")
            print(message)
            


    except BaseException as ex:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
        
        print(message)
        print("We were unable to complete the action  During this process"+"\nerror message : "+message )
          
        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" %ex_value)
        print("Stack trace : %s" %stack_trace)
        logging.critical("Stack trace : %s" %stack_trace)
   

def update_workflow (id):


  
    tries = 0
    logging.info('accessing add_role function ')
    data ={
    "id" : 0 ,
    "params" :
    {    "dataObjectId": str(id),
         "newLifecycle": "237",
         "commentToTransition": "",
         "attachmentsToTransition": ""
    } ,
    "objects" : None
    }
    body = encode_body(str(data))
    print(data)
    try : 
        resp = requests.get(domain +"/triskell/service/rest/proxy/operation/execute/ObjectPropertiesPanelAS/AdvancedLifecycleChange/" + body, headers = stateless_header)
        json_req = json.loads(resp.text)
        
        success = json_req["success"]
        message = json_req['message']
        error = json_req["ret_i18n_code"]
        
        if success :
            print("Role has been succefully added !")
            return (True)
        else :
            print("A problem has occured !")


    except BaseException as ex:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
        print("We were unable to complete the action  During this process"+"\nerror message : "+message )
          
        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" %ex_value)
        print("Stack trace : %s" %stack_trace)
        logging.critical("Stack trace : %s" %stack_trace)

def login() :
    s = requests.session()
    r = s.get("https://sandbox-eu.triskellsoftware.com/triskell/service/rest/login/user/admin@caas_import5.fr/passwd/abe44d75d0a36d2b2ad5d8b30eba48afae7e41c848a84ea2b5f2ceea6be935ca")
    
    code = r.status_code

    authash = r.cookies.values()[0]
    JESESSIONID =  r.cookies.values()[1]
    return(s,r)

def generate__xml (dataobject_name, list_data, attr_id, version_name) : 

    unit = list_data[1]

    root = etree.Element('timephased')

    # another child with text
    child_1 = etree.Element('object')
    child_1.text = '113'
    root.append(child_1)

    # another child with text
    child_2 = etree.Element('timephased_attribute')
    child_2.text = str(attr_id)
    root.append(child_2)

    # another child with text
    child_3 = etree.Element('rate_type')
    child_3.text = '0'
    root.append(child_3)

    # another child with text
    child_4 = etree.Element('path')
    child_4.text = "Portefeuille d'activités"
    root.append(child_4)



            
    child_5 = etree.Element('name')
    child_5.text = dataobject_name
    root.append(child_5)
    name = dataobject_name

    child_6 = etree.Element('version')
    
    root.append(child_6)
    
    child_7 = etree.Element('name')
    child_7.text = version_name
    child_6.append(child_7)


    child_8 = etree.Element('year')
    child_6.append(child_8)

    child = etree.Element('value')
    child.text = str (list_data[0])
    child_8.append(child)
    month = 0
    for row in list_data[1:]:

        if month != row['mm'] :
            child_month = etree.Element('month')
            child_8.append(child_month)
            child  = etree.Element('value') 
            child.text = str (row['mm'])
            child_month.append(child)

            month = row['mm']

        child_row = etree.Element('row')
        child_month.append(child_row)

        child = etree.Element('id')
        child.text = "2"
        child_row.append(child)

        child_attributes = etree.Element("attributes")
        child_row.append(child_attributes)

        child_attribute = etree.Element('attribute')
        child_attributes.append(child_attribute)

        child = etree.Element('name')
        child.text = "ATTRID_622"
        child_attribute.append(child)

        child = etree.Element('value')
        child.text = row['$Organisation']
        child_attribute.append(child)

        child_attribute = etree.Element('attribute')
        child_attributes.append(child_attribute)

        child = etree.Element('name')
        child.text = "ATTRID_486"
        child_attribute.append(child)

        child = etree.Element('value')
        child.text = row['$Typederessource']
        child_attribute.append(child)

        child = etree.Element('amount')
        child.text = str (row['unit'] * row ['poids'])
        child_row.append(child)

        child = etree.Element('unit')
        child.text = 'Euro'
        child_row.append(child)
    s = etree.tostring(root, encoding='UTF-8', pretty_print=True)
    return (s)
        


        

    

