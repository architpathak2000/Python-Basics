def print_sum(*args):
    print(args)
    return sum(args)

# Numbers = tuple(map(int,input("Enter the numbers separated by space").split(" ")))
print(print_sum(1,2,3,4,5))