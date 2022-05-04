def hebing(l1, l2):
    if not l2:
        return l1
    if not l1:
        return l2
    left1 = left2 = 0
    ans = []
    while left1 < len(l1) and left2 < len(l2):
        if l1[left1] < l2[left2]:
            ans.append(l1[left1])
            left1 += 1
        else:
            ans.append(l2[left2])
            left2 += 1
        if len(ans) == 10:
            return ans
    if left1 == len(l1):
        return ans + l2[left2:left2 + 10 - left1]
    return ans + l1[left1:left1 + 10 - left2]


    # a = [2, 6, 7, 9, 10, 12, 32, 43, 54, 65, 67, 76, 87, 90]
    # b = [1, 3, 4, 5, 11, 12, 13, 15, 34, 35, 35, 37, 39, 45]
    # print(hebing(a, b))


s1=set([1,2,3])
s2=set([3,4,5])
print(s1.union(s2))
