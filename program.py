# 2^24+4^34-5

print('''
Всем привет
Это моя программа
''')
numbers = '0123456789'
k = 0
print('Выражение:')
example = input()
answer = 0
operation = True

while k < len(example):
    # Первое число
    n1 = ''
    while k < len(example) and example[k] in numbers:
        n1 += example[k]
        k += 1
    # если это последнее число без степени
    if k == len(example):
        if operation:
            answer += int(n1)
        else:
            answer -= int(n1)
    else:
        # Если дальше степень
        if example[k] == '^':
            k += 1
            n2 = ''
            while k < len(example) and example[k] in numbers:
                n2 += example[k]
                k += 1
            if operation:
                answer += int(n1)**int(n2)
            else:
                answer -= int(n1) ** int(n2)
        # если дальше арифм операция
        if k < len(example) and example[k] == '+':
            operation = True
        else:
            operation = False
    k = k + 1
print(answer)


num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
print('Система счисления:')
ss = int(input())
s = ''
while answer >= ss:
    p = answer % ss
    answer = answer // ss
    s += num[p]
s += num[answer]
print(s[::-1])
