# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1: time = O(n), space = O(n)
        resHead = None
        current = None
        resElements = []
        while head:
            resElements.append(head.val)
            head = head.next
        resElements = resElements[::-1]
        for x in resElements:
            newNode = ListNode(x)
            if not resHead:
                resHead = newNode
                current = newNode
            else:
                current.next = newNode
                current = newNode
        return resHead

        # Approach 2: time = O(n), space = O(1)
        if not head:
            return None
        prev = None
        curr = head
        nxt = head.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
        return curr


