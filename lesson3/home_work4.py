def my_func(x, y):
    """
    :parameter x
    :parameter y
    :return 1/ x**abs(y)
     """
    if y < 0:
        n = []
        total = 1
        for i in range(y, 0):
            n.append(x)
            total *= x
        return 1 / total
    else:
        return x ** y

print('Exponentiation')
print(f'result:  {my_func(int(input("enter x: ")), int(input("enter y: ")))}')
