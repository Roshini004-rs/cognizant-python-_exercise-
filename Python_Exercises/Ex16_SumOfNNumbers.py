def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

num = int(input("Enter a number: "))
result = sum_of_numbers(num)

print("Sum of first", num, "numbers is:", result)