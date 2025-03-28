import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from dotenv import load_dotenv
from src.services.queries_service import QueriesService


load_dotenv()

queries_service = QueriesService()

test_token = os.getenv("TEST_TOKEN")

try:
   
    print("Probando get_reads...")
    reads_result = queries_service.get_reads(test_token)
    print(f"Resultado de get_reads:\n{reads_result}\n")

    # Probar el método get_alerts
    print("Probando get_alerts...")
    alerts_result = queries_service.get_alerts(test_token)
    print(f"Resultado de get_alerts:\n{alerts_result}\n")

    # Probar el método get_adress
    print("Probando get_adress...")
    address_result = queries_service.get_adress()
    print(f"Resultado de get_adress:\n{address_result}\n")

except Exception as e:
    print(f"Error durante las pruebas: {e}")