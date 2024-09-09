# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         m = len(matrix)
#         n = len(matrix[0])
#         result = []
#         i = 0
#         while (i < m):
#             for j in range(i, n):
#                 print(matrix[i][j],"1")
#                 result.append(matrix[i][j])
#             # print(i,j, m, n)
#             # if i + 1 > m - 1 or j == n:
#             #     break
#             for x in range(i + 1, m):
#                 print(matrix[x][j],"2")
#                 result.append(matrix[x][j])
#             # if i == 0 and j == 0:
#             #     break
#             for y in range(j, i, -1):
#                 print(matrix[x][y - 1],"3")
#                 result.append(matrix[x][y - 1])

#             for k in range(m - 1, i + 1, -1):
#                 print(matrix[k - 1][y - 1],"4")
#                 result.append(matrix[k - 1][y - 1])

#             i += 1
#             m -= 1
#             n -= 1
#             # print("*******************",i, m)
#         return result
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        direction = 1
        i, j = 0, -1
        result = []
        while m * n > 0:
            for x in range(n):
                j += direction
                result.append(matrix[i][j])
            m -= 1
            for x in range(m):
                i += direction
                result.append(matrix[i][j])
            n -= 1
            direction *= -1
        return result
