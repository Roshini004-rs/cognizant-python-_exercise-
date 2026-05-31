def check_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is Even")

num = int(input("Enter a number: "))
check_even_numbers(num)