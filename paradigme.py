'''Write a Python function that checks whether a word or phrase is palindrome or
not.
Note: A palindrome is word, phrase, or sequence that reads the same
backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"
'''
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
