"""
Student Records Management System
Task 9: Practice Python Lists With Student Records

This beginner-friendly, menu-driven console program manages student records
using two synchronized parallel lists: `names` and `marks`.

Key Built-in Functions Used:
- len(): Get total number of students
- sum(): Compute total marks for class average
- max(): Identify highest mark
- min(): Identify lowest mark
- zip(): Pair names and marks together for iteration and sorting
- enumerate(): Generate serial numbers for listings and searches
- sorted(): Sort paired records while keeping lists aligned
"""


def display_menu():
    """Display the interactive main menu options to the user."""
    print("\n" + "=" * 45)
    print("      STUDENT RECORDS MANAGEMENT SYSTEM      ")
    print("=" * 45)
    print("1. Add a Student")
    print("2. View All Students")
    print("3. Search for a Student by Name")
    print("4. Sort Students (by Marks or Name)")
    print("5. Show Highest and Lowest Scores")
    print("6. Show Class Average")
    print("7. Delete a Student")
    print("8. Exit")
    print("=" * 45)


def get_valid_name(prompt="Enter student name: "):
    """
    Prompt the user for a student name and validate that it is not empty.

    Parameters:
        prompt (str): Custom prompt string.

    Returns:
        str: The trimmed, non-empty student name.
    """
    while True:
        name = input(prompt).strip()
        if not name:
            print("[!] Error: Student name cannot be empty. Please try again.")
        else:
            return name


def get_valid_marks(prompt="Enter student marks (0 - 100): "):
    """
    Prompt the user for marks and validate that it is a numeric value between 0 and 100.

    Parameters:
        prompt (str): Custom prompt string.

    Returns:
        float: Validated marks between 0.0 and 100.0.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            marks = float(user_input)
            if 0.0 <= marks <= 100.0:
                # Return integer if it has no fractional part, else float
                return round(marks, 2)
            else:
                print("[!] Error: Marks must be between 0 and 100.")
        except ValueError:
            print("[!] Error: Invalid input. Marks must be a number (e.g., 85 or 92.5).")


def add_student(names, marks):
    """
    Add a new student name and marks to the parallel lists.
    Validates input and warns if duplicate names exist.

    Parameters:
        names (list): List of student names.
        marks (list): List of student marks.
    """
    print("\n--- [1] Add New Student ---")
    name = get_valid_name("Enter student name: ")
    score = get_valid_marks("Enter marks (0 - 100): ")

    # Check for duplicate names (case-insensitive)
    existing_matches = [n for n in names if n.lower() == name.lower()]
    if existing_matches:
        print(f"[!] Note: A student named '{existing_matches[0]}' already exists.")
        confirm = input("Do you still want to add this record? (y/n): ").strip().lower()
        if confirm != 'y':
            print("[-] Operation cancelled. Student not added.")
            return

    # Keep both lists synchronized by appending at the same time
    names.append(name)
    marks.append(score)
    print(f"[+] Successfully added {name} with {score} marks.")


def view_students(names, marks):
    """
    Display all student records in a formatted table with serial numbers.

    Parameters:
        names (list): List of student names.
        marks (list): List of student marks.
    """
    print("\n--- [2] Student Records ---")
    if not names:
        print("[!] No student records found. The list is empty.")
        return

    # Table header
    print("-" * 45)
    print(f"{'S.No':<6}{'Student Name':<28}{'Marks':>10}")
    print("-" * 45)

    # Use enumerate() and zip() to iterate through synchronized lists
    for sno, (name, mark) in enumerate(zip(names, marks), start=1):
        print(f"{sno:<6}{name:<28}{mark:>10.2f}")

    print("-" * 45)
    print(f"Total Students: {len(names)}")


def search_student(names, marks):
    """
    Search for a student by name (case-insensitive).
    Displays matching student(s) and their marks, or handles 'not found'.

    Parameters:
        names (list): List of student names.
        marks (list): List of student marks.
    """
    print("\n--- [3] Search Student by Name ---")
    if not names:
        print("[!] No student records available to search.")
        return

    query = get_valid_name("Enter student name to search: ")
    query_lower = query.lower()

    # Search using enumerate() and zip()
    matches = []
    for idx, (name, mark) in enumerate(zip(names, marks), start=1):
        if name.lower() == query_lower:
            matches.append((idx, name, mark))

    if matches:
        print(f"\n[+] Found {len(matches)} matching record(s):")
        print("-" * 45)
        print(f"{'S.No':<6}{'Student Name':<28}{'Marks':>10}")
        print("-" * 45)
        for sno, name, mark in matches:
            print(f"{sno:<6}{name:<28}{mark:>10.2f}")
        print("-" * 45)
    else:
        # Partial match suggestion if exact match was not found
        partial_matches = [
            (idx, name, mark)
            for idx, (name, mark) in enumerate(zip(names, marks), start=1)
            if query_lower in name.lower()
        ]
        if partial_matches:
            print(f"[-] Exact match for '{query}' not found. Did you mean:")
            for sno, name, mark in partial_matches:
                print(f"    * #{sno} {name} (Marks: {mark:.2f})")
        else:
            print(f"[!] No student found with name '{query}'.")


def sort_students(names, marks):
    """
    Sort students by marks (highest to lowest) or by name (A to Z).
    Keeps both parallel lists strictly aligned using zip() and sorted().

    Parameters:
        names (list): List of student names.
        marks (list): List of student marks.
    """
    print("\n--- [4] Sort Students ---")
    if not names:
        print("[!] No student records available to sort.")
        return

    print("Choose sorting criteria:")
    print("1. By Marks (Highest to Lowest)")
    print("2. By Name (A to Z, Alphabetical)")
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == '1':
        # Sort by marks in descending order; secondary sort by name
        paired = list(zip(names, marks))
        # sorted() returns a new sorted list of tuples (name, mark)
        sorted_pairs = sorted(paired, key=lambda item: item[1], reverse=True)
        # Update both lists in-place using slice assignment to maintain synchronization
        names[:], marks[:] = [item[0] for item in sorted_pairs], [item[1] for item in sorted_pairs]
        print("[+] Students sorted by marks (Highest to Lowest).")
        view_students(names, marks)

    elif choice == '2':
        # Sort by name alphabetically (case-insensitive)
        paired = list(zip(names, marks))
        sorted_pairs = sorted(paired, key=lambda item: item[0].lower())
        # Update both lists in-place using slice assignment
        names[:], marks[:] = [item[0] for item in sorted_pairs], [item[1] for item in sorted_pairs]
        print("[+] Students sorted by name (A to Z).")
        view_students(names, marks)

    else:
        print("[!] Invalid sorting option selected. Returning to main menu.")


def show_highest_lowest(names, marks):
    """
    Display the highest and lowest scores, along with all student names
    who achieved those scores (handles ties gracefully).

    Parameters:
        names (list): List of student names.
        marks (list): List of student marks.
    """
    print("\n--- [5] Highest and Lowest Scores ---")
    if not names:
        print("[!] No student records available.")
        return

    # Use built-in max() and min() functions
    highest_score = max(marks)
    lowest_score = min(marks)

    # Find all students matching highest/lowest (handling ties)
    top_achievers = [name for name, mark in zip(names, marks) if mark == highest_score]
    lowest_achievers = [name for name, mark in zip(names, marks) if mark == lowest_score]

    print(f"\n[TOP] Highest Score: {highest_score:.2f}")
    print(f"      Achieved by  : {', '.join(top_achievers)}")

    print(f"\n[LOW] Lowest Score : {lowest_score:.2f}")
    print(f"      Achieved by  : {', '.join(lowest_achievers)}")


def show_class_average(names, marks):
    """
    Calculate and display the class average marks using sum() and len().

    Parameters:
        names (list): List of student names.
        marks (list): List of student marks.
    """
    print("\n--- [6] Class Average ---")
    if not names:
        print("[!] No student records available to calculate average.")
        return

    # Use built-in sum() and len() functions
    total_marks = sum(marks)
    count = len(marks)
    average = total_marks / count

    print(f"Total Students : {count}")
    print(f"Total Marks    : {total_marks:.2f}")
    print(f"Class Average  : {average:.2f} / 100.00")


def delete_student(names, marks):
    """
    Delete a student record by name or serial number, keeping both lists synchronized.

    Parameters:
        names (list): List of student names.
        marks (list): List of student marks.
    """
    print("\n--- [7] Delete a Student ---")
    if not names:
        print("[!] No student records available to delete.")
        return

    print("Delete by:")
    print("1. Student Name")
    print("2. Serial Number (from View List)")
    method = input("Enter choice (1 or 2): ").strip()

    if method == '1':
        target_name = get_valid_name("Enter student name to delete: ")
        # Find all occurrences of target_name (case-insensitive)
        matching_indices = [
            i for i, name in enumerate(names)
            if name.lower() == target_name.lower()
        ]

        if not matching_indices:
            print(f"[!] No student found with name '{target_name}'.")
            return

        if len(matching_indices) == 1:
            idx = matching_indices[0]
            del_name = names[idx]
            del_mark = marks[idx]
            confirm = input(
                f"Are you sure you want to delete '{del_name}' (Marks: {del_mark:.2f})? (y/n): "
            ).strip().lower()

            if confirm == 'y':
                # Remove from both lists synchronously
                removed_name = names.pop(idx)
                removed_mark = marks.pop(idx)
                print(f"[+] Deleted {removed_name} (Marks: {removed_mark:.2f}) successfully.")
            else:
                print("[-] Deletion cancelled.")

        else:
            # Handle duplicate names by showing them with indices
            print(f"[!] Multiple records found with name '{target_name}':")
            for pos, idx in enumerate(matching_indices, start=1):
                print(f"  {pos}. #{idx + 1} {names[idx]} (Marks: {marks[idx]:.2f})")

            choice = input("Enter the number (1, 2, ...) of the record to delete: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(matching_indices):
                selected_idx = matching_indices[int(choice) - 1]
                removed_name = names.pop(selected_idx)
                removed_mark = marks.pop(selected_idx)
                print(f"[+] Deleted {removed_name} (Marks: {removed_mark:.2f}) successfully.")
            else:
                print("[!] Invalid selection. Deletion cancelled.")

    elif method == '2':
        view_students(names, marks)
        sno_input = input("Enter the Serial Number (S.No) of the student to delete: ").strip()
        if sno_input.isdigit():
            sno = int(sno_input)
            if 1 <= sno <= len(names):
                idx = sno - 1
                del_name = names[idx]
                del_mark = marks[idx]
                confirm = input(
                    f"Are you sure you want to delete #{sno} '{del_name}' (Marks: {del_mark:.2f})? (y/n): "
                ).strip().lower()

                if confirm == 'y':
                    # Remove from both lists synchronously
                    removed_name = names.pop(idx)
                    removed_mark = marks.pop(idx)
                    print(f"[+] Deleted #{sno} {removed_name} (Marks: {removed_mark:.2f}) successfully.")
                else:
                    print("[-] Deletion cancelled.")
            else:
                print(f"[!] Error: Serial number must be between 1 and {len(names)}.")
        else:
            print("[!] Error: Please enter a valid numeric serial number.")

    else:
        print("[!] Invalid choice. Returning to main menu.")


def load_sample_students():
    """
    Return pre-loaded sample student names and marks for quick testing/demo.

    Returns:
        tuple: (list of names, list of marks)
    """
    sample_names = [
        "Aarav Sharma",
        "Diya Patel",
        "Rohan Mehta",
        "Sneha Rao",
        "Vikram Singh"
    ]
    sample_marks = [
        88.5,
        94.0,
        76.5,
        94.0,
        62.0
    ]
    return sample_names, sample_marks


def main():
    """Main function to run the student records application."""
    print("Welcome to the Student Records Management System!")
    print("Pre-loading sample student records for demonstration...")

    # Initialize parallel lists with 5 sample students
    names, marks = load_sample_students()
    print(f"[+] Loaded {len(names)} sample records.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            add_student(names, marks)
        elif choice == '2':
            view_students(names, marks)
        elif choice == '3':
            search_student(names, marks)
        elif choice == '4':
            sort_students(names, marks)
        elif choice == '5':
            show_highest_lowest(names, marks)
        elif choice == '6':
            show_class_average(names, marks)
        elif choice == '7':
            delete_student(names, marks)
        elif choice == '8':
            print("\nThank you for using Student Records Management System. Goodbye!\n")
            break
        else:
            print("[!] Invalid option. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
