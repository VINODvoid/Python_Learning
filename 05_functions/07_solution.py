def no_of_sums(*args):
    print(args)
    for i in args:
        print(i *2)
    return sum(args)


# print(no_of_sums(2,4,5,23,1,6,8,45,2))
print(no_of_sums(2,6))