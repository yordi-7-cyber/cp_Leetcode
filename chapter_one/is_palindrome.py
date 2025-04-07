class Solution:
    def isPalindrome(self,S:str | int) ->bool:
        S=str(S).replace(" ","").lower()
        return S==S[::-1]

print(Solution().isPalindrome(121))
        