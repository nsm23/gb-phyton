class OwenError(Exception):
    def __init__(self, text):
        self.text = text
class DiByZ():
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def div(num_1, num_2):
        try:
            if num_2 == 0:
                raise OwenError('num_2 != 0!!!')

        except ValueError:
            return 'Enter the number.'
        except OwenError as err:
            return err
        else:
            return num_1 / num_2


a = DiByZ(100, 20)
b = DiByZ(53, 0)

print(f'num_1 / num_2 = {a.div(100, 20)}')
print(f'Error: {b.div(100, 0)}')