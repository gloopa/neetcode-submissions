class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #key -> tuple of ascii freqs, ex: (1, 0, 0 1, ...)-> immutable so its valid map key (canonical key)
        #value -> list of strings in strs that have same ascii tuple (means they are the same underlying) 

        seen = defaultdict(list)

        for string in strs:
            count = [0] * 26 
            for c in string:
                count[ord(c) - ord('a')] += 1
            seen[tuple(count)].append(string)
        
        return list(seen.values())
        