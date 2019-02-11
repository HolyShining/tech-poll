import string
import base64
from random import *
from techpoll.secrets import BASE64_KEY


def get_password(lenght):
    characters = list(string.ascii_letters + string.punctuation + string.digits)
    shuffle(list(characters))
    password = "".join(choice(characters) for symbol in range(lenght))
    return password


def decode(text):
    return base64.b64decode(text)
