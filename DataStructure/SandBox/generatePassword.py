import string
import random

def genPassword(x):
    chars = string.ascii_letters + string.digits + '#@%&^(){}'
    password = ''.join(random.choice(chars) for i in range(x))
    return password

key = genPassword(10)
print(key)