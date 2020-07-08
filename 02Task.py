# Пользователь вводит время в секундах.
var_sec = int(input('Dear user,enter some amount of seconds:'))
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
var_hour = var_sec//3600
if var_hour < 9:
    var_hour = '0' + str(var_hour)
var_min = (var_sec%3600)//60
if var_min < 9:
    var_min = '0' + str(var_min)
var_sec = (var_sec%360)%60
if var_sec < 9:
    var_sec = '0' + str(var_sec)
print(f'Your time is: {var_hour}:{var_min}:{var_sec}')
