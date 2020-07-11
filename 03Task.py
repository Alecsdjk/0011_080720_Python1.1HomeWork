# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
var_num = int(input("Введите число:"))
var_num = var_num + int(str(var_num) +
                        str(var_num)) + int(str(var_num) + str(var_num) + str(var_num))
print(f'Результат сложения введенного числа n + nn + nnn = {var_num}')
