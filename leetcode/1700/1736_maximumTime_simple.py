'''
1736. 替换隐藏数字得到的最晚时间
给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。

有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。

替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。



示例 1：

输入：time = "2?:?0"
输出："23:50"
解释：以数字 '2' 开头的最晚一小时是 23 ，以 '0' 结尾的最晚一分钟是 50 。
示例 2：

输入：time = "0?:3?"
输出："09:39"
示例 3：

输入：time = "1?:22"
输出："19:22"

'''


class Solution:
    def maximumTime(self, time: str) -> str:
        result = 0
        if time[0].isdigit() == False and time[1].isdigit() == True:
            tmp = int(time[1])
            if tmp < 4:
                result = "2" + time[1]
            else:
                result = "1" + time[1]
        elif time[0].isdigit() == False and time[1].isdigit() == False:
            result = "23"
        elif time[0].isdigit() == True and time[1].isdigit() == False:
            tmp = int(time[0])
            if tmp<2:
                result = time[0] + "9"
            else:
                result = time[0] + "3"

        else:
            result = time[:2]
        # 2222222222
        if time[3].isdigit() == False and time[4].isdigit() == True:
            result+=":5"+time[4]
        elif time[3].isdigit() == False and time[4].isdigit() == False:
            result += ":59"
        elif time[3].isdigit() == True and time[4].isdigit() == False:
            result += ":"+time[3] + "9"
        else:
            result +=time[2:]
        return result

solve = Solution()
# time = "2?:?0"
# time = "0?:3?"
# time = "1?:22"
time = "?0:15"

result = solve.maximumTime(time)
print(result)
