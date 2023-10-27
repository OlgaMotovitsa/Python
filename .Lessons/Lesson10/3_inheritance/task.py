# Задание
#
# Перед вами несколько строк кода. Напишите что выведет программа, не запуская
# код. У вас 3 минуты.

class A:
    name = 'A'
    def call(self):
        print(f'I am {self.name}')


class B:
    name = 'B'
    def call(self):
        print(f'I am {self.name}')


class C:
    name = 'C'
    def call(self):
        print(f'I am {self.name}')


class D(C, A):
    pass


class E(D, B):
    pass


e = E()
e.call()
