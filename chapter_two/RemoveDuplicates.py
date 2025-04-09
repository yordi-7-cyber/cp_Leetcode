class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        Duplicates=0
        for i in range(len(nums)):
            if nums[Duplicates]!=nums[i]:
                Duplicates+=1
                nums[Duplicates]=nums[i]
        return Duplicates +1
        if not nums:
            return 0
sol=Solution()
result=sol.removeDuplicates([1,1,2,1])
print(result)