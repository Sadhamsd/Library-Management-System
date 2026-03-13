library = []

while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.append(book)
        print(book + " added to library")

    elif choice == "2":
        if len(library) == 0:
            print("Library is empty")
        else:
            print("Books in library:")
            for book in library:
                print(book)

    elif choice == "3":
        book = input("Enter book name to issue: ")
        if book in library:
            library.remove(book)
            print(book + " issued successfully")
        else:
            print("Book not available")

    elif choice == "4":
        book = input("Enter book name to return: ")
        library.append(book)
        print(book + " returned to library")

    elif choice == "5":
        print("Thank you")
        break

    else:
        print("Invalid choice")