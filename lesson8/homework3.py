class MyError(Exception):
    def __init__(self, text):
        self.text = text

class MyNumbers:
        def __init__(self):
            self.my_list = []

        def in_num(self):
            while True:
                try:
                    try:
                        el = int(input('Enter a numbers: '))
                        self.my_list.append(el)
                        print(f'List of numbers: {self.my_list}')
                    except ValueError:
                        raise MyError('ENTER A NUMBER(1,2,3,4...)')
                except MyError:
                    el = input('Want to continue? (y) or (n): ')
                    if el == 'N' or el == 'n':
                        print(f'Final list: {self.my_list}')
                        break
                    else:
                        self.in_num()


a = MyNumbers()
a.in_num()
