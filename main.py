import random
import time
print("Hello world!")
name = 'Миша'
power = 100
health = 100
money = 0
situations = ['монстр', 'удача', 'еда', 'подарок']
monsters = ['тролли', 'орки', 'гномы', 'смог', 'квирл']
presents = ['кольчуга', 'оружие']
vibe = ['Вы наступаете в лужу','Проход становится уже','Вы слышите странный шелест сзади', 'Вы наступаете на что-то склизское', 'Вы видите просвет справа', 'Вас обвевает прохладный сквозняк']
print('Добро пожаловать в игру! Вы играете за персонажа, который охотится за монстрами и получает за это деньги. Сейчас у него силы: ', power, 'денег: ', money, 'здоровья: ', health)

while True:
    situation = random.choice(situations)
    if situation == 'монстр':
        name_m = random.choice(monsters)
        power_m = random.randint(1, 100)
        health_m = random.randint(1, 100)
        print(f'Имя монстра: {name_m}, сила монстра: {power_m}, здоровье монстра: {health_m}')
        time.sleep(5)
        pass
    elif situation == 'удача':
        print('Перед Вами два коридора. Один ведет направо, другой - налево. Ответьте, в какой коридор вы хотите пойти. Ответ дайте числом - 1 или 2')
        answer = int(input('Какой коридор выбираете?'))
        lucky_door = random.randint(1, 2)
        if answer == lucky_door:
            print('Вы нашли деньги! Поздравляем!')
            new_money = random.randint(1, 1000)
            print('Сумма, которую вы нашли:', new_money)
            money += new_money
        else:
            print('Вы долго шли по коридору, но так ничего и не нашли')
    elif situation == 'еда':
        print('Вы нашли еду! Поздравляем, Ваше здоровье восстановилось!')
    elif situation == 'подарок':
        print('Вы находите на земле коробочку. Что же в ней? Будем открывать?')
        present = random.choice(presents)
        if present == 'кольчуга':
            health = health + random.randint(1,100)
            print(f'Ваше здоровье поднимается до {health}')
        elif present == 'оружие':
            power = power + random.randint(1,100)
            print(f'Ваша сила поднимается до {power}')
        else:
            damage = random.randint(1,50)
            health -= damage
            print(f'Берегись! Дух прошлого вылетает из коробки и наносит Вам удар: {damage}. Ваше здоровье: {health} ')

    if health <= 0:
        print('Вы умерли. Игра окончена')
        death = True
