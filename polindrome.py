# Palindrome Checker Program

text = input("Enter a word or number: ")

# Reverse the input
reversed_text = text[::-1]

if text == reversed_text:
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")
