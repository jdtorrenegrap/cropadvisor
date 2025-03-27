from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    GET_READS = os.getenv('endpoint_get_read')
    GET_ALERTS = os.getenv('endpoint_alert_config')
    GET_ADDRESS = os.getenv('endpoint_get_adress')
    
    #Redis
    REDIS_HOST = os.getenv('host')
    REDIS_PORT = os.getenv('port')
    DECODE_RESPONSES = os.getenv('decode_responses')