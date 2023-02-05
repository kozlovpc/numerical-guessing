import random

n = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')


def is_valid(a):
    if a.isdigit() == True:
        return True
    else:
        return False


while True:
    a = input()
    is_valid(a)
    if is_valid(a) == True:
        a = int(a)
        if a == n:
            print('Вы угадали,поздравляем')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        elif a < n:
            print('Ваше число меньше загаданного,попробуйте ещё раз')
        elif a > n:
            print('Ваше число больше загаданного,попробуйте ещё раз')
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
