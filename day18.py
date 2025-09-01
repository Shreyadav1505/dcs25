# N = 18
# N = 12
# N = 29
N = 100
# N = 1
# N = 997
count = 0
i = 1
while i * i <= N:
    if N % i == 0:
        if i * i == N:
            count += 1
        else:
            count += 2
    i += 1
print(count)
