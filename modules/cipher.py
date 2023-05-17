import pickle
import base64
import csv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import InvalidToken

class PasswordEncryption:
    '''
    --- https://t.me/cryptogovnozavod ---
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
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        if data is None:
            return None
        encrypted_data = self.cipher.encrypt(pickle.dumps(data))
        return encrypted_data.decode()

    def decrypt(self, encrypted_data):
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data.encode())
            return pickle.loads(decrypted_data)
        except InvalidToken as e:
            #print('Error: Invalid password!')
            return None