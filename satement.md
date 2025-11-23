1. problem statement:Traditional methods of managing library records using physical registers are inefficient, time-consuming, and prone to human error.Librarian often struggle to track  which books are currently available versus those has been borrowed,leading to mismanagment Furthermore physical records are susceptible to damage or loss, posing a risk to the integrity of library data. There is a need for a digital solution to automate these tasks and ensure data persistence.
2. scope of the project: the scope of the project is to create a console based managment system using python.The system is designed to streamline the fundamental operations of a library including inventory management and transaction tracking.
3. Technical scope-
. core logic:Implements OOP  concepts (classes,objects) to model books and Library system.
. Data presistence:Utilizes File Handling (Text/CSV) to ensure data is saved and retrieved effectively preventing data loss when the program terminates.
. Interface:Features a modular menu-driven Command Line Interface (CLI) for ease of use.
4. Target users: Librarianas/Admiinistrators and students/Faculty
5. High level features:
   Book management:Functionality to add new books with details (ID, Title, Author) to the system catalog.
   Inventory Tracking:A view all feature that display the complete  list of books and their current status.
   Borrowing System: Allows users to check out books,automatically updating its status to "Borrowed" in the database.
   Return System: Allows user to return books,instantly updating the status back to "Available."
   Data Persistence:Automatic saving and loading of library records using file handling techniques to ensure longterm storage.
   Input Validation:Robust error handling to manage invalid inputs (e.g., entering empty data or non-existent Book IDs).
   
    
   
