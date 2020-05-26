class Date:
    def __init__(self, data):
        self.data = data.split('-')
    """
        @staticmethod
        def verify(data)
            data = [int(i) for i in data.split('-')]
                if 1 <= int(data[0]) <= 31:
                    if 1 <= int(data[1]) <= 12:
                        if 1147 <= int(data[2]) <= 2020:
                            return f'Всё ок! - {data}'#{day, month, year}
                        else:
                            return "Проверьте год."
                    else:
                        return 'Проверьте месяц.'
                else:
                    return 'Проверьте день.'
            print(Date.verify('25-15-2020'))
    """

    @staticmethod
    def verify(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and 1147 <= year <= 2020:
            return f'Всё ок! - {day, month, year}'
        else:
            return "Проверьте правильность ввода даты."

    @classmethod
    def date_type(cls, data):
        data = [int(i) for i in data.split('-')]
        return f'{data}:\nday - {data[0]}\nmonth - {data[1]}\nyear - {data[2]}'


print(Date.verify(25, 15, 2020))
print()
print(Date.date_type('25-05-2020'))




