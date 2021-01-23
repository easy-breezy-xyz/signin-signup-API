#!/usr/bin/env python3

import pickle

def fetch(loc, email):
    """
    File where emails are stored are param loc
    Email is param email
    Returns data if account exists
    Returns None if account does not exist
    """
    emails = pickle.load(open(loc, "rb"))
    nded = True
    for eml in emails:
        if eml[0] == email:
            resp = eml[2]
            nded = False
            break
    if nded:
        resp = None
    return resp
