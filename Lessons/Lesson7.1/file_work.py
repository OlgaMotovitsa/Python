# Работа с файлами
# Рассмотрим базовые операции по работе с файлами как с отдельными объектами.

# ● Переименование файлов
# Переименование файла подразумевает сохранение неизменным файла в файловой
# таблице и в содержимом файла, но изменение его имени. Для переименования
# можно воспользоваться следующим кодом.

import os
# from pathlib import Path

# os.rename('old_name.py', 'new_name.py')

# p = Path('old_file.py')
# p.rename('new_file.py')

# Path('new_file.py').rename('newest_file.py')

# Функция rename принимает на вход два обязательных аргумента — исходное имя
# файла и новое имя. Важно чтобы файл существовал, а новое имя не было занято.
# Модуль pathlib позволяет сделать переименование через создание экземпляра
# класса Path с указанием исходного файла. А затем вызов метода rename задаёт
# новое имя. При этом операции могут быть объединены в одну строку через
# точечную нотацию и без явного сохранения экземпляра класса в переменной.
# ------------------------------------------------------------

# ● Перемещение файлов
# Перемещение файла подразумевает изменение его позиции в каталоге файловой
# системы. В процессе перемещения файл может быть переименован.

# import os
# from pathlib import Path

# os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'new_name.py'))

# old_file = Path('new_name.py')
# new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)

# Для исходного файла явно не указывали директорию, где он расположен. При
# переносе была указана текущая директория как отправная точка. Оба варианта
# имеют одинаковый эффект.
# Также при работе через os мы присвоили файлу новое имя. А при использовании
# модуля pathlib указали, что после переноса файл должен сохранить старое имя.
# ---------------------------------------------------------------------

# ● Копирование файлов
# Для копирования файлов лучше всего подходит модуль shutil, который
# предоставляет ряд высокоуровневых операций.

# import shutil
#
# shutil.copy('one', 'dir')
# shutil.copy2('two', 'dir/one_more.txt')

# Функции copy и copy2 работают схожим образом. Они принимают файл для
# копирования и целевой каталог. Если такого каталога не существует, функция
# попытается присвоить копируемому файлу имя “цели”.
# Отличие состоит в том, что функция copy2 помимо содержимого файла пытается
# скопировать и связанные с ним метаданные например фотка с геоданными - неоданные тоже скопируются.
# ----------------------------------------------------------------

# Если стоит задача скопировать каталог со всем его содержимым в новое место,
# модуль предоставляет функции copytree.

# import shutil
#
# shutil.copytree('dir', 'one_more_dir')

# Функция copytree рекурсивно обходит указанный каталог и копирует его
# содержимое в новое место.
# -------------------------------------------------------------

# ● Удаление файлов
# Вариант удаления всего каталога целиком с содержимым мы уже рассматривали
# сегодня.

# import shutil
# shutil.rmtree('dir')

# Если же необходимо удалить один файл, можно воспользоваться следующими
# вариантами:

import os
from pathlib import Path

os.remove('one_more_dir/one')
Path('one_more_dir/one_more.txt').unlink()

# И функция remove и метод unlink пытаются удалить файл по указанному пути.





