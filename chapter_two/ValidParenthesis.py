class Solution:
    def isValid(self, s: str) -> bool:
        store=[]
        stack={'(':')','{':'}','[':']'}
        for i in s:
            if i in stack:
                store.append(i)
            elif i in stack.values():
                if not store or stack[store.pop()]!= i:
                    return False
        return not store

sol=Solution()
result=sol.isValid("[]")
print(result)
        