# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
#
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;

with open('input_data.txt', 'r') as data:
    some_string = str(data.read())
    data.close()

list_of_operators = ['-', '+', '*', '/', '(', ')']

def split_into_arifm(some_string, list_of_operators):
    operator = []
    numbers = []
    temp = ''
    for char in some_string:
        if not char in list_of_operators:
            temp+= char
        else:
            operator.append(char)
            numbers.append(int(temp))
            temp = ''
    numbers.append(int(temp))
    while (len(numbers)>1):
        if '*' in operator:
            index=operator.index('*')
            temp=parser(numbers[index], numbers[index+1], '*')
            numbers[index]=temp
        elif '/' in operator:
            index=operator.index('/')
            temp=parser(numbers[index], numbers[index+1], '/')
            numbers[index]=temp
        elif '+' in operator:
            index=operator.index('+')
            temp=parser(numbers[index], numbers[index+1], '+')
            numbers[index]=temp
        elif '-' in operator:
            index=operator.index('-')
            temp=parser(numbers[index], numbers[index+1], '-')
            numbers[index]=temp
        del (numbers[index+1])
        del (operator[index])
    return numbers[0]

def parser(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1-num2
    if operator == '*':
        return num1*num2
    if operator == '/':
        return num1/num2

print(f'{some_string} = {split_into_arifm(some_string, list_of_operators)}')
