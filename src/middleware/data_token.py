from fastapi import Security, HTTPException
from fastapi.security import HTTPBearer
from dotenv import load_dotenv
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

class TokenUsers:
    security = HTTPBearer()

    @staticmethod
    def extract_user_info(token: str):
        """Extrae información del usuario desde el token."""
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = decoded_token.get("sub")
            username = decoded_token.get("username")
            
            if not user_id or not username:
                raise ValueError("El token no contiene los campos necesarios (sub, username)")
            
            return user_id, username
        except Exception as e:
            raise ValueError(f"Error al decodificar el token: {str(e)}")

    @staticmethod
    def validate_token(credentials: Security = Security(security)):
        """Valida el token JWT desde el encabezado Authorization."""
        token = credentials.credentials
        print(f"Token recibido: {token}")
        try:
            jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return token  
        except Exception as e:
            raise ValueError(f"Error al decodificar el token: {str(e)}")