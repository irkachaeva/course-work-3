from datetime import datetime

def format_operation(data):
        if data['description'] == 'Открытие вклада':
                from_bank = ''
                from_card = ''
        else:
                card = data['from'][(len(data['from']) - 16):len(data['from'])]
                from_card = f"{card[0:4]} {card[4:6]}{'** ****'} {card[-4:]}"
                from_bank = data['from'][0:(len(data['from']) - 16)]

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

