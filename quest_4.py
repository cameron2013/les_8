from abc import ABC, abstractmethod


class MyOwnABC(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def stop_work(self):
        pass


class Office():

    def __init__(self, count, name):
        try:
            self.name = name
            self.count = int(count)
        except ValueError:
            print("Количество товаров введено не числом\nТовар не создан, введите параметры заново")


class Printer(Office, MyOwnABC):

    def __init__(self, count, name):
        super().__init__(count, name)

    def work(self):
        print("Печатаю")

    def stop_work(self):
        print("Останавливаю печать")


class Scanner(Office, MyOwnABC):

    def __init__(self, count, name):
        super().__init__(count, name)

    def work(self):
        print("Сканирую")

    def stop_work(self):
        print("Перестаю сканировать")


class Copier(Office, MyOwnABC):

    def __init__(self, count, name):
        super().__init__(count, name)

    def work(self):
        print("Копирую")

    def stop_work(self):
        print("Перестаю копровать")


class Storage():
    full = 0
    storage_dict = {"Printer": 0, "Scanner": 0, "Copier": 0}

    def __init__(self, places):
        try:
            self.places = places
            list_none = [None] * places
            self.storage_dict_places = dict(zip(range(1, places + 1), list_none))
        except ValueError:
            print("Количество мест на скалде введено не числом: ")

    def recieve(self, count, offices, name):
        try:
            count = int(count)
            if self.full + count <= self.places:
                print("Завозим на склад.")
                self.full += count
                self.storage_dict[offices] += count
                j = 0
                for i in range(1, self.places + 1):
                    if self.storage_dict_places[i] is None:
                        self.storage_dict_places[i] = name
                        j += 1
                        if j == count:
                            break
                    else:
                        pass
            else:
                print("Cклад не может принять товар из-за отсутствия места")
        except ValueError:
            pass

    def decline(self, count, offices, name):
        try:
            count = int(count)
            if self.storage_dict[offices] >= count:
                print("Увозим из склада другой отдел.")
                self.full -= count
                self.storage_dict[offices] -= count
                j = 0
                for i in range(1, self.places + 1):
                    if self.storage_dict_places[i] == name:
                        self.storage_dict_places[i] = None
                        j += 1
                        if j == count:
                            break
                    else:
                        pass
            else:
                print("Товара на складе недостаточно")
        except ValueError:
            pass

    def __str__(self):
        s = "На складе:\n"
        for el in self.storage_dict:
            s = s + f"{el}: {self.storage_dict[el]} шт.\n"
        return s

    def places_storage(self):
        s = "Местоположение товаров на складе: \n"
        for el in self.storage_dict_places:
            if self.storage_dict_places[el] is not None:
                s = s + f"Полка №{el} - Товар {self.storage_dict_places[el]} \n"
        return s


stor_1 = Storage(100)
item_1 = Scanner(4, "ABC")
item_2 = Printer(3, "Printer X")
item_1.work()
item_2.work()
stor_1.recieve(item_1.count, item_1.__class__.__name__, item_1.name)
stor_1.recieve(item_2.count, item_2.__class__.__name__, item_2.name)
print(stor_1)
print(stor_1.places_storage())
stor_1.decline(item_1.count, item_1.__class__.__name__, item_1.name)
item_3 = Copier(97, "Zendo")
stor_1.recieve(item_3.count, item_3.__class__.__name__, item_3.name)
print(stor_1)
print(stor_1.places_storage())
stor_1.decline(item_3.count, item_3.__class__.__name__, item_3.name)
stor_1.recieve(item_1.count, item_1.__class__.__name__, item_1.name)
print(stor_1)
print(stor_1.places_storage())
