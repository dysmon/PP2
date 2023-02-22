def generator(n):
    while n:
        yield n
        n = n - 1 

n = int(input("Enter a value for n: "))

decrease = generator(n)

print(*decrease)