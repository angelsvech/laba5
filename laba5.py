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
    md4 = ["Иванов", "Смирнов", "Кузнецов", "Соколов", "Попов", "Лебедев", "Козлов", "Новиков", "Морозов",
           "Петров"]
    md5 = ["Волков", "Соловьев", "Васильев", "Зайцев", "Павлов", "Семенов", "Голубев", "Виноградов",
           "Богданов", "Воробьев"]
    team4 = random.sample(md4, 5)
    team5 = random.sample(md5, 5)
    team = team4 + team5
    print("МД-4:", md4, "МД-5", md5, "команда", team)
    alf = list(team)
    alf.sort()
    print(team)
    print("колличество", len(team))
    ivanov = "Иванов"
    if ivanov in team:
        print("Иванов есть в команде", team.count("Иванов"))
    else:
        print("Иванов нет в команде")

def z61():
    stran = {"Россия": "Москва", "США": "Вашингтон", "Китай": "Пекин"}
    print(stran)
    a = input("введите страну")
    if a in stran:
        print(stran[a])
    else:
        print("в списке нет")
        b = sorted(stran.keys())
        for key in b:
            print(f"{key}:{stran[key]}")

def z62():
    sp={"А":1, "В":1, "Е":1, "И":1, "Н":1, "О":1, "Р":1, "С":1, "Т":1,"Д":2, "К":2, "Л":2, "М":2, "П":2, "У":2,"Б":3, "Г":3 , "Ё":3, "Ь":3, "Я":3, "Й":4 , "Ы":4, "Ж":5, "З":5, "Х":5, "Ц":5, "Ч":5,"Ш":8, "Э":8, "Ю":8,"Ф":10, "Щ":10, "Ъ":10 }
    world=input("введите слово").upper()
    a= sum(sp.get(letter,0)for letter in world)
    print(f"Стоимость слова '{world}': {a} очков")

def z63():
    st=[{"name":"Саша","lang":["русский","английский","китайский"]},{"name":"Дима","lang":["русский","испанский","китайский"]},{"name":"Анна","lang":["русский","английский","французский"]}]
    al=[lang for student in st for lang in student["lang"]]
    all=set(al)
    sa=sorted(all)
    print("Отсортированный список уникальных языков:",sa)
    ch=[student["name"] for student in st if "китайский" in student["lang"]]
    print("Список студентов, которые знают китайский язык:",ch)
z63()
