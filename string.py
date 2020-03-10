# Экранирование строк 
print('C:\some\name')  #  \n не экранируется
#C:\some
#ame
print(r'C:\some\name')  # \n экранируется
#C:\some\name

# Форматирование строк
word = 'форматированием'

str1 = f'строка с {word}' # строка с форматированием
str2 = 'строка с {} .format'.format(word) # строка с форматированием .format


