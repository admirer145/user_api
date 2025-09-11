import jwt
import datetime

SECRET_KEY = "your-secret-key"

def create_jwt_token(data):
    payload = {
        **data,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        "iat": datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expired
    except jwt.InvalidTokenError:
        return None  # Invalid token
    

import secrets

# Generate a random 32-byte (256-bit) secret key
secret_key = secrets.token_hex(32)  # Generates a 64-character hex string

print(secret_key)


