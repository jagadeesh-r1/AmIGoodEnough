class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if len(set(list(s))) == len(set(list(t))):
        #     return True
        # return False
        len_s = len(s)
        if len_s != len(t):
            return False
        smap_letter = {}
        tmap_letter = {}
        for i in range(len_s):
            if not smap_letter.get(s[i]) and not tmap_letter.get(t[i]):
                smap_letter[s[i]] = t[i]
                tmap_letter[t[i]] = s[i]
            else:
                if smap_letter.get(s[i]) != t[i] or tmap_letter[t[i]] != s[i]:
                    return False
        print(smap_letter, tmap_letter)
        return True