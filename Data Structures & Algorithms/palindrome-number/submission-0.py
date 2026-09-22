class Solution:
    def isPalindrome(self, x: int) -> bool:
        strInt = str(x)
        if strInt == strInt[::-1]:
            return True
        else:
            return False
        