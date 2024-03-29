# Отдельный способ создания строк — конкатенация. Или говоря проще, сложение.
# Разберём на примере и обсудим все его нюансы:

LIMIT = 120
ATTENTION = 'Внимание!'
name = input('Твоё имя? ')
age = int(input('Твой возраст? '))
text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) + \
       " до ста лет, но длинна строки не должна превышать " + str(LIMIT) + ' символов.'
print(text)
# Переменная text получилась в результате сложения нескольких строк. При этом:
# ● Все элементы должны быть строками. Иначе получим ошибку вида: TypeError:
# can only concatenate str (not "int") to str Именно для этого мы обернули
# переменные с числами, такие как LIMIT, функцией str()
# ● Если в переменной хранится строковое значение, оборачивать её в str() не
# нужно. Получится масло масляное.
# ● Складывать можно строки в одинарных, двойных и даже в трех двойных
# кавычках. Но лучше выбрать единый стиль записи строк и придерживаться
# его во всём проекте.
# ● Если код не влазит в 120 символов строки, не стесняемся использовать
# обратный слеш для его разделения на несколько строк.
# Конкатенация строк затратна по памяти и по времени. Для простых задач допустим
# подобный подход. В реальных проектах конкатенация используется для
# формирования констант. В остальных случаях используют способы форматирования
# строк. О них поговорим на следующей лекции.
# Кстати, рекомендации Google по стилю кода, которые являются продвинутой
# версией PEP-8 с дополнительными требования запрещают программистам
# использовать конкатенацию строк, особенно если она происходит внутри цикла.