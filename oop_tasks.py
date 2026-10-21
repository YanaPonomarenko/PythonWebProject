class Car:
    def __init__(self, mark="", release_year=0, brand="", engine_capacity=0.0, shade="", cost=0.0):
        self.__mark = mark
        self.__release_year = release_year
        self.__brand = brand
        self.__engine_capacity = engine_capacity
        self.__shade = shade
        self.cost = cost

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        if value < 0:
            raise ValueError("Вартість не може бути від'ємною")
        self.__cost = value

    def __str__(self):
        return (
            f"Марка: {self.__mark}\n"
            f"Рік випуску: {self.__release_year}\n"
            f"Бренд: {self.__brand}\n"
            f"Об'єм двигуна: {self.__engine_capacity} л\n"
            f"Колір: {self.__shade}\n"
            f"Вартість: {self.cost:.2f}"
        )

    def enter_data(self):
        self.__mark = input("Марка авто: ").strip()
        self.__release_year = int(input("Рік випуску: "))
        self.__brand = input("Бренд: ").strip()
        self.__engine_capacity = float(input("Об'єм двигуна (л): "))
        self.__shade = input("Колір: ").strip()
        self.cost = float(input("Вартість: "))

    def print_data(self):
        print(self)


class Book:
    def __init__(self, name="", year=0, publisher="", genre="", author="", cost=0.0):
        self.__name = name
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.cost = cost

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        if value < 0:
            raise ValueError("Вартість не може бути від'ємною")
        self.__cost = value

    def __str__(self):
        return (
            f"Назва: {self.__name}\n"
            f"Рік: {self.__year}\n"
            f"Видавництво: {self.__publisher}\n"
            f"Жанр: {self.__genre}\n"
            f"Автор: {self.__author}\n"
            f"Вартість: {self.cost:.2f}"
        )

    def enter_data(self):
        self.__name = input("Назва книги: ").strip()
        self.__year = int(input("Рік видання: "))
        self.__publisher = input("Видавництво: ").strip()
        self.__genre = input("Жанр: ").strip()
        self.__author = input("Автор: ").strip()
        self.cost = float(input("Вартість: "))

    def print_data(self):
        print(self)


class Stadium:
    def __init__(self, title="", date="", country="", city="", seats=0):
        self.__title = title
        self.__date = date
        self.__country = country
        self.__city = city
        self.seats = seats

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, new_capacity):
        if type(new_capacity) is not int or new_capacity < 0:
            raise ValueError("Кількість місць має бути цілим невід'ємним числом.")
        self.__seats = new_capacity

    def __str__(self):
        return (
            f"Назва: {self.__title}\n"
            f"Дата відкриття: {self.__date}\n"
            f"Країна: {self.__country}\n"
            f"Місто: {self.__city}\n"
            f"Місць: {self.seats}"
        )

    def enter_data(self):
        self.__title = input("Назва стадіону: ").strip()
        self.__date = input("Дата відкриття (дд.мм.рррр): ").strip()
        self.__country = input("Країна: ").strip()
        self.__city = input("Місто: ").strip()
        self.seats = int(input("Кількість місць: "))

    def print_data(self):
        print(self)


def main():
    while True:
        print("\n1. Авто")
        print("2. Книга")
        print("3. Стадіон")
        print("0. Вихід")
        choice = input("Оберіть завдання: ").strip()

        if choice == "0":
            break
        if choice == "1":
            item = Car()
        elif choice == "2":
            item = Book()
        elif choice == "3":
            item = Stadium()
        else:
            print("Невірний вибір.")
            continue

        try:
            item.enter_data()
            print("\nРезультат")
            item.print_data()
        except ValueError as error:
            print(f"Помилка введення: {error}")


if __name__ == "__main__":
    main()