### lucky

stop = True
hello = "Привет,это моя вторая программа"
a1 = print(hello)
#################
for o in range(11):
    print(o)
a2 = print("Отлично,а теперь приступай!")
number1 = int(input("Введите число для проверки четности:  "))
if (number1 % 2) ==0:
    res = print("Четное число!")
else:
    res = print("Не четное число!")
####################################
pred = int(input("Хотите я вам напишу четные числа до 100? \n1-да \n 2-нет"))
if pred ==1:
    for i in range(101):
        if (i % 2) ==0:
            print(i)
if pred ==2:
        print("Работа прекращена")

