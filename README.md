# cognizant-python-_exercise-
## EX:01:Simple Hello World 
## code:
```
print("Hello World!")
```
## output:
<img width="1267" height="105" alt="image" src="https://github.com/user-attachments/assets/a957fb80-2aed-4fd5-8e86-01ebbc86a3db" />


## EX:02:Jupyter Notebook 
## code:
```
print("Hello from Jupyter!")

```
## output:
<img width="783" height="315" alt="image" src="https://github.com/user-attachments/assets/109fe388-5c19-436c-b27f-d11eab873cc8" />

## EX:03:VS Code Setup 
## code:
```
name = "Roshhhh"
print("Welcome", name)
```
## output:
<img width="1256" height="147" alt="image" src="https://github.com/user-attachments/assets/245b76ad-304f-4dde-8873-617019f92a6c" />


## EX:04:Float Precision 
## code:
```
num = 10.56789

print("Original:", num)
print("2 decimal places:", round(num, 2))
print("3 decimal places:", round(num, 3))

```
## output:
<img width="1271" height="282" alt="image" src="https://github.com/user-attachments/assets/668868e7-e70a-4a8a-9cab-01cceb7ec561" />

## EX:05:Multiple Assignment
## code:
```
name = input("Enter your name: ")
age = int(input("Enter your age: python Ex05_UserInput.py"))

print("Hello", name)
print("Next year your age will be", age + 1)
```
## output:
<img width="897" height="62" alt="image" src="https://github.com/user-attachments/assets/99881eb9-87e8-49dc-bb90-82786015dc23" />

## EX:06:Modulo Operator 
## code:
```
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```
## output:
<img width="1282" height="133" alt="image" src="https://github.com/user-attachments/assets/ec71e078-4f0c-47f3-b7a2-cb347dfbb623" />

## EX:07:For Loop
## code:
```
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)
```
## output: 
<img width="1191" height="420" alt="image" src="https://github.com/user-attachments/assets/55386dfc-2d3b-4517-a704-a29c70e11b3b" />

## EX:08:ListLoop
## code:
```
fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    print(fruit)

```
## output:
<img width="522" height="227" alt="image" src="https://github.com/user-attachments/assets/504b30d3-1d4e-4c15-aaa2-48ebe4e985b7" />


## EX:09: String
## code:
```
text = input("Enter a string: ")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
```
## output:
<img width="1066" height="130" alt="image" src="https://github.com/user-attachments/assets/49ecf2f9-5851-4232-b0f2-290b4f78444c" />


## EX:10
## code:
```
def greet(name):
    print("Hello", name)

name = input("Enter your name: ")
greet(name)
```
## output:
<img width="1034" height="235" alt="image" src="https://github.com/user-attachments/assets/33d52937-b60f-4f5d-b3db-6ba0ab533987" />

## EX:11
## code:
```
def add_numbers(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add_numbers(num1, num2)

print("Sum is:", result)
```
## output:
<img width="1246" height="162" alt="image" src="https://github.com/user-attachments/assets/222e4112-2a80-40ea-9bba-27ebba839525" />

## EX:12
## code:
```
def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

num = int(input("Enter a number: "))
multiplication_table(num)
```
## output:
<img width="387" height="342" alt="image" src="https://github.com/user-attachments/assets/274e7972-0c5e-430f-8835-a594da5c16a0" />

## EX:13
## code:
```
def check_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is Even")

num = int(input("Enter a number: "))
check_even_numbers(num)
```
## output:
<img width="1267" height="241" alt="image" src="https://github.com/user-attachments/assets/fef597f1-9e76-4d58-b467-dbce44ea2f95" />

## EX:14
## code:
```
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print("*" * i)
```
## output:
<img width="1263" height="233" alt="image" src="https://github.com/user-attachments/assets/98f7275a-2233-4431-ab2e-bd3b9689051b" />

## EX:15
## code:
```
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```
## output:
<img width="1260" height="252" alt="image" src="https://github.com/user-attachments/assets/1f3b701b-7384-4530-8a67-b44e4eddada5" />

## EX:16
## code:
```
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

num = int(input("Enter a number: "))
result = sum_of_numbers(num)

print("Sum of first", num, "numbers is:", result)
```
## output:
<img width="1251" height="133" alt="image" src="https://github.com/user-attachments/assets/1aaf1930-d304-4413-bbea-167898289f6b" />

## EX:17
## code:
```
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
result = factorial(num)

print("Factorial of", num, "is:", result)
```
## output:
<img width="1260" height="136" alt="image" src="https://github.com/user-attachments/assets/626d95bb-8b86-498f-ba10-c71a0b920e8b" />

## EX:18
## code:
```
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number is:", reverse)
```
## output:
<img width="1245" height="125" alt="image" src="https://github.com/user-attachments/assets/b4e8161c-6237-4a88-9d39-a78da358d1e7" />

 ## EX:19
## code:
```
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
```
## output:

<img width="1005" height="203" alt="image" src="https://github.com/user-attachments/assets/1762aa35-c99f-4e37-bb8b-3161a889f5d2" />

 ## EX:20
## code:
```
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
```
## output:
<img width="976" height="138" alt="image" src="https://github.com/user-attachments/assets/74a1542a-0a7e-4c5c-9e81-86070a936ad6" />

 ## EX:21
## code:
```
n = int(input("Enter number of terms: "))

a = 0
b = 1

if n <= 0:
    print("Enter a positive number")
elif n == 1:
    print(a)
else:
    print(a)
    print(b)

    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c
```
## output:
<img width="981" height="403" alt="image" src="https://github.com/user-attachments/assets/681d5fa8-08cc-4d03-9294-43b379590ce7" />

 ## EX:22
## code:
```
text = input("Enter a string: ")

reverse = ""

for i in text:
    reverse = i + reverse

if text == reverse:
    print("Palindrome String")
else:
    print("Not a Palindrome String")
```
## output:
<img width="976" height="133" alt="image" src="https://github.com/user-attachments/assets/240c5a99-a993-4cb8-87a8-54c70eb75dc9" />

 ## EX:23
## code:
```
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)
```
## output:
<img width="985" height="141" alt="image" src="https://github.com/user-attachments/assets/ac6fdef7-8aa9-4db2-adb8-d18ab37dd913" />

## EX:24
## code:
```
n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)
```
## output:
<img width="991" height="217" alt="image" src="https://github.com/user-attachments/assets/c367bd4d-5416-473f-89ab-25f053640074" />

## EX:25
## code:
```
def add(a, b):
    if type(a) != int or type(b) != int:
        return "Invalid input"
    
    return a + b

print(add(5, 3))
```
## output:
<img width="978" height="91" alt="image" src="https://github.com/user-attachments/assets/8fcfc888-41ef-4278-be51-3234cb56658a" />

 ## EX:26
## code:
```
def area(length, width):
    if length <= 0 or width <= 0:
        return "Invalid input"
    
    return length * width

print(area(5, 3))
```
## output:
<img width="993" height="107" alt="image" src="https://github.com/user-attachments/assets/bbf79b65-9884-411a-89f8-02f5e2798382" />

## EX:27
## code:
```
def find_length(text):
    if text == "":
        return "Invalid input"
    
    return len(text)

print(find_length("Roshini"))
```
## output:
<img width="998" height="117" alt="image" src="https://github.com/user-attachments/assets/3a5286ee-5b8e-4fe0-88d8-a8fa8a6bbb28" />

 ## EX:28
## code:
```
def write_file():
    file = open("output.txt", "w")
    file.write("Hello World")
    file.close()
    return "File written successfully"

print(write_file())
```
## output:
<img width="1008" height="107" alt="image" src="https://github.com/user-attachments/assets/c9ed805c-7990-49f5-bb15-91088293d28a" />

 ## EX:29
## code:
```
def read_file():
    try:
        file = open("output.txt", "r")
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        return "File not found"

print(read_file())
```
## output:
<img width="1017" height="121" alt="image" src="https://github.com/user-attachments/assets/2b9f4b9c-b955-44d4-a5ea-0460fc05919b" />

 ## EX:30
## code:
```
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 2))
print(divide(10, 0))
```
## output:
<img width="1002" height="141" alt="image" src="https://github.com/user-attachments/assets/c44024a9-9530-464d-a122-320ae191b802" />

## EX:31
## code:
```
def show_cart():
    cart = [100, 250, 75]

    if len(cart) == 0:
        return "Cart is empty"

    return cart

print("Shopping Cart:", show_cart())
```
## output:
<img width="1011" height="117" alt="image" src="https://github.com/user-attachments/assets/d9d08d9d-6970-4e8d-b809-e66c7a80bdfd" />

 ## EX:32
## code:
```
def add_expense():
    expenses = [100, 200, 300]

    new_expense = 150

    if new_expense <= 0:
        return "Invalid expense"

    expenses.append(new_expense)

    return expenses

print(add_expense())
```
## output:
<img width="997" height="112" alt="image" src="https://github.com/user-attachments/assets/0d6fb886-ed23-4738-b13d-4e084bcca2f2" />

 ## EX:33
## code:
```
def update_employee():
    emp1 = {"name": "Roshini", "id": 101}
    emp2 = {"salary": 50000, "department": "AI"}

    if not emp1 or not emp2:
        return "Invalid input"

    emp1.update(emp2)

    return emp1

print(update_employee())
```
## output:
<img width="988" height="97" alt="image" src="https://github.com/user-attachments/assets/6df3995b-1e80-4030-8c17-74ada722e0a4" />

 ## EX:34
## code:
```
def get_salary(dept, emp_name):
    employees = {
        "AI": {
            "Roshini": 60000,
            "Arun": 55000
        },
        "IT": {
            "Kiran": 70000,
            "Meena": 65000
        }
    }

    if dept not in employees:
        return "Department not found"

    if emp_name not in employees[dept]:
        return "Employee not found"

    return employees[dept][emp_name]

print(get_salary("AI", "Roshini"))
```
## output:
<img width="998" height="98" alt="image" src="https://github.com/user-attachments/assets/006e4f86-bdb4-4ecb-9839-496f91faa318" />

 ## EX:35
## code:
```
def show_coordinates():
    coordinates = (10, 20)

    if len(coordinates) != 2:
        return "Invalid coordinates"

    x, y = coordinates

    return f"X: {x}, Y: {y}"

print(show_coordinates())
```
## output:
<img width="1012" height="95" alt="image" src="https://github.com/user-attachments/assets/a92d3a09-293b-474f-a079-75a179889e79" />

 ## EX:36
## code:
```
def common_skills():
    set1 = {"Python", "Java", "SQL", "AI"}
    set2 = {"Python", "C++", "SQL", "ML"}

    if not set1 or not set2:
        return "Invalid input"

    return set1 & set2   # intersection

print("Common Skills:", common_skills())
```
## output:
<img width="980" height="103" alt="image" src="https://github.com/user-attachments/assets/c06380bb-5069-4677-9b7f-b00c48a15958" />

 ## EX:37
## code:
```
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        return f"Name: {self.name}, ID: {self.emp_id}"


def main():
    emp1 = Employee("Roshini", 101)
    emp2 = Employee("Arun", 102)
    emp3 = Employee("Meena", 103)

    employees = [emp1, emp2, emp3]

    for emp in employees:
        print(emp.display())


main()

```
## output:
<img width="977" height="152" alt="image" src="https://github.com/user-attachments/assets/3a73901d-68d9-4a7c-bcc8-d56b07df510a" />

 ## EX:38
## code:
```
class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def set_salary(self, salary):
        if salary <= 0:
            self.salary = 0
        else:
            self.salary = salary
        return self

    def apply_raise(self, percent):
        if percent < 0:
            percent = 0
        self.salary += self.salary * (percent / 100)
        return self

    def display(self):
        print("Employee:", self.name)
        print("Final Salary:", self.salary)
        return self


def main():
    emp = Employee("Roshini")
    emp.set_salary(50000).apply_raise(10).display()


main()
```
## output:
<img width="985" height="132" alt="image" src="https://github.com/user-attachments/assets/185f14c1-b428-48d2-b4b0-f8ab0b5e5076" />

 ## EX:39
## code:
```
class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer writes code")


class Tester(Employee):
    def work(self):
        print("Tester tests the application")


def main():
    employees = [Developer(), Tester(), Employee()]

    for emp in employees:
        emp.work()


main()

```
## output:
<img width="991" height="168" alt="image" src="https://github.com/user-attachments/assets/614f916b-77ce-4f0b-8aaf-b1931f0a1d67" />

 ## EX:40
## code:
```
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def from_string(cls, data):
        name, salary = data.split(",")

        if not salary.isdigit():
            return "Invalid salary"

        return cls(name, int(salary))


def main():
    emp = Employee.from_string("Shubh,75000")
    print(emp.display())


main()
```
## output:
<img width="981" height="106" alt="image" src="https://github.com/user-attachments/assets/f36a2b26-a868-4999-9735-c452275e7d4a" />

 ## EX:41
## code:
```
# OOP + File Handling + JSON)
import json

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def to_dict(self):
        return {
            "id": self.emp_id,
            "name": self.name,
            "salary": self.salary
        }


def save_employees(emp_list):
    data = {}

    for emp in emp_list:
        data[emp.emp_id] = emp.to_dict()

    with open("emps.json", "w") as file:
        json.dump(data, file)

    return "Data saved successfully"


def load_employees():
    try:
        with open("emps.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return "No file found"


def main():
    e1 = Employee(101, "Roshini", 60000)
    e2 = Employee(102, "Arun", 55000)

    employees = [e1, e2]

    print(save_employees(employees))
    print(load_employees())


main()

```
## output:
<img width="1000" height="186" alt="image" src="https://github.com/user-attachments/assets/08c8637a-6cea-4f88-a1c2-8d3d96ef70c2" />

 ## EX:42
## code:
```
import statistics

def read_sales():
    try:
        with open("sales.txt", "r") as file:
            data = file.readlines()

        sales = []

        for value in data:
            value = value.strip()

            if value.isdigit():
                sales.append(int(value))

        if len(sales) == 0:
            return "No valid data"

        mean_val = statistics.mean(sales)
        median_val = statistics.median(sales)

        return f"Mean: {mean_val}, Median: {median_val}"

    except FileNotFoundError:
        return "File not found"


print(read_sales())
```
## output:
<img width="993" height="91" alt="image" src="https://github.com/user-attachments/assets/8a8af075-04ac-4ca0-a9f8-8be6f2d9d6b3" />

 ## EX:43
## code:
```
import configparser

class Config:
    def __init__(self, file_name):
        self.file_name = file_name
        self.config = configparser.ConfigParser()

    def load(self):
        self.config.read(self.file_name)
        return self.config


class DatabaseConfig(Config):
    def get_db_settings(self):
        config = self.load()

        if "database" not in config:
            return "Database section missing"

        db = config["database"]

        required_keys = ["host", "user", "password"]

        for key in required_keys:
            if key not in db:
                return f"Missing key: {key}"

        return {
            "host": db["host"],
            "user": db["user"],
            "password": db["password"]
        }


def main():
    obj = DatabaseConfig("db.ini")
    print(obj.get_db_settings())


main()
```
## output:
<img width="997" height="110" alt="image" src="https://github.com/user-attachments/assets/91a24c84-8322-4829-aeaf-1a8e00d40433" />

 ## EX:44
## code:
```
import csv

def process_csv():
    try:
        employees = []

        with open("employees.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["salary"] = int(row["salary"])
                employees.append(row)

        if len(employees) == 0:
            return "No data found"

        high_salary = [emp for emp in employees if emp["salary"] > 50000]

        total_salary = sum(emp["salary"] for emp in employees)
        avg_salary = total_salary / len(employees)

        return {
            "high_salary_employees": high_salary,
            "average_salary": avg_salary
        }

    except FileNotFoundError:
        return "File not found"


print(process_csv())
```
## output:
<img width="982" height="101" alt="image" src="https://github.com/user-attachments/assets/9b92c9fa-c7a0-4236-a187-a18745154ac1" />

 ## EX:45
## code:
```
import csv
from datetime import datetime

def expense_tracker():
    try:
        expenses = []

        current_month = datetime.now().month
        current_year = datetime.now().year

        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                date = datetime.strptime(row["date"], "%Y-%m-%d")
                amount = float(row["amount"])
                category = row["category"]

                # Filter current month
                if date.month == current_month and date.year == current_year:
                    expenses.append({
                        "date": date,
                        "amount": amount,
                        "category": category
                    })

        if not expenses:
            return "No expenses for current month"

        # Group by category
        summary = {}

        for exp in expenses:
            cat = exp["category"]
            summary[cat] = summary.get(cat, 0) + exp["amount"]

        return summary

    except FileNotFoundError:
        return "File not found"


print(expense_tracker())
```
## output:
<img width="986" height="97" alt="image" src="https://github.com/user-attachments/assets/0ff23e66-fbc6-4667-8478-5c1ed7f0bd48" />

 ## EX:46
## code:
```
import requests

def get_weather(city):
    try:
        if city.strip() == "":
            return "Invalid city name"

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)

        if response.status_code != 200:
            return "Error fetching data"

        data = response.json()

        current = data["current_condition"][0]

        temp = current["temp_C"]
        weather = current["weatherDesc"][0]["value"]

        return f"Temperature: {temp}°C, Condition: {weather}"

    except requests.exceptions.RequestException:
        return "Network error"


print(get_weather("Chennai"))
```
## output:

<img width="983" height="102" alt="image" src="https://github.com/user-attachments/assets/b3bdc01f-0578-4dc7-a8b8-22d8f3d351a2" />

 ## EX:47
## code:
```
def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            return "Invalid operator"

    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input type"


def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        result = calculate(a, b, op)

        print("Result:", result)

    except ValueError:
        print("Invalid number input")


main()
```
## output:
<img width="978" height="185" alt="image" src="https://github.com/user-attachments/assets/eec3c7e2-8f36-4ab9-ba96-46ccfa74c297" />

 ## EX:48
## code:
```
class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def calculate_total(self):
        total = sum(item.total_price() for item in self.items)
        gst = total * 0.18
        final_total = total + gst
        return total, gst, final_total

    def print_receipt(self):
        print("\n--- Receipt ---")
        for item in self.items:
            print(item.name, "-", item.quantity, "x", item.price, "=", item.total_price())

        total, gst, final_total = self.calculate_total()

        print("\nTotal:", total)
        print("GST (18%):", gst)
        print("Final Total:", final_total)


def main():
    cart = ShoppingCart()

    cart.add_item(CartItem("Rice", 50, 2))
    cart.add_item(CartItem("Milk", 30, 3))
    cart.add_item(CartItem("Soap", 40, 1))

    cart.remove_item("Soap")

    cart.print_receipt()


main()
```
## output:
<img width="975" height="311" alt="image" src="https://github.com/user-attachments/assets/04c7c96c-1ee1-4c4d-ba84-c6273f0cd74f" />

 ## EX:49
## code:
```
class TemperatureConverter:

    def c_to_f(self, c):
        return (c * 9/5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def c_to_k(self, c):
        return c + 273.15

    def k_to_c(self, k):
        return k - 273.15


def main():
    converter = TemperatureConverter()

    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Enter choice (1-4): ")

    try:
        temp = float(input("Enter temperature: "))

        if choice == "1":
            print("Result:", round(converter.c_to_f(temp), 2))

        elif choice == "2":
            print("Result:", round(converter.f_to_c(temp), 2))

        elif choice == "3":
            print("Result:", round(converter.c_to_k(temp), 2))

        elif choice == "4":
            print("Result:", round(converter.k_to_c(temp), 2))

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid temperature input")


main()
```
## output:
<img width="993" height="357" alt="image" src="https://github.com/user-attachments/assets/8fa2b4c3-0bb2-44a3-a0ec-9d4f91b7ea6c" />

 ## EX:50
## code:
```
 import shutil
import os

def backup_files():
    source_folder = "source_files"
    backup_folder = "backup_files"
    log_file = "backup.log"

    os.makedirs(backup_folder, exist_ok=True)

    copied_files = set()

    with open(log_file, "a") as log:
        for file_name in os.listdir(source_folder):

            source_path = os.path.join(source_folder, file_name)
            backup_path = os.path.join(backup_folder, file_name)

            if file_name in copied_files:
                continue

            try:
                shutil.copy(source_path, backup_path)
                copied_files.add(file_name)
                log.write(f"Copied: {file_name}\n")

            except FileNotFoundError:
                log.write(f"Missing file: {file_name}\n")

    return "Backup completed successfully"


print(backup_files())
```
## output:
<img width="977" height="101" alt="image" src="https://github.com/user-attachments/assets/e349b045-207d-4c09-a82f-288b355acba7" />

 ## EX:51
## code:
```
import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def _generate_short_code(self, url):
        # Create hash and take first 6 characters
        hash_object = hashlib.md5(url.encode())
        return hash_object.hexdigest()[:6]

    def shorten_url(self, url):
        if not url:
            return "Invalid URL"

        short_code = self._generate_short_code(url)
        self.url_map[short_code] = url

        return short_code

    def get_original_url(self, short_code):
        return self.url_map.get(short_code, "URL not found")


def main():
    shortener = URLShortener()

    url = "https://www.google.com"
    short_code = shortener.shorten_url(url)

    print("Short URL code:", short_code)
    print("Original URL:", shortener.get_original_url(short_code))


main()
```
## output:
<img width="976" height="133" alt="image" src="https://github.com/user-attachments/assets/a8e6d833-6720-496d-b4d7-e112523a232f" />

 ## EX:52
## code:
```
import json

# Student data structure:
# student_name -> list of grades

def calculate_gpa(grades):
    if not grades:
        return 0

    return sum(grades) / len(grades)


def add_student_grade(data, name, grade):
    if name not in data:
        data[name] = []

    if 0 <= grade <= 100:
        data[name].append(grade)
    else:
        print("Invalid grade ignored")


def class_average(data):
    all_grades = []

    for grades in data.values():
        all_grades.extend(grades)

    if not all_grades:
        return 0

    return sum(all_grades) / len(all_grades)


def save_data(data, filename="grades.json"):
    with open(filename, "w") as file:
        json.dump(data, file)


def load_data(filename="grades.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def main():
    students = load_data()

    add_student_grade(students, "Roshini", 85)
    add_student_grade(students, "Arun", 90)
    add_student_grade(students, "Roshini", 78)

    print("GPA Roshini:", calculate_gpa(students["Roshini"]))
    print("Class Average:", class_average(students))

    save_data(students)


main()
```
## output:
<img width="982" height="132" alt="image" src="https://github.com/user-attachments/assets/26d1972c-688a-4291-9d88-534c5dc854e9" />

 ## EX:53
## code:
```
from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

    def is_overdue(self):
        return self.due_date < datetime.now()


class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_sorted_tasks(self):
        return sorted(self.tasks, key=lambda t: t.due_date)

    def get_overdue_tasks(self):
        return [t for t in self.tasks if t.is_overdue()]

    def display_tasks(self):
        print("\n--- Task List ---")
        for task in self.get_sorted_tasks():
            status = "Overdue" if task.is_overdue() else "Pending"
            print(task.name, "-", task.due_date.date(), "-", task.priority, "-", status)


def main():
    scheduler = TaskScheduler()

    scheduler.add_task(Task("Finish Project", "2026-05-20", "High"))
    scheduler.add_task(Task("Study SQL", "2026-06-05", "Medium"))
    scheduler.add_task(Task("Practice Python", "2026-05-10", "High"))

    scheduler.display_tasks()

    print("\nOverdue Tasks:")
    for task in scheduler.get_overdue_tasks():
        print(task.name)


main()
```
## output:
<img width="977" height="338" alt="image" src="https://github.com/user-attachments/assets/278d6678-71f5-41b6-9604-09675474f4f0" />

 ## EX:54
## code:
```
#(OOP + Inheritance + Dictionaries + Sets)
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display(self):
        return f"{self.name} | Price: {self.price} | Stock: {self.stock}"


class Perishable(Product):
    def __init__(self, name, price, stock, expiry_date):
        super().__init__(name, price, stock)
        self.expiry_date = expiry_date


class Electronics(Product):
    def __init__(self, name, price, stock, warranty_years):
        super().__init__(name, price, stock)
        self.warranty_years = warranty_years


class InventoryManager:
    def __init__(self):
        self.products = {}
        self.low_stock_alert = set()

    def add_product(self, product):
        self.products[product.name] = product

        if product.stock < 5:
            self.low_stock_alert.add(product.name)

    def update_stock(self, name, new_stock):
        if name in self.products:
            self.products[name].stock = new_stock

            if new_stock < 5:
                self.low_stock_alert.add(name)
            elif name in self.low_stock_alert:
                self.low_stock_alert.remove(name)

    def show_inventory(self):
        print("\n--- Inventory ---")
        for product in self.products.values():
            print(product.display())

    def show_low_stock(self):
        print("\n--- Low Stock Items ---")
        for item in self.low_stock_alert:
            print(item)


def main():
    manager = InventoryManager()

    p1 = Perishable("Milk", 50, 3, "2026-06-10")
    p2 = Electronics("Phone", 15000, 10, 2)
    p3 = Product("Book", 200, 2)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    manager.show_inventory()
    manager.show_low_stock()

    manager.update_stock("Phone", 3)

    print("\nAfter Update:")
    manager.show_inventory()
    manager.show_low_stock()


main()


```
## output:
<img width="981" height="571" alt="image" src="https://github.com/user-attachments/assets/ad45ceaa-c295-4fa1-b461-c852f45e6581" />

 ## EX:55
## code:
```
import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        if amount <= 0:
            return "Invalid amount"
        self.spent += amount

    def status(self):
        if self.spent > self.limit:
            return f"{self.name}: Budget exceeded!"
        return f"{self.name}: Within budget"


class BudgetPlanner:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def show_status(self):
        print("\n--- Budget Status ---")
        for c in self.categories:
            print(c.status())

    def show_chart(self):
        names = [c.name for c in self.categories]
        spent = [c.spent for c in self.categories]

        plt.pie(spent, labels=names, autopct="%1.1f%%")
        plt.title("Monthly Budget Distribution")
        plt.show()


def main():
    planner = BudgetPlanner()

    food = Category("Food", 5000)
    travel = Category("Travel", 3000)
    shopping = Category("Shopping", 4000)

    food.add_expense(4500)
    travel.add_expense(3500)
    shopping.add_expense(2000)

    planner.add_category(food)
    planner.add_category(travel)
    planner.add_category(shopping)

    planner.show_status()
    planner.show_chart()


main()
```
## output:
<img width="985" height="217" alt="image" src="https://github.com/user-attachments/assets/ae5d50dc-0cdb-4044-92c7-958d1857c3ae" />

<img width="792" height="668" alt="image" src="https://github.com/user-attachments/assets/c3b1ac10-4bff-4af8-95ce-b72ea51ac1bc" />
