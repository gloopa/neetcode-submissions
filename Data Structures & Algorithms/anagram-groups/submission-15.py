class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for string in strs:
            quant = [0] * 26
            for c in string:
                quant[ord(c) - ord('a')] += 1 
            hmap[tuple(quant)].append(string)
        
        return list(hmap.values())
        