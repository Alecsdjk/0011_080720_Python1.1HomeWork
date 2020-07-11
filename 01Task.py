# создайте несколько переменых
var = 0
print(f'Значение:{var},класс:{type(var)}')
var = 0.0
print(f'Значение:{var},класс:{type(var)}')
var = ''
print(f'Значение:{var},класс:{type(var)}')
var = False
print(f'Значение:{var},класс:{type(var)}')
var = None
print(f'Значение:{var},класс:{type(var)}')
# запросите у пользователя несколько чисел и строк
# и сохраните в переменные
user_name = str(input('Sign you name,please:'))
user_age = int(input('and you age:'))
user_weight = float(input('will be brave and sign you weight to:'))
print(f'Congratulation {user_name}!In this massive old galaxy '
      f'your age only {user_age} and weight less {user_age} kg')
# выведите на экран.
