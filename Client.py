import socket
from threading import Thread
from Crypto.Cipher import AES

def receive():
    while True:
        data = c.recv(102).decode("utf8")
        print(data)

#After encrypting, server will send the key to the client as string, To decrypt
 en = eval(msg)
 decrypt = key.decrypt(en)
 # hashing sha1
 en_object = hashlib.sha1(decrypt) en_digest = en_object.hexdigest()


# this method to encrypt your data and send the encrypted data
def do_encrypt(message):
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(message)
    return ciphertext

host = 'localhost'
port = 12345
addr = (host,port)
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(addr)
print("enter your name")
name = input()
c.send(bytes(name,"utf8"))
Thread(target = receive).start()
while True:
    #print(name,end = '')
    data = input()
    c.send(bytes(data,'utf8'))