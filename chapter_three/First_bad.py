# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    bad = 4 
    return version >= bad
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        first_bad = n  
        while left <= right:
            mid = left + (right - left) // 2  
            if isBadVersion(mid):
                first_bad = mid
                right = mid - 1 
            else:
                left = mid + 1 
        return first_bad
sol=Solution()
result=sol.firstBadVersion(4)
print(result)