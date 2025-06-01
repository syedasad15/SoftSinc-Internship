
print("Unit Conversion CLI Tool")
print("1: km to miles")
print("2: miles to km")
print("3: Celsius to Fahrenheit")
print("4: Fahrenheit to Celsius")

choice = input("Enter conversion type (1-4): ")

values_str = input("Enter values separated by commas: ")
try:
    values = list(map(float, values_str.split(',')))
except ValueError:
    print("Invalid input. Please enter numeric values separated by commas.")
    

if choice == '1':
    result = list(map(lambda x: round(x * 0.621371, 4), values))
    print("Result (miles):", result)
elif choice == '2':
    result = list(map(lambda x: round(x / 0.621371, 4), values))
    print("Result (kilometers):", result)
elif choice == '3':
    result = list(map(lambda x: round((x * 9/5) + 32, 2), values))
    print("Result (Fahrenheit):", result)
elif choice == '4':
    result = list(map(lambda x: round((x - 32) * 5/9, 2), values))
    print("Result (Celsius):", result)
else:
    print("Invalid choice.")

