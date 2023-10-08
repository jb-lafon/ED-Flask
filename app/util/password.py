# ==========
# File : user_managment.py
# Author : Jb
# First created on : 16/11/2018
# Description: Password hashing functions
# ==========

from uuid import uuid4
from hashlib import sha256


def hash_password(password):
    salt = uuid4().hex
    return sha256(salt.encode() + password.encode()).hexdigest() + 'CgysjT37' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split('CgysjT37')
    print(salt)
    print(password)
    return password == sha256(salt.encode() + user_password.encode()).hexdigest()
