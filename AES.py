# Les cl´es ´echang´ees seront utilis´ees pour chiffrer les messages `
#a l’aide d’un syst`eme de chiffrement sym´etrique. Ajouter 
#une classe permettant l’ajout de la couche de chiffrement des messages avec le
#cryptosyst`eme AES-256.

from Crypto import Random
from Crypto.Cipher import AES, DES

# Vecteurs d'initialisation
iv_AES = Random.new().read(AES.block_size)
#iv_DES = Random.get_random_bytes(8)

#entree
key_AES = 'abcdefghijklmnop'
#key_DES = 'abcdefgh'

#entree
aese = AES.new(key_AES, AES.MODE_CFB, iv_AES)
aesd = AES.new(key_AES, AES.MODE_CFB, iv_AES)
