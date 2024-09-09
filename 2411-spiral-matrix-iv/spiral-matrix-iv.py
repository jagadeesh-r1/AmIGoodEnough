# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1] * n for i in range(m)]
        # print(result)
        print(head.val)
        if not head:
            return result
        direction = 1
        i = 0
        j = -1
        while (m * n > 0):
            if head:
                for x in range(n):
                    j += direction
                    result[i][j] = head.val if head else -1
                    head = head.next if head else None
            m -= 1
            if head:
                for x in range(m):
                    i += direction
                    result[i][j] = head.val if head else -1
                    head = head.next if head else None
            n -= 1
            direction *= -1
        return result
