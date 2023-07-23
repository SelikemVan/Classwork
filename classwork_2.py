
def palindrome(word):
    my_str = word.lower()
    rev_str = my_str[::-1]

    # Compare the original and reversed strings
    if list(my_str) == list(rev_str):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


palindrome("level")
# palindrome("Python")
# palindrome("radar")
# palindrome("hello")
