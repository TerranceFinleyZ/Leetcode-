class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        char_count = defaultdict(int)
        for ch in t:
            char_count[ch] += 1
        
        target_chars_remaining = len(t)
        min_window = (0, float("inf"))
        start_index = 0

        for end_index, ch in enumerate(s):
            if char_count[ch] > 0:
                target_chars_remaining -= 1
            char_count[ch] -= 1

            if target_chars_remaining == 0:
                while True:
                    char_at_start = s[start_index]
                    if char_count[char_at_start] == 0:
                        break
                    char_count[char_at_start] += 1
                    start_index += 1
                
                if end_index - start_index < min_window[1] - min_window[0]:
                    min_window = (start_index, end_index)
                
                char_count[s[start_index]] += 1
                target_chars_remaining += 1
                start_index += 1
        
        return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1]+1]