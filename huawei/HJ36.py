s = input()
keyText = []
charSet = set()
for i in s:
    if i not in charSet:
        keyText.append(i)
        charSet.add(i)
for i in range(0, 26):
    A = chr(ord('a') + i)
    if A not in charSet:
        keyText.append(A)
clearText = input()
res = []
for c in clearText:
    res.append(keyText[ord(c) - ord('a')])
print(''.join(res))
