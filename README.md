1.Library Management System
   Project Overview:
   This project is a Console-Based Library Management System built using Python. It was developed as  to demonstrate mastery of Python Fundamentals, Object-Oriented Programming (OOP), and File Handling.
The system allows librarians to manage book inventories and enables users to borrow or return books. Unlike simple scripts, this project uses a modular architecture and persistent storage (data is saved to a file), ensuring that records remain intact even after the program is closed.
2.  Key features:
    Book Management: Add new books with ID, Title, and Author details.
    Inventory Tracking: View a real-time list of all books and their availability status (Available/Borrowed).
     Borrowing System: Check out books, automatically updating their status in the database.
     Return System: Return books to the library, making them available again.
     Data Persistence: All data is automatically saved to library_data.txt. No database setup is required.
     Error Handling: Robust validation for invalid inputs (e.g., empty fields, non-existent IDs).

3. Technologies & Tools Used
Language: Python 3.x
Concepts Covered (Syllabus Alignment):
Module 12: Object-Oriented Programming (Classes Book, Library)
Module 10: Modules & Packages (Importing library, book)
Module 11: Arrays/Lists (Managing book collections)
Module 9: Functions (Modular logic)
Module 8: Control Flow (Menu loops, conditional logic)
Module 4: Input/Output Operations
Version Control: Git & GitHub
IDE: VS Code / PyCharm
4.Project Structure
The project follows a modular design with separation of concerns:
Library-Management/
│
├── book.py           Class definition for a 'Book' object
├── library.py        Logic for managing the collection and file handling
├── main.py           The main entry point (Menu & User Interface)
├── library_data.txt  Auto-generated file where data is stored
├── README.md         Project documentation
└── statement.md      Problem statement and scope definition5.Steps to Install & Run
5.Clone the Repository
git clone [https://github.com/your-username/Library-Management.git](https://github.com/your-username/Library-Management.git)
cd Library-Management
Verify Files
Ensure that main.py, library.py, and book.py are in the same folder.
Run the Application
Execute the main script using Python:
python main.py

6.Instructions for Testing
Follow these steps to verify the system works as expected:
Test Adding a Book:
Select Option 1 (Add New Book).
Enter ID: 101, Title: Python Basics, Author: Guido.
Expected Result: Success message appearing.
Test Viewing Books:
Select Option 2.
Expected Result: You should see [ID: 101] Python Basics... (Available).
Test Persistence (The "Close & Reopen" Test):
Select Option 5 to Exit.
Run python main.py again.
Select Option 2.
Expected Result: The book 101 should still be there (loaded from file).
Test Validation:
Try to borrow a book with ID 999 (which doesn't exist).
Expected Result: The system should show an error message and not crash.

 Screenshots
 <img width="1919" height="1079" alt="Screenshot 2025-11-23 192421" src="https://github.com/user-attachments/assets/6c8b96b2-5b15-4cb7-b0fe-7e42aecd2fd8" />

<img width="1909" height="1079" alt="Screenshot 2025-11-23 192453" src="https://github.com/user-attachments/assets/175d4454-fe1e-41cb-886b-2d3880d4eee9" />
<img width="1791" height="537" alt="Screenshot 2025-11-23 194048" src="https://github.com/user-attachments/assets/74a4b390-d599-484b-a770-2ed4d8893574" />
<img width="1919" height="1077" alt="Screenshot 2025-11-23 194542" src="https://github.com/user-attachments/assets/48edc6ed-3eca-4ab7-8d85-b9a2a3f54cd5" />
<img width="1919" height="1079" alt="Screenshot 2025-11-23 194600" src="https://github.com/user-attachments/assets/cd03c519-1801-4ffa-a043-c33ba2492b26" />
<img width="1919" height="1079" alt="Screenshot 2025-11-23 194651" src="https://github.com/user-attachments/assets/1207c864-631b-4f82-a1a8-cd4b6a17b22e" />
<img width="1082" height="878" alt="Screenshot 2025-11-23 194906" src="https://github.com/user-attachments/assets/cefbf154-4c0a-4c83-8703-1665f9c26edb" />













     
