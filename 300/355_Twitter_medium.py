'''
355. 设计推特
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近 10 条推文。

实现 Twitter 类：

Twitter() 初始化简易版推特对象
void postTweet(int userId, int tweetId) 根据给定的 tweetId 和 userId 创建一条新推文。每次调用此函数都会使用一个不同的 tweetId 。
List<Integer> getNewsFeed(int userId) 检索当前用户新闻推送中最近  10 条推文的 ID 。新闻推送中的每一项都必须是由用户关注的人或者是用户自己发布的推文。推文必须 按照时间顺序由最近到最远排序 。
void follow(int followerId, int followeeId) ID 为 followerId 的用户开始关注 ID 为 followeeId 的用户。
void unfollow(int followerId, int followeeId) ID 为 followerId 的用户不再关注 ID 为 followeeId 的用户。


示例：

输入
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
输出
[null, null, [5], null, null, [6, 5], null, [5]]

解释
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // 用户 1 发送了一条新推文 (用户 id = 1, 推文 id = 5)
twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含一个 id 为 5 的推文
twitter.follow(1, 2);    // 用户 1 关注了用户 2
twitter.postTweet(2, 6); // 用户 2 发送了一个新推文 (推文 id = 6)
twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含两个推文，id 分别为 -> [6, 5] 。推文 id 6 应当在推文 id 5 之前，因为它是在 5 之后发送的
twitter.unfollow(1, 2);  // 用户 1 取消关注了用户 2
twitter.getNewsFeed(1);  // 用户 1 获取推文应当返回一个列表，其中包含一个 id 为 5 的推文。因为用户 1 已经不再关注用户 2


提示：

1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
所有推特的 ID 都互不相同
postTweet、getNewsFeed、follow 和 unfollow 方法最多调用 3 * 104 次
'''

from collections import defaultdict


class Node:
    def __init__(self, tweetId, time):
        self.tweetId = tweetId
        self.time = time


class Twitter:

    def __init__(self):
        self.followU = defaultdict(set)
        self.followT = defaultdict(list)
        self.time = 0

    def hebing(self, l1, l2):
        if not l2:
            return l1
        if not l1:
            return l2
        left1 = left2 = 0
        ans = []
        while left1 < len(l1) and left2 < len(l2):
            if l1[left1].time > l2[left2].time:
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

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followT[userId] = [Node(tweetId, self.time)] + self.followT[userId]
        self.time += 1
        if len(self.followT[userId]) > 10:
            self.followT[userId].pop()

    def getNewsFeed(self, userId: int):
        followList = self.followU[userId].union(set([userId]))
        ans = []
        for i in followList:
            ans = self.hebing(ans, self.followT[i])
        return [i.tweetId for i in ans]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followU[followerId] = self.followU[followerId].union(set([followeeId]))

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # self.followU[followerId].pop(followeeId)
        if followeeId in self.followU[followerId]:
            self.followU[followerId].remove(followeeId)


twitter = Twitter()
# twitter.postTweet(1, 5)
# print(twitter.getNewsFeed(1))
# twitter.follow(1, 2)
# twitter.postTweet(2, 6)
# print(twitter.getNewsFeed(1))
# twitter.unfollow(1, 2)
# print(twitter.getNewsFeed(1))
# ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
# [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
# twitter.postTweet(1, 5)
# print(twitter.getNewsFeed(1))
# twitter.follow(1, 2)
# twitter.postTweet(2, 6)
# print(twitter.getNewsFeed(1))
# twitter.unfollow(1, 2)
# print(twitter.getNewsFeed(1))

# ["Twitter","postTweet","postTweet","unfollow","getNewsFeed"]
# [[],[1,4],[2,5],[1,2],[1]]
# twitter.postTweet(1, 4)
# twitter.postTweet(2, 5)
# twitter.unfollow(1, 2)
# print(twitter.getNewsFeed(1))
#
# ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
# [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))
#
# ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed"]
# [[],[1,5],[1,3],[1,101],[1,13],[1,10],[1,2],[1,94],[1,505],[1,333],[1,22],[1,11],[1]]
# twitter.postTweet(1, 5)
# twitter.postTweet(1, 3)
# twitter.postTweet(1, 101)
# twitter.postTweet(1, 13)
# twitter.postTweet(1, 10)
# twitter.postTweet(1, 2)
# twitter.postTweet(1, 94)
# twitter.postTweet(1, 505)
# twitter.postTweet(1, 333)
# twitter.postTweet(1, 22)
# twitter.postTweet(1, 11)
# print(twitter.getNewsFeed(1))
