def is_text_a_palindrome(text):
    """
        Description:
        This function checks if the 'text' is palindrome,
        it means if they are the same if we read them from left to right, 
        and from right to left.

        Arguments:
        text (string)

        Returns:
        This function returns boolean True if text is a palindrome otherwise False.
    """
    reversed_text = text[::-1]
    if text == reversed_text:
        return True
    else:
        return False


## test ##
print("Is 'hello' a palindrome?", is_text_a_palindrome("hello"))
print("Is 'kayak' a palindrome?", is_text_a_palindrome("kayak"))
print("Is 'potop' a palindrome?", is_text_a_palindrome("potop"))