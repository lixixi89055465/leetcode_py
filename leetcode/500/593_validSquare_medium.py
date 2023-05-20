'''
593. 有效的正方形
给定2D空间中四个点的坐标 p1, p2, p3 和 p4，如果这四个点构成一个正方形，则返回 true 。

点的坐标 pi 表示为 [xi, yi] 。输入 不是 按任何顺序给出的。

一个 有效的正方形 有四条等边和四个等角(90度角)。



示例 1:

输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
输出: True
示例 2:

输入：p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
输出：false
示例 3:

输入：p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
输出：true


提示:

p1.length == p2.length == p3.length == p4.length == 2
-104 <= xi, yi <= 104
'''
class Solution:

    def validSquare(self, p1, p2, p3, p4) -> bool:
        s12=(p1[0]-p2[0])**2+(p1[1]-p2[1])**2
        s13=(p1[0]-p3[0])**2+(p1[1]-p3[1])**2
        s14=(p1[0]-p4[0])**2+(p1[1]-p4[1])**2
        s23=(p2[0]-p3[0])**2+(p2[1]-p3[1])**2
        s24=(p2[0]-p4[0])**2+(p2[1]-p4[1])**2
        s34=(p3[0]-p4[0])**2+(p3[1]-p4[1])**2
        if s12==0 or s13==0 or s14==0 or s23==0 or s24==0 or s34==0 :
            return False
        if s12==s13:
            if s12==s13==s24==s34 and s14==s23:
                return True
        elif s12==s14:
            if s12==s14==s23==s34 and s13==s24:
                return True
        elif s13==s14:
            if s13==s14==s23==s24 and s12==s34:
                return True
        return False

solve=Solution()
# p1 = [0,0]
# p2 = [1,1]
# p3 = [1,0]
# p4 = [0,1]
# p1 = [0,0]
# p2 = [1,1]
# p3 = [1,0]
# p4 = [0,12]
# p1 = [1,0]
# p2 = [-1,0]
# p3 = [0,1]
# p4 = [0,-1]
# p1=[0,0]
# p2=[0,0]
# p3=[0,0]
# p4=[0,0]
p1=[0,0]
p2=[1,1]
p3=[0,0]
p4=[1,1]
reslut=solve.validSquare(p1,p2,p3,p4)
print(reslut)