class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1
        
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                'x', 'y', 'z']

        matchs = 0
        for letter in letters:
            matchs += (1 if s1Count[letter] == s2Count[letter] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matchs == 26: return True

            s2Count[s2[r]] += 1
            if s1Count[s2[r]] == s2Count[s2[r]]:
                matchs += 1
            elif s1Count[s2[r]] + 1 == s2Count[s2[r]]:
                matchs -= 1
            
            s2Count[s2[l]] -= 1
            if s1Count[s2[l]] == s2Count[s2[l]]:
                matchs += 1
            elif s1Count[s2[l]] - 1 == s2Count[s2[l]]:
                matchs -= 1
            l += 1
        return matchs == 26
