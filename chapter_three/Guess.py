def guess(num: int) -> int:
    PICKED_NUMBER = 6 
    if num > PICKED_NUMBER:
        return -1
    elif num < PICKED_NUMBER:
        return 1
    else:
        return 0
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1
        return -1 
sol = Solution()
print(sol.guessNumber(10))