# ==========
# File : user_managment.py
# Author : Jb
# First created on : 16/11/2018
# Description:
# ==========

from passlib.hash import pbkdf2_sha256


def encrypt(password):
    hash = pbkdf2_sha256(password)
    return hash


def verify(password, hash):
    return pbkdf2_sha256.verify(password, hash)
