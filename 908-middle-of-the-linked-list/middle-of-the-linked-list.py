# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        temp = head
        while(True):
            if (head.next):
                values.append(head.val)
                head = head.next
            else:
                values.append(head.val)
                break

        for i in range(len(values)//2):
            temp = temp.next
        return temp
