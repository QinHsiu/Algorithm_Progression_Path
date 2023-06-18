# 1.最长数对链，力扣646题
# 解题思路：排序+贪心
from math import inf
from itertools import pairwise
from collections import defaultdict

def findLongestChain(pairs):
    pairs.sort(key=lambda x: x[1])
    ans, cur = 0, -inf
    for l, r in pairs:
        if cur < l:
            ans += 1
            cur = r
    return ans

# 2.统计封闭岛屿数目，力扣1254
# 解题思路：DFS+并查集
def closedIsland(grid):
    def dfs(i,j):
        res= int(0 < i < m - 1 and 0 < j < n - 1)
        grid[i][j]=1
        for a,b in pairwise(dirs):
            x,y=i+a,j+b
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                res &= dfs(x, y)
        return res
    m,n=len(grid),len(grid[0])
    dirs=(-1,0,1,0,-1)
    return sum(grid[i][j] == 0 and dfs(i, j) for i in range(m) for j in range(n))
        
# 3.最长定差子序列
# 解题思路：动规+字典
def longestSubsequence(arr, difference):
    d = defaultdict(int)
    for num in arr:
        # 定差，d[4]=d[3]+1=d[2]+2=d[1]+3
        d[num] = d[num - difference] + 1
    return max(d.values())