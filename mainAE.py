class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = [-1] * 256  # Array to store last seen indices
        length, right, left = 0, 0, 0
        n = len(s)

        while right < n:
            # If the character has been seen, adjust the left pointer
            if map[ord(s[right])] != -1:
                left = max(map[ord(s[right])] + 1, left)
            # Update the last seen index
            map[ord(s[right])] = right
            # Calculate the length of the current window
            length = max(length, right - left + 1)
            right += 1
        return length