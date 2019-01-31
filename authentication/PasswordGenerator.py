import string
from random import *


def get_password(lenght):
    characters = list(string.ascii_letters + string.punctuation + string.digits)
    shuffle(list(characters))
    password = "".join(choice(characters) for symbol in range(lenght))
    return password
