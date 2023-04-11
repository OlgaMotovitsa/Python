
# def add_cont():
#     file = open('Файл.txt','a', encoding= 'UTF-8')
#     surname = input("Фамилия Имя: ")  
#     phone_number = input("Телефон: ")
#     comment = input("Комментарий: ")
#     data = '\n' + surname + '; ' + phone_number + '; ' + comment 
#     file.write(data)
#     file.close()

# def read_cont():
#     file = open('Файл.txt','r', encoding= 'UTF-8')
#     data = file.readlines()
#     file.close()
#     for contact in data:
#         print(contact)
# read_cont()       
        
# def find_cont():
#     file = open('Файл.txt','r', encoding= 'UTF-8')
#     data = file.readlines()
#     file.close()
#     search_cont = input('Введите инфу для поиска: ')
#     for cont in data:
#         if search_cont.lower() in cont:
#             print(cont)
# find_cont()


def change_cont():
    phone_book = []

    file = open('Файл.txt','r', encoding= 'UTF-8')
    data = file.readlines()
    file.close()
    i = 0
    for contact in data:
        new_contact = contact.strip().split(';')
        print(new_contact)
        new_contact = {'id' : i,
                        'name': new_contact[0],
                        'phone': new_contact[1],
                        'comment': new_contact[2]}
        phone_book.append(new_contact)
        i =+1
    print(phone_book)
    elem = int(input('введите на замену id: '))
    print(phone_book[elem])






change_cont()







# phone_book.append({'name': 'Мотовица Ольга Васильевна', 
#                         'phone': '8918000000', 
#                         'comment': 'Маршал'})
# print(phone_book)













        # new_contact = contact.strip().split(';')
