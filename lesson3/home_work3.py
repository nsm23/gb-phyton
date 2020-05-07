def my_func(arg_1, arg_2, arg_3):
    if arg_1 >= arg_2 > arg_3:
        return sum([arg_1, arg_2])
    elif arg_1 > arg_2 <= arg_3:
        return sum([arg_1, arg_3])
    else:
        return sum([arg_2, arg_3])


print('The sum of 2 max numbers out of 3')
print(
    f'Result - {my_func(int(input("enter arg_1: ")), int(input("enter arg_2: ")), int(input("enter arg_3: ")))}')
