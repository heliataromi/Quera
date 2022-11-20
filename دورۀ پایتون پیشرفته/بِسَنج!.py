import re


def validate_email(email: str) -> bool:
    if re.search('^([\w\.]+)@([\w\.]+)\.([a-zA-Z]{3})$', email):
        return True
    return False


def validate_phone(number: str) -> bool:
    if re.search('^(\+98)?(0098)?(0)?9\d{9}$', number):
        return True
    return False
