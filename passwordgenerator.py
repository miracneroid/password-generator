import re

def simplify_to_single_digit(value):
    try:
        value = float(value)
        while value >= 10:
            value = sum(int(digit) for digit in str(value))
        return int(value)
    except ValueError:
        raise ValueError("Invalid input format")

def is_valid_input(number, name):
    try:
        float_number = float(number)
        valid_number = float_number == float_number
        valid_name = re.match("^[a-zA-Z]+$", name)
        return valid_number and valid_name
    except ValueError:
        return False

def generate_password(number, name):
    try:
        if not is_valid_input(number, name):
            raise ValueError("Invalid input format")
        
        scientific_notation = "{:e}".format(float(number))
        coefficient, exponent = scientific_notation.split('e')
        
        simplified_coefficient = simplify_to_single_digit(float(coefficient))
        simplified_exponent = simplify_to_single_digit(int(exponent))
        
        s1 = ''.join(str(simplify_to_single_digit(int(digit)))[:3] for digit in str(simplified_coefficient))
        
        if simplified_exponent % 2 == 1:
            s2 = ''.join(name[i-1] for i in range(1, len(name)+1) if i % 2 == 1)
        else:
            s2 = ''
        
        password = s1 + "@" + s2
        if len(password) < 8:
            password += "X" * (8 - len(password))
        
        print(f"Password for {number} and name {name}: {password}")
    except ValueError as e:
        print(e)

T = int(input("Enter the number of test cases: "))

for _ in range(T):
    number = input("Enter the number: ")
    name = input("Enter the name (case-insensitive): ")
    generate_password(number, name)
