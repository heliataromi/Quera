import re
def invalid(s):
    c = len(s)
    for x in s:
        if(re.match("[\w\s]", x)):
            c -= 1
    if(c > len(s)/2 and re.search('spam', s.lower())):
        return(True)
sender = input()
content = input()
if(sender.isdigit()):
    if(invalid(content)):
        print("Fully Invalid")
    else:
        print("Invalid Sender")
elif(invalid(content)):
    print("Invalid Content")
else:
    print("Not Spam")
