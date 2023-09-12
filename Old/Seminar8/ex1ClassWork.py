

file = open('phon_book.txt','r', encoding= 'UTF-8')
data = file.readlines()
file.close()

phone_book = []
for contact in data:
    new_contact = contact.strip().split(';')
    print(new_contact)
    new_contact = {'name': new_contact[0],
                    'phone': new_contact[1],
                    'comment': new_contact[2]}
    phone_book.append(new_contact)
print(phone_book)

phone_book.append({'name': 'Мотовица Ольга Васильевна', 
                        'phone': '8918000000', 
                        'comment': 'Маршал'})
print(phone_book)

new_phone_book = []
for contact in phone_book:
    new_contact = ';'.join([values for values in contact.values()]) #получили строчный контакт
    new_phone_book.append(new_contact)
print(new_phone_book)
#['Седов Андрей Павлович;8918754321;генеральный директор', 'Кожухова Марина Дмитриевна;89195647300;бухгалтер', 'Митицина Ольга Ивановна;89214777718;склад', 'Мотовица Ольга;8918000000;Маршал']

new_phone_book = '\n'.join(new_phone_book) #перенос строки
print(new_phone_book)


file = open('phon_book.txt','w', encoding= 'UTF-8')
file.write(new_phone_book)
file.close()

cont = '\nЕлена Симонова;8976543211;почта'
file = open('phon_book.txt','a', encoding= 'UTF-8') # а - добавляет в конец
file.write(cont)
file.close()


# так писать без клоуз
# with open('phon_book.txt','w', encoding= 'UTF-8') as file:
#     file.write(cont)