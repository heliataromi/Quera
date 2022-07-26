from datetime import datetime
date = datetime.strptime(input(), '%Y-%m-%d')
date2 = datetime.strptime("1999-01-14",'%Y-%m-%d')
print((date - date2).days) if (date - date2).days > 0 else print("Not yet born")
