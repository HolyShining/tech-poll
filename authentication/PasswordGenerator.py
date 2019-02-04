import string
import base64
from random import *
from techpoll.secrets import BASE64_KEY


def get_password(lenght):
    characters = list(string.ascii_letters + string.punctuation + string.digits)
    shuffle(list(characters))
    password = "".join(choice(characters) for symbol in range(lenght))
    return password


def encode(clear):
    key = BASE64_KEY
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(enc):
    key = BASE64_KEY
    dec = []
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
