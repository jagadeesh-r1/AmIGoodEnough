class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        for i in range(1, n+1):
            result.append(i)
        result.sort(key=str)
        return result
