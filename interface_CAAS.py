#!/usr/bin/python3
import logging
from lxml import etree
import copy
from itertools import cycle

from Tkconfig import *
from TkActions import *

logging.basicConfig(filename='CAAS_interface.log',level=logging.DEBUG,\
      format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')


PEI_ID = ""



# while ( login()[1].ok ) :
#     s = login()[0]
headers = {'Content-Type': 'application/xml'}
#     xml =  """  """

#     resp = s.post("https://sandbox-eu.triskellsoftware.com/triskell/service/rest/timephased/update",xml.encode('UTF-8'), headers)
#     print(resp.text)
#     break

# valorisation = get_report(REPORT_VALORISATION_ID,"2021-01-01","2021-12-31")
# regie_intere = valorisation['Vent regie, interne']
# forfait = valorisation['Vent forfaits']


# print("Valorisation des regies et internes")
# logging.info("Valorisation des regies et internes")

# for row in regie_intere :
#     organisation_id = row["Organisation_id"]
#     typederessource_id = row["Typederessource_id"]
#     unit_valorise = row["sum(JH_VALORISE)"]
#     period_id = row["period_id"]
#     timephased_id = AddTimephasedItem ("44181","964", "314", organisation_id, typederessource_id)
#     SaveTimephasedData( "44181","964", "314", timephased_id, period_id, unit_valorise)

# print("Valorisation des Forfaits")
# logging.info("Valorisation des Forfaits")

# for row in forfait :
#     organisation_id = row["Organisation_id"]
#     typederessource_id = row["Typederessource_id"]
#     unit_valorise = row["sum(JH_VALORISE)"]
#     period_id = row["period_id"]
#     timephased_id = AddTimephasedItem ("44181","964", "314", organisation_id, typederessource_id)
#     SaveTimephasedData( "44181","964", "314", timephased_id, period_id, unit_valorise)





# print("Ventilation global des JH et EUR")
# logging.info("##########  Ventilation global des JH & EUR ##########")

# vent_glb_jh = get_report(REPORT_VENTILATION_GLOBAL_JH_ID)
# vent_glb_eur = get_report(REPORT_VENTILATION_GLOBAL_EUR_ID)['Ventilation_EURO_global']
# dict_vent_eur = {}
# for row in vent_glb_eur :
#     cout_moyen = row['consomme_global']/row['consomme_valo']


# ventilation_JH_global = vent_glb_jh["Ventilation_JH_global"]
# Ventilation_PRJ_PEI = vent_glb_jh["Ventilation_PRJ_PEI"][0]

# proj_global = Ventilation_PRJ_PEI ['proj_global']
# conso_global_PEI = Ventilation_PRJ_PEI ['conso_global_PEI']

# dict_vent_jh ={}
# id1 = 0
# li = []
# for row in ventilation_JH_global :
#     dataobject_id = row['dataobject_id']
#     if dataobject_id != id1 :
#         dict_vent_jh[dataobject_id] = []
#         dict_vent_jh[dataobject_id].append( row['somme_revise'] )
#         id1 = dataobject_id
#     dict_vent_jh[dataobject_id].append(row['period_id'])


# for key in dict_vent_jh.keys():
#     timephased_jh_id = AddTimephasedItem (key,"805", "329", "1553", "4399")
#     timephased_eur_id = AddTimephasedItem (key,"964", "332", "1553", "4399")
    
#     list_periods = dict_vent_jh[key][1:]
#     budget_pei_x = dict_vent_jh[key][0]

#     result_jh = ((conso_global_PEI/proj_global) * budget_pei_x )/(len(list_periods))
     
#     for period in list_periods:
#         SaveTimephasedData( key,"805", "329", timephased_jh_id, period, str(result_jh))
    

#         result_eur = (result_jh * cout_moyen)/(len(list_periods))
#         SaveTimephasedData( key,"964", "332", timephased_eur_id, period, str(result_eur))



########################### VENTILATION DU DETAIL JH ###########################

# vent_det_jh = get_report(REPORT_VENTILATION_DETAIL_JH_ID)
# vent_det_jh_val = vent_det_jh['Ventilation_JH_detail']
# vent_det_jh_poids = vent_det_jh['Ventilation_JH_poids']

# # while (login()[1].ok) :
# resp = login()[0]
# name_tmp = ""  
# dict_vent_jh = {} 
# for row in vent_det_jh_val :
#       dataobject_name = row ['dataobject_name']
#       if dataobject_name != name_tmp :
#             dict_vent_jh[dataobject_name] = []   
#             dict_vent_jh[dataobject_name].append ( row['yyyy']) 
#             name_tmp = dataobject_name
            
#       for line in vent_det_jh_poids :
#             dict_temp = {}
#             dict_temp ['mm'] = row['mm']
#             dict_temp ['$Organisation'] =  line['$Organisation']
#             dict_temp ['$Typederessource'] =  line['$Typederessource']
#             dict_temp ['poids'] = line ['poids']
#             dict_temp ['unit'] = row['unit']
#             dict_vent_jh[dataobject_name].append(dict_temp)


            


# for key in dict_vent_jh.keys():
#       x = generate__xml(key,dict_vent_jh[key])
#       req = resp.post("https://sandbox-eu.triskellsoftware.com/triskell/service/rest/timephased/update",x,headers)
#       if req.text.__contains__('KO') == True :
#             print(req.text)
#             print("there are some erros")
#             #logging.info("There are some missing data for dataobject_name : ",key)
#       ## add in log file
#       if req.text.__contains__('OK') == True :
#             print("Tpa for project ", key, "scucessfully updated !")
                     



    
        
########################### VENTILATION DU DETAIL EURO ###########################

# vent_det_eur = get_report(REPORT_VENTILATION_DETAIL_EUR_ID)
# vent_det_eur_poids = vent_det_eur['Ventilation_EUR_detail']

# while (login()[1].ok) :
#     resp = login()[0]
#     name_tmp = ""  
#     dict_vent_eur = {} 
#     for row in vent_det_eur_poids :
#         dataobject_name = row ['dataobject_name']
#         if dataobject_name != name_tmp :
#             dict_vent_eur[dataobject_name] = []   
#             dict_vent_eur[dataobject_name].append (row['yyyy'])
#             dict_vent_eur[dataobject_name].append (row)
#             name_tmp = dataobject_name
#         else : 
#             dict_vent_eur[dataobject_name].append (row)

#     for key in dict_vent_eur.keys():
#         x = generate__xml(key,dict_vent_eur[key])
#         req = resp.post("https://sandbox-eu.triskellsoftware.com/triskell/service/rest/timephased/update",x,headers)
#         if req.text.__contains__('KO') == True :
#             print("there are some erros")
#             logging.info("There are some missing data for dataobject_name : ",key)
#             ## add in log file
#         if req.text.__contains__('OK') == True :
#             print("Tpa for project ", key, "scucessfully updated !")
#     break        
# 


########################### Ventilation des Euro en detail ###########################    

# vent_det_eur = get_report(REPORT_VENTILATION_DETAIL_EUR_ID)

# vent_det_eur_val = vent_det_eur['Ventilation_EUR_detail']
# vent_det_eur_poids = vent_det_eur['Ventilation_EUR_poids']

# # while (login()[1].ok) :
# resp = login()[0]
# name_tmp = ""  
# dict_vent_jh = {} 
# for row in vent_det_eur_val :
#       dataobject_name = row ['dataobject_name']
#       if dataobject_name != name_tmp :
#             dict_vent_jh[dataobject_name] = []   
#             dict_vent_jh[dataobject_name].append ( row['yyyy']) 
#             name_tmp = dataobject_name
            
#       for line in vent_det_eur_poids :
#             dict_temp = {}
#             dict_temp ['mm'] = row['mm']
#             dict_temp ['$Organisation'] =  line['$Organisation']
#             dict_temp ['$Typederessource'] =  line['$Typederessource']
#             dict_temp ['poids'] = line ['poids']
#             dict_temp ['unit'] = row['unit']
#             dict_vent_jh[dataobject_name].append(dict_temp)


            


# for key in dict_vent_jh.keys():
#       x = generate__xml(key,dict_vent_jh[key])
#       req = resp.post("https://sandbox-eu.triskellsoftware.com/triskell/service/rest/timephased/update",x,headers)
#       if req.text.__contains__('KO') == True :
#             print(req.text)
#             print("there are some erros")
#             #logging.info("There are some missing data for dataobject_name : ",key)
#       ## add in log file
#       if req.text.__contains__('OK') == True :
#             print("Tpa for project ", key, "scucessfully updated !")
















########################### Valorisation des Sqauds ###########################    
# 
# 
# ########################### VEntilation DETAIL Squads JH sur les Projets/Runs ########################### 


resp = login()[0] 
vent_det_squads_jh = get_report (REPORT_VENTILATION_DETAIL_SQUAD_JH_ID)
vent_det_squads_jh = vent_det_squads_jh['test squads']

name_tmp = ""  
dict_vent_squad_jh = {} 
for row in vent_det_squads_jh :
      
      dataobject_name = row ['dataobject_name']
      if dataobject_name != name_tmp :
            dict_vent_squad_jh[dataobject_name] = []   
            dict_vent_squad_jh[dataobject_name].append ( row['yyyy']) 
            name_tmp = dataobject_name
            
      dict_temp = {}
      dict_temp ['mm'] = row['mm']
      dict_temp ['$Organisation'] =  row['$Organisation']
      dict_temp ['$Typederessource'] =  row['$Typederessource']
      dict_temp ['poids'] = 1
      dict_temp ['unit'] = row ['result']
      dict_vent_squad_jh[dataobject_name].append(dict_temp)

print(dict_vent_squad_jh)
for key in dict_vent_squad_jh.keys():
      x = generate__xml(key,dict_vent_squad_jh[key], 805, "Consommé Squad")
      req = resp.post("https://sandbox-eu.triskellsoftware.com/triskell/service/rest/timephased/update",x,headers)
      if req.text.__contains__('KO') == True :
            print(req.text)
            print("there are some erros")
            #logging.info("There are some missing data for dataobject_name : ",key)
      ## add in log file
      if req.text.__contains__('OK') == True :
            print("Tpa for project ", key, "scucessfully updated !")




















########################### VEntilation DETAIL Squads EURO sur les Projets/Runs ########################### 

resp = login()[0] 
vent_det_squads_jh = get_report (REPORT_VENTILATION_DETAIL_SQUAD_EUR_ID)
vent_det_squads_jh = vent_det_squads_jh['tes squads2']

name_tmp = ""  
dict_vent_squad_jh = {} 
for row in vent_det_squads_jh :
      
      dataobject_name = row ['dataobject_name']
      if dataobject_name != name_tmp :
            dict_vent_squad_jh[dataobject_name] = []   
            dict_vent_squad_jh[dataobject_name].append ( row['yyyy']) 
            name_tmp = dataobject_name
            
      dict_temp = {}
      dict_temp ['mm'] = row['mm']
      dict_temp ['$Organisation'] =  row['$Organisation']
      dict_temp ['$Typederessource'] =  row['$Typederessource']
      dict_temp ['poids'] = 1
      dict_temp ['unit'] = row ['result']
      dict_vent_squad_jh[dataobject_name].append(dict_temp)

for key in dict_vent_squad_jh.keys():
      x = generate__xml(key,dict_vent_squad_jh[key], 964, "Consommé Squad")
      req = resp.post("https://sandbox-eu.triskellsoftware.com/triskell/service/rest/timephased/update",x,headers)
      if req.text.__contains__('KO') == True :
            print(req.text)
            print("there are some erros")
            #logging.info("There are some missing data for dataobject_name : ",key)
      ## add in log file
      if req.text.__contains__('OK') == True :
            print("Tpa for project ", key, "scucessfully updated !")












# ########################## VEntilation GLOBAL Squads JH sur les Projets/Runs ########################### 

resp = login()[0] 
vent_det_squads_jh = get_report (REPORT_VENTILATION_GLOBAL_SQUAD_JH_ID)
vent_det_squads_jh = vent_det_squads_jh['squads_synthese_jh']

name_tmp = ""  
dict_vent_squad_jh = {} 
for row in vent_det_squads_jh :
      
      dataobject_name = row ['dataobject_name']
      if dataobject_name != name_tmp :
            dict_vent_squad_jh[dataobject_name] = []   
            dict_vent_squad_jh[dataobject_name].append ( row['yyyy']) 
            name_tmp = dataobject_name
            
      dict_temp = {}
      dict_temp ['mm'] = row['mm']
      dict_temp ['$Organisation'] =  row['sousservice']
      dict_temp ['$Typederessource'] =  "Contribution Squad"
      dict_temp ['poids'] = 1
      dict_temp ['unit'] = row ['result']
      dict_vent_squad_jh[dataobject_name].append(dict_temp)

for key in dict_vent_squad_jh.keys():
      x = generate__xml(key,dict_vent_squad_jh[key], 805, "Consommé Squad synthèse")
      req = resp.post("https://sandbox-eu.triskellsoftware.com/triskell/service/rest/timephased/update",x,headers)
      if req.text.__contains__('KO') == True :
            print(req.text)
            print("there are some erros")
            #logging.info("There are some missing data for dataobject_name : ",key)
      ## add in log file
      if req.text.__contains__('OK') == True :
            print("Tpa for project ", key, "scucessfully updated !")     


















########################## VEntilation GLOBAL Squads EUR sur les Projets/Runs ########################### 

resp = login()[0] 
vent_det_squads_jh = get_report (REPORT_VENTILATION_GLOBAL_SQUAD_EUR_ID)
vent_det_squads_jh = vent_det_squads_jh['squads_synthese_eur']

name_tmp = ""  
dict_vent_squad_jh = {} 
for row in vent_det_squads_jh :
      
      dataobject_name = row ['dataobject_name']
      if dataobject_name != name_tmp :
            dict_vent_squad_jh[dataobject_name] = []   
            dict_vent_squad_jh[dataobject_name].append ( row['yyyy']) 
            name_tmp = dataobject_name
            
      dict_temp = {}
      dict_temp ['mm'] = row['mm']
      dict_temp ['$Organisation'] =  row['sousservice']
      dict_temp ['$Typederessource'] =  "Contribution Squad"
      dict_temp ['poids'] = 1
      dict_temp ['unit'] = row ['result']
      dict_vent_squad_jh[dataobject_name].append(dict_temp)

for key in dict_vent_squad_jh.keys():
      x = generate__xml(key,dict_vent_squad_jh[key], 964, "Consommé Squad synthèse")
      req = resp.post("https://sandbox-eu.triskellsoftware.com/triskell/service/rest/timephased/update",x,headers)
      if req.text.__contains__('KO') == True :
            print(req.text)
            print("there are some erros")
            #logging.info("There are some missing data for dataobject_name : ",key)
      ## add in log file
      if req.text.__contains__('OK') == True :
            print("Tpa for project ", key, "scucessfully updated !") 