class Solution:
    from collections import deque
    def characterReplacement(self, s: str, k: int) -> int:
        maxWindow = 0
        window = deque()
        count = Counter(window)
        for char in s:
            window.append(char)
            if len(window) > 0:
                while (len(window) - (Counter(window).most_common(1)[0][1])) > k:
                    window.popleft()
            maxWindow = max(maxWindow, len(window))
        return maxWindow