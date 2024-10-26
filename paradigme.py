def is_palindrome():
    text = input("Enter a word or phrase: ")
    cleaned_text = ''.join(text.lower().split())
    if cleaned_text == cleaned_text[::-1]:
        print(f"True - {text} is a palindrome.")
        return True
    else:
        print(f"False - {text} is not a palindrome.")
        return False

is_palindrome()
