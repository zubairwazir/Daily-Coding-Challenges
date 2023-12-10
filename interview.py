# Question 1: Write a Python program to check if a string is a palindrome.

string = "gig"

# Remove spaces and convert to lowercase for case-insensitive comparison
string = string.replace(" ", "").lower()

# create an empty string
reversed_string = ''

for char in string:
    reversed_string = char + reversed_string

if string == reversed_string:
    print(string + " is palindrome")
else:
    print(string + " is not palindrome")



# Solution Using Function
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

# Test the function
word = "madam"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
