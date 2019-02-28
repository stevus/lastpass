#!/usr/bin/env python
# coding: utf-8

import json
import os
from lastpass import (
    Vault
)
from prettytable import PrettyTable

DEVICE_ID = "example.py"

with open(os.path.join(os.path.dirname(__file__), 'credentials.json')) as f:
    credentials = json.load(f)
    username = credentials['username']
    password = credentials['password']

# TODO: Could use some account error checking/handling
vault = Vault.open_remote(username, password, None, DEVICE_ID)

t = PrettyTable(['Name', 'Username', 'Password'])

for index, i in enumerate(vault.accounts):
    t.add_row([
        i.name.decode("utf-8"),
        i.username.decode("utf-8"),
        i.password.decode("utf-8")
    ])

print(t)
