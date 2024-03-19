def is_palindrome(text):
    return ''.join([c.lower() for c in text if c.isalnum()]) == ''.join([c.lower() for c in text[::-1] if c.isalnum()])

# Przykłady użycia funkcji
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("No 'x' in Nixon"))                # True
print(is_palindrome("not a palindrome"))               # False
