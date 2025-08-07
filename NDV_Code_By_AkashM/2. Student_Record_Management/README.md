Student Record Management Dashboard 📚✨

📂 Project Overview
    This Python-based dashboard manages student records with full CRUD (Create, Read, Update, Delete) functionality. It stores data in a JSON file (students.json) for persistence and uses a simple command-line interface for interaction.

Files in This Folder

    -students.json 🗂️
     Stores student records in JSON format. Starts with one sample record.

    -student_manager.py 🐍
     Python script implementing the dashboard with functions to add, view, update, and delete students.

Key Components
    1. Data Storage 💾
        Student records saved in students.json as a list of dictionaries.

        Each record contains:

        Student ID

        Name

        Branch

        Year

        Marks

    2. Student Class 🎓

        Represents a student object with attributes matching the data fields.

        Provides a method to_dict() for converting object data into dictionary form suitable for JSON storage.

    3. StudentManager Class 🛠️

        Handles loading and saving JSON data.

        Maintains a list of Student objects in memory.

        Provides methods to:

        Add student ➕

        View students 👀

        Update student ✏️

        Delete student ❌

    4. Command-Line Interface 💻

        Menu-driven loop lets users select options to manage students.

        Validates input and gives feedback on actions.

How to Run ▶️

    Make sure Python is installed.

    Keep students.json and student_manager.py in the same folder.

    Run python student_manager.py in your terminal or command prompt.

    Use the menu to manage student records easily.

Example Usage 📝

    Add new students by entering ID, Name, Branch, Year, and Marks.

    View all students displayed in a clean table.

    Update details by Student ID; leave blank to keep current info.

    Delete students by ID when needed.

    Exit to quit the program.

Benefits 💪

    Lightweight with no need for databases.

    Persistent storage using JSON.

    Easy-to-use command-line interface.

    Ready for further enhancements.

Future Improvements 🚀

    Add input validation (e.g., numeric marks, unique IDs).

    Search students by name or branch.

    Sort and filter students in view mode.

    Build a GUI for better user experience.

Author ✍️
    This project is a simple yet effective student record management system built using Python and JSON for data storage.

