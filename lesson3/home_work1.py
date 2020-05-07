def my_func(*args):
    num_1 = int(input('Enter first number: '))
    try:
        num_2 = int(input('Enter second number: '))
        div = num_1 / num_2
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        print('You can`t divide by zero')
        num_2 = int(input('Enter second number: '))
        return ("%.2f" % (num_1 / num_2))
    """
    if num_2 != 0:
        return num_1 / num_2
    else:
    print('You can`t divide by zero')
        enter num_2
        return num_1 / num_2
    """
    return ("%.2f" % div)

print('Dividing')
print(f'result - {my_func()}')
