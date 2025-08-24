strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = [""]
strs = ["a"]
strs = ["abc", "bca", "cab", "xyz", "zyx", "yxz"]
strs =  ["abc", "def", "ghi"]
groups = {}
for word in strs:
    key = ''.join(sorted(word))
    
    if key not in groups:
        groups[key] = []
    groups[key].append(word)
    
print(list(groups.values()))
