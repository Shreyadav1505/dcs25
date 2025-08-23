# strs = ["flower", "flow", "flight"]
# strs = ["dog", "racecar", "car"]
strs = ["apple", "ape", "april"]
# strs = [""]
# strs = ["alone"]
if len(strs) == 0:
    print("")
else:
    pre = strs[0]
    for i in range(1, len(strs)):
        comp = ""
        preq = strs[i]
        for j in range(min(len(pre), len(preq))):
            if pre[j] == preq[j]:
                comp += pre[j]
            else:
                break
        pre = comp
    print(pre)
