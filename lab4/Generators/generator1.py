def square_generator(N):
    for i in range(1, N+1):
        yield i*i

sg = square_generator(5)

for sq in sg:
    print(sq)