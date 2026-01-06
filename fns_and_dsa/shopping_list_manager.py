def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"Added: {item}")
            else:
                print("No empty items allowed!")

        elif choice == '2':
            if not shopping_list:
                print("List is empty!")
            else:
                item = input("Enter item to remove: ").strip()
                try:
                    shopping_list.remove(item)
                    print(f"Removed: {item}")
                except ValueError:
                    print(f"'{item}' not found in list!")

        elif choice == '3':
            if not shopping_list:
                print("\nShopping list is empty.")
            else:
                print("\nShopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"  {i}. {item}")

        elif choice == '4':
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()