class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s)==0:
            return t
        for i in t:
            if i not in s:
                return i
            if s.count(i)!=t.count(i):
                return i