import requests
from src.core.config import Settings
from src.middleware.data_token import TokenUsers


class QueriesService:

    def __init__(self):
        self.settings = Settings()
        self.data_token = TokenUsers()

    def get_reads(self, token):
        username = self.data_token.extract_user_info(token)[1]
        headers = {"Authorization": f"Bearer {token}"}

        response = requests.get(f"{self.settings.GET_READS}{username}", headers=headers)

        if response.status_code == 200:
            data = response.json()
            if data:
                formatted_data = "**Lecturas de sensores:**\n"
                for i in data:
                    formatted_data += f"- **Sensot:** {i.get('device_id', 'N/A')}\n"
                    formatted_data += f"  **Unidad de medida:** {i.get('unit_id', 'N/A')}, Valor: {i.get('value', 'N/A')}\n"
                    formatted_data += f"  *Fecha:** {i.get('created_at', 'N/A')}\n"
                return formatted_data.strip()
            else:
                return "No se encontraron lecturas de sensores."
        else:
            return f"Error al obtener lecturas. Código: {response.status_code}, Detalle: {response.text}"