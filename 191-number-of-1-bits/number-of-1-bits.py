class Solution:
    def hammingWeight(self, n: int) -> int:
        a=f"{n:b}"
        return a.count('1')