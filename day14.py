s = "pqpqs"
k = 2
# s = "aabacbebebe"
# k = 3
# s = "a"
# k = 1
# s = "abc"
# k = 3
# s = "abc"
# k = 2
count = {}
left = 0
res1 = 0
for right in range(len(s)):
    count[s[right]] = count.get(s[right], 0) + 1
    while len(count) > k:
        count[s[left]] -= 1
        if count[s[left]] == 0:
            del count[s[left]]
        left += 1
    res1 += (right - left + 1)

count = {}
left = 0
res2 = 0
for right in range(len(s)):
    count[s[right]] = count.get(s[right], 0) + 1
    while len(count) > k-1:
        count[s[left]] -= 1
        if count[s[left]] == 0:
            del count[s[left]]
        left += 1
    res2 += (right - left + 1)

print(res1 - res2)
