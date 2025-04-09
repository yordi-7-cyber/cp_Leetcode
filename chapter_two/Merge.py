class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Now = ListNode()
        Next=Now
        
        while list1 and list2:
            if list1.val <= list2.val:
                Next.next = list1
                list1 = list1.next
            else:
                Next.next = list2
                list2 = list2.next
            Next= Next.next
        Next.next = list1 if list1 else list2
        return Now.next 
def list_to_linked_list(lst):
    Now = ListNode()
    Next = Now
    for val in lst:
        Next.next = ListNode(val)
        Next=Next.next
    return Now.next
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()
sol=Solution()
list1 = list_to_linked_list([1, 2, 4])
list2 = list_to_linked_list([1, 3, 4])
result= sol.mergeTwoLists(list1, list2)
print(result)