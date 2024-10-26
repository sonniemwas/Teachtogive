'''Write a program that accepts a string as input, capitalizes the first letter of each
word in the string, and then returns the result string.
Examples:
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming" '''
def capitalize_words(text):
 
    return text.title()
 
user_input = input("Enter a sentence: ")
result = capitalize_words(user_input)

print("Capitalized sentence:", result)
