# Создать словарь

def add_person_data():           
    name = input('ФИО: ')
    phone_number = input('Телефон: ')
    comment = input('Комментарий: ')
    data = open('phonebook.txt', 'a', encoding='utf-8')
    data.writelines(f'{name} ; {phone_number}; {comment}\n')
    print('Данные добавлены') 
    data.close()

def search_data_in_phonebook():     
    look_for = input('Что ищем?: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if look_for in line.lower():
                print(line)    
                   
def print_phonebook():       
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)

def change_data():
    with open('phonebook.txt', 'r+', encoding='utf-8') as data:
        text = data.read()
        current_data = input('введите данные, которые хотите изменить: ')
        new_data = input('Введите новые данные: ')
        text = text.replace(current_data, new_data)
        data.seek(0)     
        data.write(text) 
        data.truncate()
        print('Данные изменены') 

def delete_line():   
    data_to_delete = input('Что хотите удалить?: ')
    with open('phonebook.txt', 'r+', encoding='utf-8') as data:
        lines = data.readlines()      

    with open('phonebook.txt', 'w', encoding='utf-8') as data_1:        
        for line in lines:
            if data_to_delete not in line:
                data_1.write(line)
        print('Данные удалены')

def import_data():     
    imp_phonebook = input('Введите ссылку для добавления данных: ')
    with open(imp_phonebook, 'r', encoding='utf-8') as data:
        with open('phonebook.txt', 'a+', encoding='utf-8') as data_1:
            for line in data:
                if line not in data_1.readlines():
                    data_1.write(line)
            data_1.write('\n')
        print('Данные импортированы')

def export_data():      
    exp_phonebook = input('Введите ссылку: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data_1:
        with open(exp_phonebook, 'a+', encoding='utf-8') as data:
            for line in data_1:
                if line not in data.readlines():
                    data.write(line)
            data.write('\n')
        print('Данные экспортированны.')
     
print('''Меню:
1 - Добавить запись 
2 - Поиск 
3 - Посмотреть все контакты 
4 - Изменить запись
5 - Удалить запись
6 - Импортировать в файл
7 - Экспортировать из файла
''')

action = int(input('Выберите действие 1-7: '))
if action == 1:
    add_person_data()
elif action == 2:
    search_data_in_phonebook()
elif action == 3:
    print_phonebook()
elif action == 4:
    change_data()
elif action == 5:
    delete_line()
elif action == 6:
    import_data()
elif action == 7:
    export_data()
else:
    print('Неверный ввод')