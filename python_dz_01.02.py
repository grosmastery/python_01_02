import random


'''
1. Дано целое число (int). Определить сколько нулей в этом числе.
'''

int_number = 10020030040
int_to_str = str(int_number)
print(int_to_str.count('0'))

##############################

'''
2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
'''

int_number = 10202000000
int_to_str = str(int_number)[::-1]
count = 0
for zero in int_to_str:
    if zero == '0':
        count += 1
    else:
        break
print(count)

##############################

'''
3. Даны списки my_list_1 и my_list_2.
Создать список my_result в который вначале поместить
элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
'''

my_list_1 = [random.randint(0, 100) for _ in range(11)]
my_list_2 = [random.randint(0, 100) for _ in range(10)]
my_result = []
print(my_list_1)
print(my_list_2)
for even in my_list_1[::2]:
    my_result.append(even)
for uneven in my_list_2[1::2]:
    my_result.append(uneven)
print(my_result)

###############################

'''
4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
'''

my_list = [random.randint(0, 10) for _ in range(5)]
new_list = []
for other in my_list[1:]:
    new_list.append(other)
for one in my_list[:1]:
    new_list.append(one)
print(my_list)
print(new_list)

##############################

'''
5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
[1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
'''

my_list = [random.randint(0, 5) for _ in range(4)]
print(my_list)
for idx, first in enumerate(my_list):
    if idx == 0:
        break
my_list.pop(0)
my_list.append(first)
print(my_list)

##############################

'''
6. Дана строка в которой есть числа (разделяются пробелами).
Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
Для данного примера ответ - 133. (используйте split и проверку isdigit)
'''

str_1 = '30 больше чем 20 но меньше чем 50'.split()
result = 0
for num in str_1:
    if num.isdigit():
        num = int(num)
        result += num
    else:
        continue
print(result)

#############################

'''
7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
'''

my_str = 'My long string'
l_limit = 'o'
r_limit = 'g'
sub_str = ('')
l_idx = my_str.index(l_limit)
r_idx = my_str.rindex(r_limit)
sub_str = my_str[l_idx + 1:r_idx]
print(sub_str)

##############################

'''
8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
(используйте срезы длинны 2)
'''

my_str = 'abcde'
my_list = []
for idx in range(len(my_str)):
    if idx == len(my_str) - 1:
        if len(my_str) % 2 != 0:
            my_list.append(my_str[-1] + '_')
    elif idx % 2 == 0:
        my_list.append(my_str[idx:idx+2])
print(my_list)

##############################

'''
9. Дан список чисел. Определите, сколько в этом списке элементов,
которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
'''

my_list = [random.randint(0, 10) for _ in range(9)]
print(my_list)
# my_list = [2,4,1,5,3,9,0,7]
count = 0
for idx in range(len(my_list)):
    if idx == len(my_list) - 1:
        break
    elif idx == 0:
        continue
    if my_list[idx] > my_list[idx-1] + my_list[idx+1]:
        count += 1
print(count)
