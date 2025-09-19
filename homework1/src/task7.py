import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Crypter:
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

    def encryptText(self,text):
        return self.f.encrypt(text.encode("utf-8"))

    def encryptFile(self,filepath):
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"input file not found:{filepath}")
        
        with open(filepath,"r") as Input:
            plaintext = Input.read()

        encFile = f"enc_{os.path.basename(filepath)}"
        encText = self.encryptText(plaintext)

        with open(encFile,"wb") as Output:
            Output.write(self.salt + encText)

        return encFile

                
    def decryptText(self, text):
        return self.f.decrypt(text).decode("utf-8")


    def decryptFile(self,enc_filepath):
        if not os.path.isfile(enc_filepath):
            raise FileNotFoundError(f"encrypted file not found: {enc_filepath}")
        
        with open(enc_filepath,"rb") as Input:
            raw = Input.read()

        self.salt = raw[:self.SALT_SIZE]
        cipher = raw[self.SALT_SIZE:]
        self.key = base64.urlsafe_b64encode(self.kdf.derive(password))
        self.f = Fernet(self.key)

        plaintext = self.decryptText(cipher)

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
            c = Crypter(pw)
            new_file = c.encryptFile(file)
            print(f"encrypted file: {new_file}")
        case 2:
            c = Crypter(pw)
            new_file = c.decryptFile(file)
            print(f"decrypted file: {new_file}")