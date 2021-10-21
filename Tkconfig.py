
from configparser import ConfigParser

parser = ConfigParser() 
parser.read('configuration.ini')

nb = 0
ERRORS = [  "parallel execution is locked",
            "USER_REPORT_ALREADY_EXECUTING",
            "Rules Engine - Could not get Dataobject Attr.",
            "User is allready executing a request"
            ]
OFFSET =  int(parser.get('settings', 'OFFSET'))
COUNT =  int(parser.get('settings', 'COUNT'))
OFFSET_ID =  int(parser.get('settings', 'OFFSET_ID'))
COUNT_ID =  int(parser.get('settings', 'COUNT_ID'))

PARAM1_ID =  int(parser.get('params', 'PARAM1_ID'))
PARAM2_ID =  int(parser.get('params', 'PARAM2_ID'))
PARAM3_ID =  int(parser.get('params', 'PARAM3_ID'))

token =  parser.get('settings', 'token')
username =  parser.get('settings', 'username')
domain =  parser.get('settings', 'domain')


nb_limit_try =  int(parser.get('settings', 'nb_limit_try'))
time_out =  int(parser.get('settings', 'time_out'))
currency_id = parser.get('settings', 'currency_id')

REPORT_VALORISATION_ID  = parser.get('settings', 'REPORT_VALORISATION_ID')
REPORT_VENTILATION_GLOBAL_JH_ID = parser.get('settings', 'REPORT_VENTILATION_GLOBAL_JH_ID')
REPORT_VENTILATION_GLOBAL_EUR_ID = parser.get('settings', 'REPORT_VENTILATION_GLOBAL_EUR_ID')
REPORT_VENTILATION_DETAIL_JH_ID = parser.get('settings','REPORT_VENTILATION_DETAIL_JH_ID')
REPORT_VENTILATION_DETAIL_EUR_ID = parser.get('settings','REPORT_VENTILATION_DETAIL_EUR_ID')

REPORT_VENTILATION_DETAIL_SQUAD_JH_ID = parser.get('settings','REPORT_VENTILATION_DETAIL_SQUAD_JH_ID')
REPORT_VENTILATION_DETAIL_SQUAD_EUR_ID = parser.get('settings','REPORT_VENTILATION_DETAIL_SQUAD_EUR_ID')

REPORT_VENTILATION_GLOBAL_SQUAD_JH_ID = parser.get('settings','REPORT_VENTILATION_GLOBAL_SQUAD_JH_ID')
REPORT_VENTILATION_GLOBAL_SQUAD_EUR_ID = parser.get('settings','REPORT_VENTILATION_GLOBAL_SQUAD_EUR_ID')