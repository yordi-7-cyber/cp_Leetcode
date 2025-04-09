class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums))!=len(nums):
            return True
        else:
            return False
sol=Solution()
result=sol.containsDuplicate([1,2,3,1])
print(result)

        