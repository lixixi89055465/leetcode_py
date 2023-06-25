dic = dict()
while True:
    try:
        s = input().split('\\')[-1].split()
        log = s[0][-16:] + ' ' + s[1]
        dic[log] = dic.get(log, 0) + 1
    except:
        break

for key, val in list(dic.items())[-8:]:
    print(key, val)
