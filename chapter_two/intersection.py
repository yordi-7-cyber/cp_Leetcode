class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)
        return list((counts1 & counts2).elements())

sol=Solution()
result=sol.intersect([1,2,2,1],[2,2])
print(result)