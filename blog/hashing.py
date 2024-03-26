from passlib.context import CryptContext


class Hash():
    def hashing(password):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashedPasword = pwd_context.hash(password)
        return hashedPasword