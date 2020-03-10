range(5) #делает ряд чисел
range(5, 10)

#  --------------------  FOR  ---------------------  #
  
# Создание списков
list(range(5)) # [0, 1, 2, 3, 4]
list(range(5, 10)) # [5, 6, 7, 8, 9]

# Цикл по объекту range
for i in range(5):
    print(i)

# Цикл по объекту списку 
for i in [1,2,3]:
    print(i)
    
# Четные числа 
for number in range(10):
    if number % 2 == 0:
        print(number)

# Цикл по словарю(перебирает ключи)
a_dict = {"one":1, "two":2, "three":3}

for key in a_dict:
    print(key)

# Цикл по словарю(перебирает значения)
a_dict = {"one":1, "two":2, "three":3}
for key in a_dict:
    print(a_dict[key])


#  --------------------  WHILE  ---------------------  #

i = 0
while i < 10:
    print(i)
    i = i + 1

#Оператор else в циклах выполняется только в том случае, если цикл выполнен успешно.

my_list = [1, 2, 3, 4, 5]
 
for i in my_list:
    if i == 3:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")