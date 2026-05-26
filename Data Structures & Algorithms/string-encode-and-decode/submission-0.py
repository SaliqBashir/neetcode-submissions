class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append(f"{len(word)}#{word}")
        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            num = 0
            while s[i] != '#':
                num = num * 10 + int(s[i])
                i += 1
            i += 1
            words.append(s[i:i+num])
            i += num
        return words

            
