# -*- coding: utf-8 -*-
# @Time    : 2024/9/2 下午9:06
# @Author  : nanji
# @Site    : 
# @File    : a.py
# @Software: PyCharm 
# @Comment : 
c_i = list(map(int, input().split()))
conInfo = list(map(int, input().split()))
a_list = []
b_liist = []
res_list = []
for i in range(0, len(c_i), 2):
	a_list.append([c_i[i], c_i[i + 1]])
a_list.sort(key=lambda x: x[0])

for i in range(0, len(conInfo), 2):
	b_liist.append([conInfo[i], conInfo[i + 1]])
for i in range(len(b_liist)):
	res_list.append([])

for i in range(len(a_list)):
	for j in range(len(b_liist), 0, -1):
		if b_liist[j - 1][0] <= a_list[i][0] < b_liist[j - 1][1]:
			res_list[j - 1].append(a_list[i][1])
			break

for contents in res_list:
	if len(contents) == 0:
		print('-1')
	else:
		print(" ".join(map(str, contents)))
