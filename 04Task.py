#  Пользователь вводит целое положительное число.
while True:
    int_var = int(input('Прошу ввести целое положительное число:'))
    if int_var < 0:
        print('Введено отрицательное число!')
        continue
    elif 0 < int_var <= 9:
        res_num = int_var
        break
    else:
        left_num=0
        while int_var // 10 != 0:
            last_num = int_var % 10
            int_var = int_var // 10
            next_num = int_var % 10
            if left_num < last_num > next_num:
                left_num = last_num
            elif left_num < next_num:
                left_num = next_num
        else:
            break
#  Найдите самую большую цифру в числе.
print(f'Самая большая цифра = {left_num}')
#  Для решения используйте цикл while и арифметические операции.
