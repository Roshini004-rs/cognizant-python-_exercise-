def write_file():
    file = open("output.txt", "w")
    file.write("Hello World")
    file.close()
    return "File written successfully"

print(write_file())