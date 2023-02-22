def squares_generator(a,b):
    for i in range(a,b+1):
        yield i*i

a, b = int(input("Enter a value for a: ")), int(input("Enter a value for b: "))

sqrs = squares_generator(a,b)

for i in sqrs:
    print(i)