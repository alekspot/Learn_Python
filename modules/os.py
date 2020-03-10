import os

# Переменные окружения
###############################################################
os.environ # все переменные среды
os.getenv('OS') # получить значение переменноый среды


# Директории(Пути), создание папок, удаление файлов/папок
###############################################################
open('newFile.txt', 'tw', encoding='utf-8').close()

# текущий путь
os.getcwd()

# поменять путь 
os.chdir(r'C:\Users\aleksandr\Desktop\myPython\modules') 
os.getcwd()

# создать папку
os.mkdir("test")
os.mkdir(r'C:\Users\aleksandr\Desktop\myPython\modules\Новая папка')

# создать папки
os.makedirs(r'C:\Users\aleksandr\Desktop\myPython\modules\Новые папки\папка1\папка2\папка3\папка4')

# удаление файла
os.remove("newFile.txt")

# удаление папки
os.rmdir("test")

# переименование файла/папок
os.rename("t.txt", "pytest.txt") # работает с файлами
os.renames("pytest.txt", "t.py") # работает с файлами/папками
os.renames("test", "pytest")


# Открытие файлов программмой по умолчанию
###############################################################
def openFiles():
    os.startfile("deleteMe.txt")
    os.startfile("oneMoreFile.txt")
openFiles()
