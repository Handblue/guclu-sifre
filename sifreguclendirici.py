import re

def password_strength_checker(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[_@$]", password):
        return False
    return True

password = input("Şifren: ")
if password_strength_checker(password):
    print("Güçlü Şifre")
else:
    print("Zayıf Şifre")
