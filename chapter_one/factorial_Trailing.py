class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n // 5 
            count += n
        return count

sol = Solution()
result=sol.trailingZeroes(24)
print(result)