# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while(True):
            if (head.next):
                values.append(head.val)
                head = head.next
            else:
                if len(values) >= 1 :
                    values.append(head.val)
                else:
                    return True
                break

        if len(values) %2 == 0:
            return values[:len(values)//2] == values[len(values)//2:][::-1]
        else:
            return values[:len(values)//2+1] == values[len(values)//2:][::-1]
