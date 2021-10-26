
from cryptography.fernet import Fernet

def generate_key(filename):
    __key = Fernet.generate_key()
    file = open(f'{filename}.key', 'wb')
    file.write(__key)
    file.close()
    return __key


def crypt(key, filename):
    __file = open(filename, 'rb')
    __original = __file.read()
    fernet = Fernet(key)
    __encrypted = fernet.encrypt(__original)
    print('Criptografando... Por favor aguarde...\n')
    with open(filename, 'wb')as encrypted_file:
        encrypted_file.write(__encrypted)


def decrypt(key, filename):
    enc_file = open(filename, 'rb')
    encrypted = enc_file.read()
    file = open(key, 'r')
    key = file.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted)
    print('descriptografando... Por favor aguarde...\n')
    with open(filename, 'wb') as dec_file:
        dec_file.write(decrypted)
