# Позиционные и ключевые параметры
# Пришло время поговорить о позиционных и ключевых параметрах функции. Начнём
# с общего синтаксиса.

def func(positional_only_parameters, /, positional_or_keyword_parameters, *,
         keyword_only_parameters):
    pass

# При указании параметров функции вначале идут позиционные параметры. При
# вызове функции передаются значения без указания имени переменной-аргумента.
# Косая черта не является переменной. Это символ разделитель. После неё могут
# 12
# идти как позиционные, так и ключевые параметры. Далее символ разделитель
# звёздочка указывает только на ключевые параметры.
# 🔥 Важно! Косая черта и звёздочка одновременно или по отдельности
# могут отсутствовать при определении функции.
# Разберем передачу аргументов по позиции и по имени на примерах.
# ● Пример обычной функции:

def standard_arg(arg):
    print(arg) # Принтим для примера, а не для привычки
standard_arg(42)
standard_arg(arg=42)
# Функция может принимать значения по позиции и по ключу. Мы явно указали имя
# переменной.
# ● Пример только позиционной функции:

def pos_only_arg(arg, /):
    print(arg) # Принтим для примера, а не для привычки
pos_only_arg(42)

# pos_only_arg(arg=42) # TypeError: pos_only_arg() got some
# positional-only arguments passed as keyword arguments: 'arg'

# Теперь функция принимает только позиционные параметры.
# ● Пример только ключевой функции:

def kwd_only_arg(*, arg):
    print(arg) # Принтим для примера, а не для привычки

# kwd_only_arg(42) #НЕЛЬЗЯ
kwd_only_arg(arg=42)

# А теперь наоборот, можем принимать только значения по ключу.
# ● Пример функции со всеми вариантами параметров:

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only) # Принтим для примера, а
# не для привычки
# combined_example(1, 2, 3) # TypeError: combined_example() takes
 # positional arguments but 3 were given         #НЕЛЬЗЯ
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) НЕЛЬЗЯ

# TypeError: combined_example() got some positional-only arguments
# passed as keyword arguments: 'pos_only'

# И наконец пример со всеми возможными вариантами параметров.
# 🔥 Важно! Если функция принимает несколько ключевых параметров,
# порядок передачи аргументов может отличаться.
def triangulation(*, x, y, z):
    pass
triangulation(y=5, z=2, x=11)
