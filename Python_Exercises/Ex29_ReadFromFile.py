def read_file():
    try:
        file = open("output.txt", "r")
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        return "File not found"

print(read_file())