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


