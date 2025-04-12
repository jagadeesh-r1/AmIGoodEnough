# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(1000)
        dummy = result
        excess = 0
        while l1 or l2 or excess:
            temp = ListNode()
            sum = excess
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next


            print(sum)
            temp.val = sum%10
            excess = sum//10
            dummy.next = temp
            dummy = dummy.next
        return result.next
            