def one_by_one(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def gauss_sum(n):
    sum = ((1 + n) * n) // 2
    return sum


print(2 // 3)
n = 9
print("one_by_one:", one_by_one(n))
print("gauss_sum:", gauss_sum(n))
