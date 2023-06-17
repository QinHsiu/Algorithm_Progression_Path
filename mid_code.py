# 1.最长数对链，力扣646题
# 解题思路：排序+贪心
from math import inf
def findLongestChain(pairs):
    pairs.sort(key=lambda x: x[1])
    ans, cur = 0, -inf
    for l, r in pairs:
        if cur < l:
            ans += 1
            cur = r
    return ans