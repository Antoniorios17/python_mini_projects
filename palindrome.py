def is_palindrome(input):
    word = input
    reverse_word = input[::-1]
    if word == reverse_word:
        return True
    else:
        return False


print(is_palindrome("aa"))
print(is_palindrome("abc"))
print(is_palindrome("kayak"))
