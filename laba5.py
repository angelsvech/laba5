import random


def z1():
    ch = []
    for i in range(5):
        ch.append(random.randint(1, 50))
    a = int(input("введите число: "))
    if a in ch:
        print("Поздравляю, Вы угадали число")
    else:
        print("Нет такого числа!")


def z2():
    sp = []
    for i in range(10):
        sp.append(random.randint(1, 10))
    if sp.count(i) > 1:
        print(sp.count(i))
    else:
        print("нет повторяющихся")


def z3():
    week = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
    a = int(input("введите колличество выходных"))
    b = 7 - a
    print("ваши выходные дни:", week[b:])
    print("ваши рабочии дни:", week[0:b])


def z4():
    md4 = ["Иванов", "Смирнов", "Иванов", "Кузнецов", "Соколов", "Попов", "Лебедев", "Козлов", "Новиков", "Морозов",
           "Петров"]
    md5 = ["Волков", "Соловьев", "Васильев", "Зайцев", "Павлов", "Семенов", "Лебедев", "Голубев", "Виноградов",
           "Богданов", "Воробьев"]
    team4 = random.sample(md4, 5)
    team5 = random.sample(md5, 5)
    team = team4 + team5
    print("МД-4:", md4, "МД-5", md5, "команда", team)
    alf=list(team)
    alf.sort()
    print(team)
    print("колличество", len(team))
    ivanov="Иванов"
    if ivanov in team:
        print("Иванов есть в команде", team.count("Иванов"))
    else:
        print("Иванов нет в команде")
z4()
