def capitalize_words(text):
 
    return text.title()
 
user_input = input("Enter a sentence: ")
result = capitalize_words(user_input)

print("Capitalized sentence:", result)