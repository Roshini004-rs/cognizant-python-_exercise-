def area(length, width):
    if length <= 0 or width <= 0:
        return "Invalid input"
    
    return length * width

print(area(5, 3))