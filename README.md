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




