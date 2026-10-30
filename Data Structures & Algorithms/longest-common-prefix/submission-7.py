class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first = strs[0]

        for i, char in enumerate(first):
            for word in strs[1:]:
                if i >= len(word) or char != word[i]:
                    return first[:i]
        
        return first

