import json
executed_count = 5
def get_info():
    with open('operations.json', encoding='UTF-8') as file:
        content = json.loads(file.read()) #Строковое представление файла
    return content
#print(get_info())

def get_info_fiter():
    info = []
    for data in get_info():
        for v in data.values():
            if v == "EXECUTED":
                info.append(data)
    return info
#print(get_info_fiter())

def get_sorted_list():
    sorted_list = sorted(get_info_fiter(), key=lambda x: x['date'], reverse=True)
    top_5 = sorted_list[0:executed_count]
    return top_5

#print(len(get_sorted_list()))