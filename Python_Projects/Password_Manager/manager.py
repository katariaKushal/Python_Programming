import json
import os
from encryptor import Encryptor

class PasswordManager:
    def __init__(self, filename="passwords.json"):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.key = None
        self.passwords = {}
    
    def authenticate(self, master_password):
        self.key = Encryptor.generate_key(master_password)
        self._load()
        return True
    
    def add_password(self, service, username, password):
        encrypted = Encryptor.encrypt(password, self.key)
        self.passwords[service] = {'username': username, 'password': encrypted}
        self._save()
        print(f"✓ Password saved for {service}")
    
    def get_password(self, service):
        if service in self.passwords:
            data = self.passwords[service]
            decrypted = Encryptor.decrypt(data['password'], self.key)
            print(f"\nService: {service}")
            print(f"Username: {data['username']}")
            print(f"Password: {decrypted}")
        else:
            print("✗ Service not found")
    
    def list_services(self):
        if not self.passwords:
            print("No passwords stored")
            return
        print("\n" + "="*40)
        for service, data in self.passwords.items():
            print(f"• {service} ({data['username']})")
        print("="*40)
    
    def delete_password(self, service):
        if service in self.passwords:
            del self.passwords[service]
            self._save()
            print("✓ Deleted")
        else:
            print("✗ Service not found")
    
    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.passwords = json.load(f)
    
    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.passwords, f, indent=2)
