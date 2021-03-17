
#задаю для теста свой рандомный массив
new = 11111111111111111111000000000000000000000000000000000000
test = list(str(new))
#исхожу из того, что первый индекс - 0, как и положено

def task_1(test):
    x = 0
    for i in test:
        if i == '1':
            x += 1
        else:
            break
    return x

print(task_1(test))

# этот алгоритм может затратить больше времени, чем хотелось бы
# а если первый 0 в конце? а если в массиве миллион единиц подряд? проверять каждую?
# пробуем бинарный поиск (O(log n)) вместо O(n)

def task_2(test, left, right):
    while not right - left == 1:
        mid = int((left + right) / 2)
        if int(test[mid]) == 0:
            right = mid
        else:
            left = mid
    return right

print(task_2(test, 0, len(test) - 1))

#индексы совпадают, можем проверить по pytest:
#import pytest
#def equals():
#   assert task_1(test) == task_2(test, 0, len(test) - 1)

# как проверить непосредственно правильность? создаем еще одну функцию

def testing(test):
    z = task_1(test)
    x = int(test[z])
    y = int(test[z - 1])
    print ([x, y])

testing(test)

#доказали, что индекс -  правильный, а цифра на индекс раньше - как раз единица