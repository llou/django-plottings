from string import ascii_letters, digits
from random import choice


chars = ascii_letters + digits


def random_name(length=5):
    return ''.join([choice(chars) for _ in range(length)])
