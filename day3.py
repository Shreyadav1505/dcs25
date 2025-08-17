# arr = [3,1,3,4,2]
# arr = [1,3,4,2,3]
# arr = [1,1]
# arr =[1,4,4,2,3]
arr = [1,2,3,4,5,6,7,8,9,3]

dicti = {}
for i in arr:
    if i not in dicti:
        dicti[i] = 1
    else:
        dicti[i] += 1

for key in dicti:
    if dicti[key] > 1:
        print(key)
