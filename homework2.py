#Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N
def fact(number):
    res = 1
    for n in range(1, number + 1):
        res *= n
    return res
def zadacha1():
    number = int(input('Введите число: '))
    for n in range(1, number+1):
        print(f'{n}! = {fact(n)}')
zadacha1()

#zadacha2
def zadacha2():
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                print(f'{x} | {y} | {z} | {int(not(x and y) and z)}')
zadacha2()

#zadacha 3
def zadacha3():
    word = 'one'
    phrase = 'onetwonine'
    used = []
    for el in word:
        count = 0
        if not el in used:
            for letter in phrase:
                if letter == el:
                    count += 1
            print(f'{el} - {count}')
        else:
            print(f'{el} уже встречался')
zadacha3()

#zadacha4
def zadacha4():
    length = int(input('Введите число: '))
    length = abs(length)
    numbers = []
    for num in range(-length, length+1):
        numbers.append(num)
    print(numbers)

    step = 2
    
    res = numbers[:-step] + numbers[- step:]
    print(res)
    
zadacha4()