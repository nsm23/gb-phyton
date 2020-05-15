import codecs
import json

profit = {}
pr = {}
prof = 0
p_aver = 0
i = 0
with codecs.open('text_7.txt', 'rb', 'utf_8_sig') as my_file:
    for l in my_file:
        company, corp_body, pribl, loss = l.split()
        profit[company] = float(pribl) - float(loss)
        if profit.setdefault(company) >= 0:
            prof += profit.setdefault(company)
            i += 1
    if i != 0:
        p_aver = prof / i
        print(f'Averege profit - {p_aver:.2f}')
    else:
         print('No one earned it')
    pr = {'Aver profit': round(p_aver)}
    profit.update(pr)
    print(f'Profit of each company - {profit}')
with open('ttx7.json', 'w') as my_write:
    json.dump(profit, my_write)
    js_f = json.dumps(profit)
    print(js_f)
