lst = []
for i in range(5):
    a = input()
    if("HAFEZ" in a or "MOLANA" in a):
        lst.append(str(i+1))
ans = " ".join(lst)
print(ans) if len(ans)>0 else print("NOT FOUND!")
