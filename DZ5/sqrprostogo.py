def IsPrime(n):
    k = 0
    for i in range(2, n // 2 + 1):
        if (n % i == 0):
            k = k + 1
    if (k <= 0):
        return n * n
    else:
        return n
lst = [1, 3, 4, 5, 7, 8, 10, 13, 15, 17]
sqr = list(map(IsPrime, lst))
print (sqr)
input()
