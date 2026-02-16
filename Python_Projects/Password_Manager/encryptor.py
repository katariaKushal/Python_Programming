from cryptography.fernet import Fernet
import hashlib
import base64

class Encryptor:
    @staticmethod
    def generate_key(master_password):
        key = hashlib.sha256(master_password.encode()).digest()
        return Fernet(base64.urlsafe_b64encode(key))
    
    @staticmethod
    def encrypt(data, key):
        return key.encrypt(data.encode()).decode()
    
    @staticmethod
    def decrypt(data, key):
        return key.decrypt(data.encode()).decode()
