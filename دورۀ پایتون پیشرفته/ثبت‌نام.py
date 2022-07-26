def check_registration_rules(lst=[],**kwargs):
    for x,y in kwargs.items():
        if(len(x)>=4 and x!='quera' and x!='codecup' and len(y)>=6 and not all([i in '1234567890' for i in y])):
            lst.append(x)
    return(lst)
