class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        y = x[:]
        y.reverse()
        if x==y : return True
        else : return False