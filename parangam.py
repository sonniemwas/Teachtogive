'''
Write a Python function to check whether a string is pangram or not. (Assume
the string passed in does not have any punctuation)
Note: Pangrams are words or sentences containing every letter of the
alphabet at least once. For example: "The quick brown fox jumps over the
lazy dog
'''
def is_pangram(text):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    text_letters = set(text.lower().replace(" ", ""))
    return alphabet.issubset(text_letters) 
user_input = input("Enter a sentence: ")
result = is_pangram(user_input)

if result:
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
