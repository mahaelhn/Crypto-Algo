from threading import Thread
import socket
from Crypto.Cipher import AES
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

import hashlib
from cryptography.hazmat.primitives.asymmetric import (padding, rsa, utils)

addr_client = {}
clients  = {}
count = 0

def incoming_connection():
    while True:
        conn, client_addr = s.accept()
        print(client_addr)
        #print(conn)
        addr_client[conn] = client_addr
        #print (conn)
        Thread(target = client_connection, args = (conn,)).start()


def client_connection(conn):
    name = conn.recv(100).decode("utf8")
    clients[conn] = name

    while True:
        msg = conn.recv(100).decode("utf8")
        broadcast(msg,name+":")


def broadcast(msg,prefix):
    for sock in clients:
        #print(prefix)
        sock.send(bytes(prefix+msg,"utf8"))


#Receive data and call this method to decrypt the data
def do_decrypt(ciphertext):
    obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    message = obj2.decrypt(ciphertext)
    return message

 #encrypting session key and public key
 E = server_public_key.encrypt(encrypto,16)

#import a annuairePKI.txt file, question 3

def importfile():
  array1 = []
  array2 = []

  with open('annuairePKI.txt', 'r') as f:
     for line in f.readlines():
         l = line.strip().split(',')
         array1 = l[0]
         array2 = l[1]

#ajouter la focntionalite de la signature numerique 
def signature()
    private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048)
    prehashed_msg = hashlib.sha256(b"A message I want to sign").digest()
    signature = private_key.sign(prehashed_msg,padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH),utils.Prehashed(hashes.SHA256()))
    public_key = private_key.public_key()
    public_key.verify(signature,prehashed_msg,padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH), utils.Prehashed(hashes.SHA256()))



host = 'localhost'
port = 12345
addr = (host,port)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(addr)

s.listen(5)
print ("waiting for connection")
Thread (target = incoming_connection).start()
#Thread (target = incoming_connection).join()