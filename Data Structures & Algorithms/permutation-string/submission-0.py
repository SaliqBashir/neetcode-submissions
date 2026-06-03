class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = deque()
        for char in s2:
            window.append(char)
            if len(window) > len(s1):
                window.popleft()
            if Counter(s1) == Counter(window):
                return True
        return False