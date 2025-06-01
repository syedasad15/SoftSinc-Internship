def kmtom(values):
    result = list(map(lambda x: round(x * 0.621371, 4), values))
    print("Result (miles):", result)
def miltokm(values):
    result = list(map(lambda x: round(x / 0.621371, 4), values))
    print("Result (kilometers):", result)    
def ctof(values):
    result = list(map(lambda x: round((x * 9/5) + 32, 2), values))
    print("Result (Fahrenheit):", result)
def ftoc(values):
    result = list(map(lambda x: round((x - 32) * 5/9, 2), values))
    print("Result (Celsius):", result)    
def converter():
    print("Unit Conversion CLI Tool")
    print("1: km to miles")
    print("2: miles to km")
    print("3: Celsius to Fahrenheit")
    print("4: Fahrenheit to Celsius")

    while True:
        choice = input("Enter conversion type (1-4): ")
        if choice in ['1', '2', '3', '4']:
            break  
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    while True:
        values_str = input("Enter values separated by commas: ")
        try:
            values = list(map(float, values_str.split(',')))
            break  
        except ValueError:
            print("Invalid input. Please enter only numeric values separated by commas.")
    if choice == '1':
        kmtom(values)
    elif choice == '2':
        miltokm(values)
    elif choice == '3':
        ctof(values)
    elif choice == '4':
        ftoc(values)
    else:
        print("Invalid choice.")

