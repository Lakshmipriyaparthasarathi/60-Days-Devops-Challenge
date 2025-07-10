try:
    x = int(input("Enter a number: "))
    print(f"Double of your number is {x * 2}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
