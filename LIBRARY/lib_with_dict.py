library = {}

def add_book():
    book = input("Enter book name: ")
    if book in library:
        print("Book already exists!")
    else:
        library[book] = "available"
        print("Book added successfully")

def issue_book():
    book = input("Enter book name to issue: ")
    if book in library:
        if library[book] == "available":
            library[book] = "issued"
            print("Book issued successfully")
        else:
            print("Book already issued")
    else:
        print("Book not found")

def return_book():
    book = input("Enter book name to return: ")
    if book in library:
        if library[book] == "issued":
            library[book] = "available"
            print("Book returned successfully")
        else:
            print("Book was not issued")
    else:
        print("Book not found")

def show_books():
    if not library:
        print("Library is empty")
    else:
        for book, status in library.items():
            print(book, ":", status)

# Menu
while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Show Books")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        issue_book()
    elif choice == 3:
        return_book()
    elif choice == 4:
        show_books()
    elif choice == 5:
        break
    else:
        print("Invalid choice")