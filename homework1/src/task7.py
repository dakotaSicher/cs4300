import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Crypter:
    """
    Wraper class for a Fernet object that uses a 
    password derived key
    """
    SALT_SIZE = 16
    ITERATIONS = 1_200_000

    def __init__(self,password,salt=None):
        if salt is None:
            salt = os.urandom(self.SALT_SIZE)

        self.salt = salt
        password = password.encode("utf-8")
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations= self.ITERATIONS,
        )
        self.key = base64.urlsafe_b64encode(self.kdf.derive(password))
        self.f = Fernet(self.key)

    def encryptText(self,text:str)-> bytes:
        return self.f.encrypt(text.encode("utf-8"))
    
    def decryptText(self, text:bytes)->str:
        return self.f.decrypt(text).decode("utf-8")


def encryptFile(filepath,password:str)->str:
    """
    Reads a text file, encrypts it using a key derived from the password
    and write the encrypted bytes to a new file with the salt value used
    Returns: The filename of the encrypted file
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"input file not found:{filepath}")
    
    with open(filepath,"r") as Input:
        plaintext = Input.read()

    e = Crypter(password)
    encFile = f"enc_{os.path.basename(filepath)}"
    encText = e.encryptText(plaintext)

    with open(encFile,"wb") as Output:
        Output.write(e.salt + encText)

    return encFile


def decryptFile(enc_filepath,password:str)->str:
    """
    Read an encrypted file, decrypts using a key derived from the password 
    and a salt value read from the file, and writes the text to a new file
    Returns: the file name of the plaintext file
    """
    if not os.path.isfile(enc_filepath):
        raise FileNotFoundError(f"encrypted file not found: {enc_filepath}")
    
    with open(enc_filepath,"rb") as Input:
        raw = Input.read()

    salt = raw[:Crypter.SALT_SIZE]
    cipher = raw[Crypter.SALT_SIZE:]

    e = Crypter(password,salt)
    plaintext = e.decryptText(cipher)

    base = os.path.basename(enc_filepath)
    if base.startswith("enc_"):
        dec_base = base.replace("enc_","dec_",1)
    else:
        dec_base = f"dec_{base}"

    with open(dec_base,"w") as Output:
        Output.write(plaintext)

    return dec_base


if __name__=="__main__":
    print("1: encrypt a file")
    print("2: decrypt a file")
    sel = input("select an operation: ")
    pw = input("enter the password for encryption/decpryption: ", )
    file = input("enter filename: ")
    match int(sel):
        case 1:
            new_file = encryptFile(file, pw)
            print(f"encrypted file: {new_file}")
        case 2:
            new_file = decryptFile(file, pw)
            print(f"decrypted file: {new_file}")