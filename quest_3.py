class IntAndFloat(Exception):

    def __init__(self,txt):
        self.txt = txt


my_float = []
flag = False
print("Для окончания работы напишите 'stop'")
while True:
    my_str = input("Вводите числа: ")
    my_str = my_str.split()
    for el in my_str:
        if el == 'stop':
            flag = True
        try:
            if not el.isdigit():
                raise IntAndFloat("Введено не число")
            el = float(el)
            my_float.append(el)
        except IntAndFloat as err:
            print(err)
    print(f'Итоговый список: {my_float}')
    if flag == True:
        print("Окончание работы")
        break

