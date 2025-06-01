from Challengepart1 import calculate
from Challengepart2 import organize
from Challengepart3 import generate


while True:
    print("\nChoose an option:")
    print("1. Calculator")
    print("2. Organize Files")
    print("3. Generate Password")
    print("4. Exit")
    choice = input("Enter choice (1-4): ")
    if choice == "1":
        calculate()
    elif choice == "2":
        organize()
    elif choice == "3":
        generate()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
