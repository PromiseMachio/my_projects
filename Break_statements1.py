for n in range(3,12):
    for x in range(3,n):
        if n % x == 0:
            print(f"{n} is equals to {x} * {n // x}")
            break
#Another example on the same
for n in range(2,20):
    if n % 2 == 0:
        print(f'{n} is an even number')
        continue
    print(f'{n} is an odd number')
