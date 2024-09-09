class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for i in range(n)]
        direction = 1
        i = 0
        j = -1
        m = n
        count = 1
        while (m * n > 0):
            for x in range(n):
                j += direction
                result[i][j] = count
                count += 1
            m -= 1
            for x in range(m):
                i += direction
                result[i][j] = count
                count += 1
            n -= 1
            direction *= -1
        return result
