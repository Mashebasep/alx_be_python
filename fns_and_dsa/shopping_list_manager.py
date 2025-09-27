def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Quit")

    def add_item(shopping_list):
        item = input("Enter item to add:").strip()
        if item:
            shopping_list.append(item)
            print(f"Added '{item}' to the list.")
        else:
            print("Item cannot be empty.")

            def remove_item(shopping_list):
                item = input("Enter item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"Removed '{item}' from the list.")
                else:
                    print(f"'{item}' not found in the list.")

                    def view_list(shopping_list):
                        if shopping_list:
                            print("/nShopping List:")
                            for i, item in enumerate(shopping_list, start=1):
                                print(f"{i}. {item}")
                            else:
                                print("The shopping list is empty.")

                                def main():
                                    shopping_list = []
                                    while True:
                                        display_menu()
                                        # Enter input       
                                        choice = input("Enter your choice: ")
                                        if choice == 1:
                                            add_item(shopping_list)
                                        elif choice == 2:
                                            remove_item(shopping_list)
                                        elif choice == 3:
                                            view_list(shopping_list)
                                        elif choice == 4:
                                            print("Goodbye!")
                                            break
                                        else:
                                            print("Invalid choice. Please try again.")



