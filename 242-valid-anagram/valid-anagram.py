class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(list(s)) == sorted(list(t)):
        #     return True
        # else:
        #     return False
        s_len = len(s)
        if s_len != len(t):
            return False
        hash_map = {}
        for i in range(0, s_len):
            if not hash_map.get(s[i]):
                hash_map[s[i]] = 1
            else:
                hash_map[s[i]] += 1
            if hash_map.get(t[i]) or hash_map.get(t[i]) == 0:
                hash_map[t[i]] -= 1
            else:
                hash_map[t[i]] = -1
        for i in hash_map.values():
            if i != 0:
                return False
        return True