goods = []
while input('Хотите добавить товар, введите "да"? ') == 'да':
    number = int(input("Введите номер продукции: "))
    features = {'name': '', 'price': '', 'quantity': ''}
    f_name = input("Введите наименование продукции: ")
    features['name'] = f_name
    f_price = float(input('Введите стоимость продукции: '))
    features['price'] = f_price
    f_quantity = int(input('Введите количество: '))
    features['quantity'] = f_quantity
    goods.append(tuple([number, features]))
print(goods)

#analitics = {}
#for i in goods:




