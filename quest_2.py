class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data_1 = input("Введите первое число: ")
inp_data_2 = input("Введите второе число: ")

try:
    inp_data_1 = int(inp_data_1)
    inp_data_2 = int(inp_data_2)
    if inp_data_2 == 0:
        raise OwnError("Нельзя делить на нуль")
    res = inp_data_1 / inp_data_2
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Результат деления: {res}")
