def add(a, b):
    if type(a) != int or type(b) != int:
        return "Invalid input"
    
    return a + b

print(add(5, 3))