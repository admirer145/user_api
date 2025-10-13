import bcrypt 


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed)


hashed_pw = hash_password("mysecret")
print(verify_password("mysecret", hashed_pw))
print(verify_password("wrongpass", hashed_pw))
