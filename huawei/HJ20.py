'''
HJ20 密码验证合格程序
描述
密码要求:

1.长度超过8位

2.包括大小写字母.数字.其它符号,以上四种至少三种

3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）

数据范围：输入的字符串长度满足
1
≤
�
≤
100

1≤n≤100
输入描述：
一组字符串。

输出描述：
如果符合要求输出：OK，否则输出NG

示例1
输入：
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
复制
输出：
OK
NG
NG
OK

'''
s = input()
# 1.长度
if len(s) < 9:
    print('NG')
    exit(0)

isBigLetter = False
isLittleLetter = False
isNum = False
isOther = False
for c in s:
    if c >= 'a' and c <= 'z':
        isLittleLetter = True
    elif c >= 'A' and c <= 'Z':
        isBigLetter = True
    elif c.isalnum():
        isNum = True
    elif c == ' ':
        continue
    else:
        isOther = True
res = 0
if isBigLetter:
    res += 1
if isLittleLetter:
    res += 1
if isOther:
    res += 1
if isNum:
    res += 1
if res < 3:
    print('NG')
    exit(0)

n = len(s)
visit = set()

for i in range(n - 2):
    if s[i:i + 3] in visit:
        print('NG')
        exit(0)
    else:
        visit.add(s[i:i + 3])
print('OK')
