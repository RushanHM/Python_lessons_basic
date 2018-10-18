# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    int_part = number // 1
    decimal_part = number % 1
    unround_p = decimal_part * 10**ndigits
    round_p = unround_p % 1
    addit = round_p * 2 // 1

    return int_part + ((unround_p + addit) // 1 / 10**ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    sum_ = 0
    num = str(ticket_number)

    if len(num) != 6:
        return 'Err'

    l_part = num[:3]
    r_part = num[3:]

    for idx in range(3):
        sum_ += int(l_part[idx])
        sum_ -= int(r_part[idx])

        if sum_ == 0:
            return True

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
