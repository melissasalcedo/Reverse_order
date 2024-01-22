# Print the reverse number of the given list

# Function
def reverse_number(number):
    reversed_str = str(number)[::-1]

    reverse_number = ' '.join(reversed_str)
    print(reverse_number)
# Numbers
input_number = 100220
reverse_number(input_number)