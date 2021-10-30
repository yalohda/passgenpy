#!/usr/bin/env python3
"""Password generator."""
# -*- coding: UTF-8 -*-
import random
import string


def gen(length=8, method=["lowercase", "uppercase", "digits", "punctuation"]):
    """String.lowercase, uppercase, digits, punctuation."""
    pwd = []
    for i in range(length):
        choice = random.choice(method)
        if choice == "lowercase":
            pwd.append(random.choice(string.ascii_lowercase))
        if choice == "uppercase":
            pwd.append(random.choice(string.ascii_uppercase))
        if choice == "digits":
            pwd.append(random.choice(string.digits))
        if choice == "punctuation":
            pwd.append(random.choice(string.punctuation))
        if choice == "string":
            pwd.append(random.choice(string.punctuation))

    random.shuffle(pwd)
    return ''.join(pwd)

# Examples
print (gen())  # /79](g}7L
print (gen(method=["uppercase"]))  # RSLCHWYED
print (gen(method=["digits"]))  # 894157281
print (gen(method=["punctuation"]))  # ~|{-()_**
print (gen(method=["uppercase", "lowercase", "digits"]))  # 0ceA711iq
print (gen(length=15, method=["uppercase", "lowercase", "digits"]))  # 97A3M481njJs1H3B
