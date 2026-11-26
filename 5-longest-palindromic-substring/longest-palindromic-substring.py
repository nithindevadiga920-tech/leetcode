class Solution:
    def longestPalindrome(self, s: str) -> str:
        lpa=''
        for j in range(len(s)):
            for i in range(j,len(s)):
                sub=s[j:i+1]
                if sub==sub[::-1] and len(sub)>len(lpa):
                    lpa=sub
        return lpa