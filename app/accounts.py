accounts = {}

def register_account(username, password, password2):
    if accounts.has_key(username) or password != password2:
        return False
    else:
        accounts[username] = password
        return True

def login_account(username, password):
    if accounts.has_key(username) and accounts[username] == password:
        return True
    else:
        return False
