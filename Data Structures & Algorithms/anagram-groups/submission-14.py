class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for string in strs:
            chars = [0] * 26 
            for c in string:
                chars[ord(c) - ord('a')] += 1 
            seen[tuple(chars)].append(string)
        
        return list(seen.values())

        