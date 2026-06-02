class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = deque()
        count = defaultdict(int)
        max_window = 0
        max_freq = 0

        for char in s:
            window.append(char)
            count[char] += 1
            max_freq = max(max_freq, count[char])
            while len(window) - max_freq > k:
                removed = window.popleft()
                count[removed] -= 1
            max_window = max(max_window, len(window))
        return max_window