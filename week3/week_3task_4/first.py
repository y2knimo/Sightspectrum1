from main import number

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
elif number % 3 == 0:
    print("The number is divisible by 3.")
elif number % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by either 3 or 5.")

is_prime = True
if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print("The number is a prime number.")
else:
    print("The number is not a prime number.")
