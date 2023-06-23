s = input()
s = s.replace(' ', '')
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

map1 = {'0': '0', '1': '8', '2': '4', '3': 'C', '4': '2', '5': 'A', '6': '6', '7': 'E', '8': '1', '9': '9',
        'a': '5', 'b': 'D', 'c': '3', 'd': 'B', 'e': '7', 'f': 'F',
        'A': '5', 'B': 'D', 'C': '3', 'D': 'B', 'E': '7', 'F': 'F'
        }
res = []
for i in range(len(oddAlpha)):
    res.append(evenAlpha[i])
    res.append(oddAlpha[i])
if len(evenAlpha) > len(oddAlpha):
    res.append(evenAlpha[-1])
for i in range(len(res)):
    res[i] = map1[res[i]] if res[i] in map1 else res[i]
print(''.join(res))
