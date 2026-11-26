class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=''
        for i in s:
            if i.isalpha() or i.isdigit():
                s1+=i
        if s1.lower()==s1[::-1].lower():
            return True
        else:
            return False