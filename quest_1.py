class Data():
    day = None;
    month = None;
    year = None;

    def __init__(self, data):
        self.data = data

    @classmethod
    def to_int(cls, data):
        [day, month, year] = data.split("-")
        cls.day = int(day)
        cls.month = int(month)
        cls.year = int(year)

    @staticmethod
    def validation(month):
        month_dict = {1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля", 5: "Мая", 6: "Июня", 7: "Июля", 8: "Августа",
                      9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}
        return month_dict[month]

    def __str__(self):
        return f"{self.day} {self.month} {self.year}"


data_1 = Data("11-12-1998")
print(data_1.data)
data_1.to_int(data_1.data)
print(data_1)
data_1.month = data_1.validation(data_1.month)
print(data_1)

data_2 = Data("12-5-1997")
data_2.to_int(data_2.data)
data_2.month = data_2.validation(data_2.month)
print(data_2)
