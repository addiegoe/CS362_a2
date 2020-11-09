# check_pwd.py
# Author: Emily Addiego
# Due Date: 11/9/20

def check_pwd(pw):
    if len(pw) < 8:
        return False
    if len(pw) > 20:
        return False
    for i in pw:
        if i.islower():
            break
        else:
            return False
    for i in pw:
        if i.isupper():
            break
        else:
            return False
    return True
