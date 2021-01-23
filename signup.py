#/usr/bin/env python3

import pickle

def signup(loc, sname, spwd):
    """
    Sign in and compare data.
    File where emails are stored are param loc
    Email is param sname
    Password is param pwd
    Returns True if account is created sucessfully
    Returns False if account already exists
    """
    emails = pickle.load(open(loc, "rb"))
    ok = True
    if ok:
        email = [str(sname).strip(), str(spwd)]
        emails.append(email)
        pickle.dump(emails, open(loc, "wb"))
        msg = True
    else:
        msg = False
    return msg
