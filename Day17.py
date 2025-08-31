def prime_factors(N):

factors = []

while N % 2 == 0:

factors.append(2)

N //= 2

i = 3

while i i <= N:

while N % i == 0:

factors.append(i)

N //= i

i += 2

if N > 2:

factors.append(N)

return factors

#print(prime_factors(30))

#print(prime_factors(49))

#print(prime_factors(19))

#print(prime_factors(64))

print(prime_factors(123456))
