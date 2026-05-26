class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        s = "".join(c for c in s if c.isalnum())
        for i in range(len(s)):
            if s[i] != s[len(s)-i-1]:
                return False
            else:
                continue
        return True