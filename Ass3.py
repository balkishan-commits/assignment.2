# 1. Student Class


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Rahul", 20, "BCA")

print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)




# 2. Car Class



class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car1 = Car("Toyota", "Fortuner", 4500000)
car2 = Car("Hyundai", "Creta", 1800000)

print("Car 1:", car1.brand, car1.model, car1.price)
print("Car 2:", car2.brand, car2.model, car2.price)



# 3. Employee Class



class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

emp = Employee(101, "Amit", 50000)

print("Employee ID:", emp.employee_id)
print("Name:", emp.name)
print("Salary:", emp.salary)



# 4. Rectangle Class



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area =", self.length * self.width)

r = Rectangle(10, 5)
r.area()
# 5. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Area =", area)

c = Circle(7)
c.area()



# 6. BankAccount Class



class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance after withdrawal:", self.balance)
        else:
            print("Insufficient Balance")

acc = BankAccount("Rahul", 10000)

acc.deposit(5000)
acc.withdraw(3000)
# 7. Animal and Dog Class (Method Overriding)
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()


# 8. Person and Student Class (Inheritance)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_number)

s = Student("Rohit", 19, 25)
s.display()



# 9. Calculator Class


class Calculator:
    def add(self, a, b):
        print("Addition =", a + b)

    def subtract(self, a, b):
        print("Subtraction =", a - b)

    def multiply(self, a, b):
        print("Multiplication =", a * b)

    def divide(self, a, b):
        if b != 0:
            print("Division =", a / b)
        else:
            print("Cannot divide by zero")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

c = Calculator()

c.add(num1, num2)
c.subtract(num1, num2)
c.multiply(num1, num2)
c.divide(num1, num2)


# 10. LibraryBook Class


class LibraryBook:
    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price

    def display_book_info(self):
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Price:", self.price)
        print()

book1 = LibraryBook("Python Programming", "John Smith", 500)
book2 = LibraryBook("Data Structures", "Robert", 650)
book3 = LibraryBook("Machine Learning", "Andrew Ng", 800)

book1.display_book_info()
book2.display_book_info()
book3.display_book_info()