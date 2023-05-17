import pickle
import base64
import csv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import InvalidToken

class PasswordEncryption:
    '''
    Encoding and decoding different python objects with password and salt
    :param str password: password
    :param str salt: salt
    '''
    def __init__(self, password: str, salt: str):
        self.password = password.encode()
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt.encode(),
            iterations=100000
        )
        self.key = base64.urlsafe_b64encode(self.kdf.derive(self.password))

    def encrypt(self, data):
        if data is None:
            return None
        cipher = Fernet(self.key)
        encrypted_data = cipher.encrypt(pickle.dumps(data))
        return encrypted_data.decode()

    def decrypt(self, encrypted_data):
        try:
            cipher = Fernet(self.key)
            decrypted_data = cipher.decrypt(encrypted_data.encode())
            return pickle.loads(decrypted_data)
        except InvalidToken as e:
            #print('Error: Invalid password, debil!')
            return None