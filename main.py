import sys
from library import Library


def print_menu():
    print("\n" + "=" * 30)
    print("   VITyarthi LIBRARY SYSTEM")
    print("=" * 30)
    print("1. Add New Book")
    print("2. View All Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    print("-" * 30)


def main():
    try:
        system = Library()
    except Exception as e:
        print(f"Error: {e}")
        return
    while True:
        print_menu()

        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            print("\n-- Add Book Details --")
            b_id = input("Enter ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            if b_id and title and author:
                system.add_book(b_id, title, author)
            else:
                print("Error: All fields are required.")

        elif choice == '2':
            system.list_books()

        elif choice == '3':
            b_id = input("\nEnter Book ID to borrow: ")
            system.borrow_book(b_id)

        elif choice == '4':
            b_id = input("\nEnter Book ID to return: ")
            system.return_book(b_id)

        elif choice == '5':
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()