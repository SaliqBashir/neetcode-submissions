class Solution:
    def isValid(self, s: str) -> bool:
        openingSets = ['(', '[', '{']

        sets = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        stack = []

        for i in range(len(s)):
            if s[i] in openingSets:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if sets[s[i]] != stack.pop():
                    return False
        return len(stack) == 0