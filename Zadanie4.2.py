def is_text_a_palindrome(text):
    right_index = 0
    for letter in text:
        right_index -= 1
        if letter != text[right_index]:
            return False
    return True


## test ##
print("Is 'hello' a palindrome?", is_text_a_palindrome("hello"))
print("Is 'kayak' a palindrome?", is_text_a_palindrome("kayak"))
print("Is 'potop' a palindrome?", is_text_a_palindrome("potop"))