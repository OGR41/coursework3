from datetime import datetime
import requests

# загружаем и сохраняем в переменную файл json
get_json = requests.get('https://www.jsonkeeper.com/b/1IUI').json()


def last_operations(json_):
    '''
    :param json_: получает данные из json-файла
    :return: список с отформатированной информацией о последних 5-ти операциях
    '''
    executed_list = []      # список с операциями по фильтрам 'state'

    for i in get_json:      # цикл для фильтрации списка по 'state'
        operations_index = get_json.index(i)
        if "state" not in i:
            continue
        elif get_json[operations_index]['state'] == 'EXECUTED':
            executed_list.append(i)
            if "from" not in i:
                get_json[operations_index]['from'] = "Данные об отравителе отсутствуют"

    executed_list.sort(key=lambda x: x['date'])     # сортируем список по дате
    last_five_operations = []       # список с последними 5-ю операциями
    a = []      # список с отформатированными операциями

    for i in list(reversed(executed_list)):     # цикл для добавления в список определённых параметров(дата, ->
                                                # -> название операции, отправитель, получатель, сумма, валюта)
        if len(last_five_operations) < 5:
            last_five_operations.append(i)
            last_five_operations_index = last_five_operations.index(i)
            thedate = datetime.fromisoformat(last_five_operations[last_five_operations_index]['date'])
            description = last_five_operations[last_five_operations_index]['description']
            from_ = last_five_operations[last_five_operations_index]['from']
            to = last_five_operations[last_five_operations_index]['to']
            amount = last_five_operations[last_five_operations_index]['operationAmount']['amount']
            currency = last_five_operations[last_five_operations_index]['operationAmount']['currency']['name']
            if 'Счет' in from_:
                a.append(f'{thedate.strftime("%d.%m.%Y")} {description}\n{from_[0:-20] + "*" * len(from_[-6:-4]) + from_[-4:]} -> {to[0:-20] + "*" * len(to[-6:-4]) + to[-4:]}\n{amount} {currency}\n')

            elif 'Данные об отравителе отсутствуют' in from_:
                a.append(f'{thedate.strftime("%d.%m.%Y")} {description}\n{from_} -> {to[0:-20] + "*" * len(to[-6:-4]) + to[-4:]}\n{amount} {currency}\n')

            else:
                a.append(f'{thedate.strftime("%d.%m.%Y")} {description}\n{from_[0:-16] + from_[-16:-12] + " " + from_[-12:-10] + "*" * len(from_[-10:-8]) + " " + "*" * len(from_[-8:-4]) + " " + from_[-4:]} -> {to[0:-20] + "*" * len(to[-6:-4]) + to[-4:]}\n{amount} {currency}\n')
    return '\n'.join(a)


print(last_operations(get_json))

