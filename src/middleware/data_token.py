import jwt

class TokenUsers:

    @staticmethod
    def extract_user_info(token: str):
        try:
            decoded_token = jwt.decode(token, options={"verify_signature": False})
            user_id = decoded_token.get("sub")
            username = decoded_token.get("username")
            
            if not user_id or not username:
                raise ValueError("El token no contiene los campos necesarios (sub, username)")
            
            return user_id, username
        except jwt.DecodeError:
            raise ValueError("Token inválido.")
        except Exception as e:
            raise ValueError(f"Error al decodificar el token: {str(e)}")