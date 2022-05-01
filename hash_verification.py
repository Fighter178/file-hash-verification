"""SHA File Verification. Includes encryption meathods."""
import hashlib
import pyAesCrypt
from os import remove
def hash_sha256_file(file):
    with open(file, "r") as f:
        return hashlib.sha256(f.read().encode()).hexdigest()
def verify_sha256_hash(stored, file):
    with open(file, "r") as f:
        with open(stored, 'r') as s:
            if hashlib.sha256(f.read().encode()).hexdigest() == s.read():
                return True
            else:
                return False
def encrypt_file(file, outfile, password, buffer=64*1024, deletePlaintext=False):
    pyAesCrypt.encryptFile(file, outfile, password, buffer)
    if deletePlaintext == True:
        remove(file)
def decrypt_file(file, outfile, password, buffer=64*1024, deleteEncrypted=False):
    pyAesCrypt.decryptFile(file, outfile, password, buffer)
    if deleteEncrypted == True:
        remove(file)
