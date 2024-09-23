class Solution:
    def climbStairs(self, n):
        if n <= 3:
            return n
        ways = [0,1,2,3]
        for i in range(4, n+1):
            ways.append(ways[i-1] + ways[i-2])
        return ways.pop()
