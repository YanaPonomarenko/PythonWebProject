# __new__ створення обєкта
# __init__ ініціалізація обєкта

class Person:
    def __init__(self):
        self.__full_name = ""
        self.__birth_date = ""
        self.__phone = ""
        self.__city = ""
        self.__country = ""
        self.__address = ""

    def input_data(self):
        self.__full_name = input("Введіть ПІБ: ")
        self.__birth_date = input("Введіть дату народження: ")
        self.__phone = input("Введіть телефон: ")
        self.__city = input("Введіть місто: ")
        self.__country = input("Введіть країну: ")
        self.__address = input("Введіть адресу: ")

    def output_data(self):
        print("\nІнформація про людину")
        print(f"ПІБ:              {self.__full_name}")
        print(f"Дата народження:  {self.__birth_date}")
        print(f"Телефон:          {self.__phone}")
        print(f"Місто:            {self.__city}")
        print(f"Країна:           {self.__country}")
        print(f"Адреса:   {self.__address}")

if __name__ == "__main__":
    person = Person()
    person.input_data()
    person.output_data()