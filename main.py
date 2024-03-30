def nthSandwich(n):
    count = 0
    current_number = 11

    while True:
        if is_sandwich(current_number):
            count += 1

        if count == n:
            return current_number

        current_number += 1


def is_sandwich(num):
    first_digit = num // 10

    last_digit = num % 10

    if first_digit == last_digit:
        if num // 10 % 10 != first_digit:
            return True

    return false



#Syntax Error
if x == 5:
    print("x is 5")
else  # 콜론
    print("x is not 5")

#Runtime Error
x = 5
y = 0
z = x / y

