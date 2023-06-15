from main import number

factorial = 1
if number < 0:
    print("Factorial cannot be calculated for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print("The factorial of", number, "is", factorial)

if number >= 0 and number ** 0.5 == int(number ** 0.5):
    print("The number is a perfect square.")
else:
    print("The number is not a perfect square.")
