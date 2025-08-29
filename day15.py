s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = "abcdefgh"
# s = "a"
char_index = {}
left = 0
max_length = 0

for right, char in enumerate(s):
    
    if char in char_index and char_index[char] >= left:
        left = char_index[char] + 1

    char_index[char] = right
    
    max_length = max(max_length, right - left + 1)

print(max_length)
