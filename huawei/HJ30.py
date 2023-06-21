s = input()
s=s.replace(' ','')
oddAlpha = []
evenAlpha = []
lens = len(s)
for i in range(lens):
    if (i & 1):
        oddAlpha.append(s[i])
    else:
        evenAlpha.append(s[i])
oddAlpha = sorted(oddAlpha, reverse=False)
evenAlpha = sorted(evenAlpha, reverse=False)
map0 = {
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}
# map0.update({i: i for i in range(0, 10)})
map1 = {0:0,1: 8, 2: 4, 3: 12, 4: 2, 5: 10, 6: 6, 7: 14, 8: 1, 9: 9, 10: 5, 11: 13, 12: 3, 13: 11, 14: 7, 15: 15}
res = []
for i in range(len(oddAlpha)):
    res.append(evenAlpha[i])
    res.append(oddAlpha[i])
if len(evenAlpha) > len(oddAlpha):
    res.append(evenAlpha[-1])
for i in range(len(res)):
    res[i] = map1[map0[res[i]] if res[i] in map0 else int(res[i])]
    res[i] = str(chr(55 + res[i]) if res[i] >= 10 else res[i])
print(''.join(res))
