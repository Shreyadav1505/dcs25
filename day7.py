# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [2, 0, 2]
# height = [5]
height = [4, 2, 0, 3, 2, 5]
# height = [1, 1, 1]

l = 0
r = len(height) - 1
lmax = 0
rmax = 0
water = 0

while l < r:
    if height[l] <= height[r]:
        if height[l] > lmax:
            lmax = height[l]
        else:
            water += lmax - height[l]
        l += 1
    else:
        if height[r] > rmax:
            rmax = height[r]
        else:
            water += rmax - height[r]
        r -= 1

print(water)
