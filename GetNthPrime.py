import math

t = int(input("Which prime to get?"))

primes = [2]
n = primes[-1] + 1

while len(primes) < t:
    for j in range(2, n):
        if j > math.sqrt(n):
            primes.append(n);
            n = primes[-1] + 1
            break;
        if n % j == 0:
            n += 1;
            break;

print("That prime is:", primes[-1]);
