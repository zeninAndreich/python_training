

a = 'on'
b = 'and'
c = 'one'

text = f"""Lannister, Targaryen, Baratheon, Stark, Tyrell...
they\'re all just spokes {a} a wheel.
This {c}'s {a} top, then {c}'s {a} top, {b} {a} {b} {a} it spins,
crushing those {a} the ground.
"""

print(text)

text = '''Lannister, Targaryen, Baratheon, Stark, Tyrell...
they're all just spokes on a wheel.
This one's on top, then that one's on top, and on and on it spins,
crushing those on the ground.

'''

print(text)


#Задание Выведите на экран результат выражения:
# 7 - (-8 - -2). Попробуйте сделать число 7 не числом, а строкой.
# Поэкспериментируйте с другими числами тоже.


one = 'Naharis'
two = 'Mormont'
three = 'Sand'


test = (f'{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}')
print(test)
test1 = (f'{one} {two}')
print(test1)
print(f'{one},{three}')
print(f'{test1},{one},{two}')



value = 2.9

# BEGIN (write your solution here)
value = str(2)
print(f'{value} time')
# END

text = 'Never forget what you are, for surely the world will not'

# BEGIN (write your solution here)
result = f'First: {text[0]}\nLast: {text[-1]}'
print(result)
# END

# imports are studied on Hexlet

from random import random

# BEGIN (write your solution here)
result=(random()*10)
resalt2=round(result)
print(resalt2)
# END


print("В лесу родилась елка".upper())

twow= 'Nom'

print(twow.replace('om', 'two'))

print("Gonson".replace('on', 'two'))


print(f'Мартышка к старости слаба глазами стала \nА у людей она слыхала,'
      f'\nЧто это зло еще не так большой руки:'
      f'\nЛишь стоит завести Очки.'.replace('Мартышка', 'Обезьяна'))


text = 'a MIND needs Books as a Sword needS a WHETSTONE.'

result = text.lower()
print(result)


text = 'Never forget what you are, for surely the world will not'


print("Index Of N:" + str(text.find("N")) +"\n" +"Index Of ,:" + str(text.find(",")))


