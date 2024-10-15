import random
import os
from time import sleep

layer1 ='''=====================
||         |
||         |
||         
||
||
||
||
||
||
||
||
||
||
||
||
||
'''

layer2 ='''=====================
||         |
||         |
||         _
||        |_|
||
||
||
||
||
||
||
||
||
||
||
||
'''

layer3 ='''=====================
||         |
||         |
||         _
||        |_|
||       /   \\
||       |   |
||       \\___/
||
||
||
||
||
||
||
||
'''

layer4 ='''
=====================
||         |
||         |
||         _
||        |_|
||       /   \\
||       |   |\\
||       \\___/ \\
||
||
||
||
||
||
||
||
||
'''
layer5 ='''
=====================
||         |
||         |
||         _
||        |_|
||       /   \\
||      /|   |\\
||     / \\___/ \\
||
||
||
||
||
||
||
||
||
'''
layer6 ='''
=====================
||         |
||         |
||         _
||        |_|
||       /   \\
||      /|   |\\
||     / \\___/ \\
||          |    
||          |
||          |
||
||
||
||
||
||
'''
layer7 ='''
=====================
||         |
||         |
||         _
||        |_|
||       /   \\
||      /|   |\\
||     / \\___/ \\
||        | |    
||        | |
||        | |
||
||
||
||
||
||
'''
def SetCMD():
    os.system(f'mode con: cols={41} lines={20}')
def GameOver():
    os.system("cls")
    print("game over")
    sleep(0.7)
    if str(input("Начать заного? да/нет :::")) == "да" or str(input("Начать заного? да/нет :::")) == "Да":
        Start()
def Congratulations(world):
    os.system("cls")
    print("goooood, you win")
    print("correct word is "+world)
    sleep(0.7)
    if str(input("Начать заного? да/нет :::")) == "да" or str(input("Начать заного? да/нет :::")) == "Да":
        Start()
def GetRandomWorld(world):
    w = world[random.randint(0,len(world))]
    return w
def Game(world,predict):
    SetCMD()
    print(layer1)
    print(predict)
    errors = 0
    while True:
        char = str(input("какая буква? ::: "))
        if(char in world):
            print("correct")
            sleep(0.7)
            ind = 0
            for i in range(0,len(world)):
                if char == world[i]:
                    predict[i] = char
                    print(predict)
            if "_" not in predict:
                Congratulations(world)
                break
            if(errors == 0):
                print(layer1)
                print(predict)
                continue
            elif(errors == 1):
                print(layer2)
                print(predict)
                continue
            elif(errors == 2):
                print(layer3)
                print(predict)
                continue
            elif (errors == 3):
                print(layer4)
                print(predict)
                continue
            elif (errors == 4):
                print(layer5)
                print(predict)
                continue
            elif(errors == 5):
                print(layer6)
                print(predict)
                continue
            elif (errors == 6):
                print(layer7)
                print(predict)
                continue
        else:
            print("error")
            sleep(0.7)
            errors += 1
            if(errors == 1):
                print(layer2)
                print(predict)
                continue
            elif(errors == 2):
                print(layer3)
                print(predict)
                continue
            elif (errors == 3):
                print(layer4)
                print(predict)
                continue
            elif (errors == 4):
                print(layer5)
                print(predict)
                continue
            elif(errors == 5):
                print(layer6)
                print(predict)
                continue
            elif (errors == 6):
                print(layer7)
                print(predict)
                continue
            elif (errors == 7):
                GameOver()

def Start():
    worlds  = ["1ис2","пятница", "дружба", "цветы", "весна", "солнце", "радость", "звезды", "ночь", "музыка", "танцы", "смех", "воскресенье", "семья", "дом", "книги", "поэзия", "искусство", "любовь", "романтика", "пицца", "кино", "поход", "природа", "река", "лес", "горы", "море", "путешествие", "автобус", "самолет", "отель", "ресторан", "шампунь", "паста", "футбол", "баскетбол", "теннис", "плаванье", "велосипед", "машина", "кофе", "чай", "шоколад", "мороженое", "торты", "пирожные", "свадьба", "рождение", "день", "ночь", "рождество", "пасха", "хэллоуин", "дедушка", "бабушка", "мама", "папа", "брат", "сестра", "кузен", "кузина", "племянник", "племянница", "собака", "кошка", "рыба", "птица", "цветок", "дерево", "камень", "вода", "огонь", "земля", "воздух", "мечта", "надежда", "вера", "счастье", "удача", "талант", "успех", "мудрость", "игра", "игрушка", "автомат", "компьютер", "телефон", "телевизор", "радио", "часы", "очки", "шапка", "перчатки", "рубашка", "брюки", "юбка", "платье", "ботинки", "туфли", "сапоги"]
    world = GetRandomWorld(worlds)
    predict = []
    for i in world:
        predict.append("_")
    Game(world,predict)




if __name__ == '__main__':
    Start()
