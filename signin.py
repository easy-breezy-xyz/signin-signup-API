#!/usr/bin/env python3

import pickle

def signin(loc, email, pwd):
    """
    Sign in and compare data.
    File where emails are stored are param loc
    Email is param email
    Password is param pwd
    Returns True if account exists and password is correct
    Returns False if account exists but password is incorrect
    Returns None if account does not exist
    """
    emails = pickle.load(open(loc, "rb"))
    nded = True
    for eml in emails:
        if eml[0] == email:
            if eml[1] == pwd:
                nded = False
                resp = True
            else:
                resp = False
                nded = False
            break
    if nded:
        resp = None
    return resp
