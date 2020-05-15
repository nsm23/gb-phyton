import codecs
import json

with codecs.open('text_6.txt', 'r', 'utf_8_sig') as my_file:
    my_dict = {}
    for i in my_file:
        lesson, lecture, practice, lab = i.split()
        my_dict[lesson] = lecture + practice + lab
    print(my_dict)

