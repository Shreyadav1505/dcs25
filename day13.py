s = "babad"
s = "abc"
s = "aaaa"
s = "a"
s = "cbbd"

if not s or len(s) == 1:
    print(s)
else:
    start, max_len = 0, 1
    
    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
    
    print(s[start:start + max_len])
