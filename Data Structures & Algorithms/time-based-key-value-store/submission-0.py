class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = [[value, timestamp]]
        else:
            self.mapping[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        ans = self.mapping[key]
        low = 0
        high = len(ans) - 1
        res = ""
        while low <= high:
            mid = low + (high - low) // 2
            if ans[mid][1] <= timestamp:
                res = ans[mid][0]
                low = mid + 1
            elif ans[mid][1] > timestamp:
                high = mid - 1
        return res