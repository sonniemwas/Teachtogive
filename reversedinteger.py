'''Write a program that takes an integer as input and returns an integer with
reversed digit ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19.'''
def reverse_integer(n):
    reversed_str = str(abs(n))[::-1]
    reversed_int = int(reversed_str)
    return -reversed_int if n < 0 else reversed_int
user_input = input("Enter an integer: ")
try:
    number = int(user_input)
    result = reverse_integer(number)
    print("Reversed integer:", result)
except ValueError:
    print("Please enter a valid integer.")


