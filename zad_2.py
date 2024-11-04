from datetime import date

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Adres: {self.street}, {self.city} {self.zip_code}.\n"
                f"Godziny otwarcia: {self.open_hours} \n" 
                f"Numer tel: {self.phone}")

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Imię i nazwisko: {self.first_name} {self.last_name}\n"
                f"Zatrudniono: {self.hire_date}\n"
                f"Urodziny: {self.birth_date}\n"
                f"Adres: {self.street}, {self.city} {self.zip_code}\n"
                f"Numer: {self.phone}\n")

class Book:
    def __init__(self, title ,library, publication_date, author_name, author_surname, number_of_pages):
        self.title = title
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Tytul: {self.title}\n"
                f"Autor: {self.author_name} {self.author_surname} Wydano {self.publication_date} \n"
                f"Strony: {self.number_of_pages}\n"
                f"Biblioteka:\n{self.library}")

class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_info = "\n".join(str(book) for book in self.books)
        return (f"Data: {self.order_date}\n"
                f"Pracownik:\n{self.employee}\n"
                f"Dla:\n{self.student}\n"
                f"Książki:\n{books_info}")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"

# -------------------------------------------
library1 = Library("Test1", "ul Zbrodniarzy Wojennych", "21-370", "8-16", "666 666 666")
library2 = Library("tes2", "ul Jakaś", "1111", "15:15-16:16", "123123132131")

employee1 = Employee("Antoni", "Macierewicz", date(2020, 5, 1), date(1990, 2, 15), "test", "aaaaaa", "omg", "jdjjd")
employee2 = Employee("abc", "abc", date(2019, 8, 10), date(1985, 7, 23), "aaaa", "21ds12s21", "1e212s1", "23jsj")
employee3 = Employee("jhhhh", "u8u8", date(2021, 3, 15), date(1995, 11, 30), "jdjd", "jhdjndj", "dkd", "111")

student1 = Student("Bogdan", [1, 2, 3])
student2 = Student("Bogumił", [12, 55, 55])
student3 = Student("Belzebub", [66, 66, 62])

book1 = Book( "AAA" ,library1, date(1410, 6, 5), "a", "a", 500)
book2 = Book("bbb", library1, date(2137, 3, 12), "a", "a", 320)
book3 = Book("zzz", library2, date(2000, 1, 20), "a", "a", 420)
book4 = Book( "a", library2, date(1999, 11, 18), "a", "a", 280)
book5 = Book( "b", library1, date(2012, 7, 23), "a", "a", 350)

order1 = Order(employee1, student1, [book1, book2], date(2023, 10, 5))
order2 = Order(employee2, student2, [book3, book4, book5], date(2023, 10, 10))


print(order1, "\n")
print(order2)
