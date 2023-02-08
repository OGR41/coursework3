import requests
from pprint import pprint
from datetime import datetime


operations_load = requests.get('https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98'
                           '-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256'
                           '=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230208%2Fus-west'
                           '-2%2Fs3%2Faws4_request&X-Amz-Date=20230208T071504Z&X-Amz-Expires=86400&X-Amz-Signature'
                           '=f2483ac8aa953b57e70ee8d0eb97ccd40598723d6153ea371feae73945be682d&X-Amz-SignedHeaders'
                           '=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject')
operations_json = operations_load.json()



def last_operations():
    executed_list = []
    for i in operations_json:
        operations_index = operations_json.index(i)
        if "state" not in i:
            continue
        elif operations_json[operations_index]['state'] == 'EXECUTED':
            executed_list.append(i)
            if "from" not in i:
                operations_json[operations_index]['from'] = "Данные об отравителе отсутствуют"

    executed_list.sort(key=lambda x: x['date'])
    last_five_operations = []
    for i in list(reversed(executed_list)):
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
                print(f'{thedate.strftime("%d.%m.%Y")} {description}\n'
                      f'{from_[0:-20] + "*" * len(from_[-6:-4]) + from_[-4:]} -> '
                      f'{to[0:-20] + "*" * len(to[-6:-4]) + to[-4:]}\n{amount} {currency}\n')
            elif 'Данные об отравителе отсутствуют' in from_:
                print(f'{thedate.strftime("%d.%m.%Y")} {description}\n'
                      f'{from_} -> {to[0:-20] + "*" * len(to[-6:-4]) + to[-4:]}\n{amount} {currency}\n')
            else:
                print(f'{thedate.strftime("%d.%m.%Y")} {description}\n'
                      f'{from_[0:-16] + from_[-16:-12] + " " + from_[-12:-10] + "*" * len(from_[-10:-8]) + " " + "*" * len(from_[-8:-4]) + " " + from_[-4:]} ->'
                      f'{to[0:-20] + "*" * len(to[-6:-4]) + to[-4:]}\n{amount} {currency}\n')


last_operations()

