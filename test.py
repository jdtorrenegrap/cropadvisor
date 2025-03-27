from src.services.queries_service import QueriesService

# Instancia de QueriesService
queries_service = QueriesService()

# Token manual para la prueba
test_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwidXNlcm5hbWUiOiJyb290IiwiZW1haWwiOiJzdXBlckByb290LmNvbSIsInJvbF9pZCI6MSwiZXhwIjoxNzQzMDU5NDQyLCJpYXQiOjE3NDMwNTU4NDJ9.TVMgP35yaCORh_hufgfL0Xo-XvV53t8TMWvIiUcKQK8"

# Llamada al método get_reads
try:
    result = queries_service.get_reads(test_token)
    print(result)
except Exception as e:
    print(f"Error durante la prueba: {e}")