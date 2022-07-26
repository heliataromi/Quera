a=[]
for i in range(4):
    a.append(int(input()))
print("Sum : {:.6f}".format(sum(a)))
print("Average : {:.6f}".format(sum(a)/4))
b=1
for i in a:
    b*=i
print("Product : {:.6f}".format(b))
print("MAX : {:.6f}".format(max(a)))
print("MIN : {:.6f}".format(min(a)))
