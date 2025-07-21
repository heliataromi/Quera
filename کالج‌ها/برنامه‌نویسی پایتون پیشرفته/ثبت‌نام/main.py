def check_registration_rules(**kwargs: str) -> list[str]:
    result = []

    INVALIDS = ['quera', 'codecup']

    for username, password in kwargs.items():
        if (len(username) >= 4 and username not in INVALIDS and
            len(password) >= 6 and not password.isdigit()):
            result.append(username)

    return result
