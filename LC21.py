from typings import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1: Time = O(nlog(m+n)), space = O(m+n) -> m = len(list1), n = len(list2)
        resElements = []
        while list1:
            resElements.append(list1.val)
            list1 = list1.next
        while list2:
            resElements.append(list2.val)
            list2 = list2.next
        resElements.sort()
        head = None
        curr = None
        for x in resElements:
            newNode = ListNode(x)
            if not head:
                head = newNode
            else:
                curr.next = newNode
            curr = newNode
        return head