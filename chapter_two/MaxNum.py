class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count= 0
        for i in sentences:
            word_count = len(i.split())
            if word_count > count:
               count= word_count
        return count
sol = Solution()
result = sol.mostWordsFound(["alice and bob love leetcode","i think so too", "this is great thanks very much"])
print(result)