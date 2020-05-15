import codecs

with codecs.open('text_3.txt', 'r', 'utf_8_sig') as my_file:
    dict_data = {}
    s_name = []  # sur_name < 20000
    salary = []  # value
    for i in my_file:
        key, value = i.split()
        dict_data[key] = value
        if float(value) < 20000:
            s_name.append(key)
            salary.append(float(value))
        else:
            salary.append(float(value))
        averege = sum(salary) / len(salary)

    print(f'Salary less then 20k.: {s_name}\nAverege salary: {averege} $')
