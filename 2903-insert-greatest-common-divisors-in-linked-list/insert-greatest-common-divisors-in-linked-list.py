# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        proxy_head = head
        while (proxy_head.next):
            tempNode = ListNode()
            tempNode.val = gcd(proxy_head.val, proxy_head.next.val)
            tempNode.next = proxy_head.next
            proxy_head.next = tempNode
            proxy_head = tempNode.next
        return head
