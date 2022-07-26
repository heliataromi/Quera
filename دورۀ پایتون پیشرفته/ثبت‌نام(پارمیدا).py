def check_registration_rules(**kw):
    accepted = []
    for x, y in kw.items():
        if(x != 'codecup' and x != 'quera' and len(x) >= 4 and len(y) >= 6):
            p = 0
            for x in (password):
                if(x in '0123456789'):
                    p += 1
            if(p != len(password)):
                accepted.append(username)
    return(accepted)
