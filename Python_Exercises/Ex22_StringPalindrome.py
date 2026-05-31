text = input("Enter a string: ")

reverse = ""

for i in text:
    reverse = i + reverse

if text == reverse:
    print("Palindrome String")
else:
    print("Not a Palindrome String")