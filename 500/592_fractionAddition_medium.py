'''
592. 分数加减运算
给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。

这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。



示例 1:

输入: expression = "-1/2+1/2"
输出: "0/1"
 示例 2:

输入: expression = "-1/2+1/2+1/3"
输出: "1/3"
示例 3:

输入: expression = "1/3-1/2"
输出: "-1/6"


提示:

输入和输出字符串只包含 '0' 到 '9' 的数字，以及 '/', '+' 和 '-'。
输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 '+' 会被省略掉。
输入只包含合法的最简分数，每个分数的分子与分母的范围是  [1,10]。 如果分母是1，意味着这个分数实际上是一个整数。
输入的分数个数范围是 [1,10]。
最终结果的分子与分母保证是 32 位整数范围内的有效整数。
'''
import re
class Solution:
    def getZiMu(self,zi,mu):
        if zi==0:
            return 0,1
        for i in [2,3,4,5,7]:
            while zi%i==0 and mu%i==0:
                zi=zi//i
                mu=mu//i
        return zi,mu
    def getResult(self,left0,right0,left1,right1):
        zi,mu=self.getZiMu(left0*right1+left1*right0,right0*right1)
        return (zi,mu)
    def str2int(self,a):
        result=[]
        for i in a.split('/'):
            result.append(int(i))
        return result

    def fractionAddition(self, expression: str) -> str:
        arr=[]
        s=(0,1)
        arr=re.split('\+|-',expression)
        print(arr)
        intarr=[]
        for a in arr:
            if not a:
                continue
            intarr.append(self.str2int(a))
        start=0
        s=(0,1)
        for i in range(0,len(expression)):
            if i ==0 and expression[0]!='-':
                s=self.getResult(s[0],s[1],intarr[start][0],intarr[start][1])
                start+=1
            elif expression[i] == '+':
                s = self.getResult(s[0], s[1], intarr[start][0], intarr[start][1])
                start += 1
            elif expression[i]=='-':
                s=self.getResult(s[0],s[1],-intarr[start][0],intarr[start][1])
                start+=1
        return str(s[0])+"/"+str(s[1])

solve=Solution()
expression = "-1/2+1/2+1/3"
# expression = "-1/2+1/2"
# expression = "1/3-1/2"
expression="-5/2+10/3+7/9"
result=solve.fractionAddition(expression)
print(result)