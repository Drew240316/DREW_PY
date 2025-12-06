def print_numbers(a, *args):
    print(a)
    print(args)

print_numbers(1,20,30,40,500)


def print_numbers(a, *args):
    print(a)
    print(*args)

print_numbers(1,10,20,30)