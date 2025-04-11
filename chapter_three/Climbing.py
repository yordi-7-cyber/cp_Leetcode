class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        one= [0] * (n + 1)
        one[1] = 1  
        one[2] = 2 
        for i in range(3, n + 1):
            one[i] = one[i - 1] + one[i - 2]
        return one[n]
sol=Solution()
result=sol.climbStairs(1)
print(result)  