
def is_palindrome(word):
    my_str = word.lower()
    # Reverse the string
    rev_str = my_str[::-1]

    # Compare the original and reversed strings
    if list(my_str) == list(rev_str):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


is_palindrome("level")
# is_palindrome("Python")
# is_palindrome("radar")
# is_palindrome("hello")
