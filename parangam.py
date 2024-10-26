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
