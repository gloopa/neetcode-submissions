class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left+=1
            sett.add(s[right])
            result = max(result, right - left + 1)
        return result
        