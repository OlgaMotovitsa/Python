# Методы проверки строк
# Ряд методов анализируют строку текста и возвращают истину или ложь в
# зависимости от содержимого строки. Часто используемые методы перечислены в
# таблице:
# Название метода Описание
# str.isalnum() Возвращает True, если все символы в строке
# буквенно-цифровые. Символ является
# буквенно-цифровым, если одно из следующих
# значений возвращает True: c.isalpha(), c.isdecimal(),
# c.isdigit()или c.isnumeric().
# str.isalpha() Возвращает True, если все символы в строке являются
# буквенными. Алфавитные символы — это символы,
# определенные в базе данных символов Юникода как
# «буква»
# str.isdecimal() Возвращает True, если все символы в строке являются
# десятичными символами
# str.isdigit() Возвращает True, если все символы в строке являются
# цифрами. Цифры включают десятичные символы и
# цифры, требующие специальной обработки, например
# цифры надстрочного индекса совместимости.
# str.isnumeric() Возвращает True, если все символы в строке являются
# 23
# Название метода Описание
# str.isalnum() Возвращает True, если все символы в строке
# буквенно-цифровые. Символ является
# буквенно-цифровым, если одно из следующих
# значений возвращает True: c.isalpha(), c.isdecimal(),
# c.isdigit()или c.isnumeric().
# числовыми символами. Числовые символы включают
# цифровые символы и все символы, которые имеют
# свойство числового значения Unicode
# str.isascii() Возвращает True, если строка пуста или все символы в
# строке ASCII
# str.islower() Возвращает True, если все символы в строке в нижнем
# регистре
# str.istitle() Возвращает True, если строка является строкой с
# заглавным регистром и содержит хотя бы один символ
# str.isupper() Возвращает True, если все символы в строке в
# верхнем регистре
# str.isprintable() Возвращает True, если все символы в строке доступны
# для печати или строка пуста. Непечатаемые символы
# — это символы, определенные в базе данных
# символов Unicode как «Другие» или «Разделители», за
# исключением пробела ASCII (0x20), который считается
# печатаемым.
# str.isspace() Возвращает True, если в строке есть только
# пробельные символы
