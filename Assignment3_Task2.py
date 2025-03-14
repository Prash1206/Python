import math

number = float(input("Enter a positive number: "))
if number <= 0:
    print("Please enter a positive number")
else:
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)

    print(f"\nResults for {number}:")
    print(f"Square root: {square_root:}")
    print(f"logarithm: {natural_log:}")
    print(f"Sine: {sine_value:}")