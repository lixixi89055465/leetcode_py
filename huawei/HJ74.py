str1 = input()
flag = False
res = ""
for i in str1:
    if i == '"' and flag == False:
        flag = True
    elif i == '"' and flag:
        flag = False
    elif i==' ' and flag==False:
        res += "\n"
    else:
        res+=i
res = res.split('\n')
print(len(res))
for r in res:
    print(r.strip())
