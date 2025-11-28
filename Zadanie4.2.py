def is_text_a_palindrome(text):
    """
        This function checks if the 'text' is palindrome,
        it means if they are the same if we read them from lef to right, 
        and from right to left.
    """
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