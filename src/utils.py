from datetime import datetime
import json

executed_count = 5
data = 'operations.json'

def get_info(data):
    with open(data, encoding='UTF-8') as file:
        content = json.loads(file.read()) #Строковое представление файла
    return content

def get_info_fiter():
    info = []
    for i in get_info(data):
        for v in i.values():
            if v == "EXECUTED":
                info.append(i)
    return info

def get_sorted_list():
    sorted_list = sorted(get_info_fiter(), key=lambda x: x['date'], reverse=True)
    top_5 = sorted_list[0:executed_count]
    return top_5

def format_operation(data):
        if data['description'] == 'Открытие вклада':
                from_bank = ''
                from_card = ''
        else:
                if data['from'][0:4] == 'Счет':
                        from_bank = "Счет"
                        from_card = f"{'**'} {data['to'][-4:]}"
                else:
                        card = data['from'][(len(data['from']) - 16):len(data['from'])]
                        from_bank = data['from'][0:(len(data['from']) - 16)]
                        from_card = f"{card[0:4]} {card[4:6]}{'** ****'} {card[-4:]}"

        description = data['description']
        v = data['date'][0:10].replace('-','.')
        date_1 = datetime.strptime(v, "%Y.%m.%d")
        date_format = date_1.strftime("%d.%m.%Y")
        to = f" -> Счет {'**'} {data['to'][-4:]}"
        amount = data['operationAmount']['amount']
        currency = data['operationAmount']['currency']['name']

        return (f'{date_format} {description}\n' 
                f'{from_bank} {from_card} {to}\n'
                f'{amount} {currency}\n')

