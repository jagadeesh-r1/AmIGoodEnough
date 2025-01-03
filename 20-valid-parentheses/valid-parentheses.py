class Solution:
    def isValid(self, s: str) -> bool:
        complements = {
            '{': '}',
            '[': ']',
            '(': ')',
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []
        for i in s:
            if i not in ['}', ']', ')']:
                stack.append(i)
                continue
            if stack:
                if stack[-1] != complements[i]:
                    return False
                stack.pop()
            else:
                return False
        return not stack