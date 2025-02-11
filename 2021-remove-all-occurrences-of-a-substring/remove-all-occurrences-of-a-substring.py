class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if part not in s:
            return s
        else:
            return self.removeOccurrences(re.sub(re.escape(part), '', s, 1), part)