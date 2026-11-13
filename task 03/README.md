TASK 3 – FILE AND EXCEPTION HANDLING IN PYTHON

Personal Details

- Name: Suvetha.S
- Register Number: 1921260208
- Python Version: Python 3.x

Objective

To implement a Python program using exception handling techniques to process attendance records, identify invalid records, and handle file-related errors.

Concepts Used

- User-defined exceptions
- try, except, else, and finally blocks
- raise statement
- File handling
- Specific exception handling
- Error tracking and reporting

Program Description

The program reads attendance records from a file and checks whether each record contains exactly three fields: register number, date, and attendance status.

It accepts only P (Present) and A (Absent) as valid attendance statuses. Invalid records are identified and stored with their line numbers.

Custom Exception

A user-defined exception named "InvalidRecord" is created to identify records with missing fields or invalid attendance status.

Expected Output

(1, 1, [(3, 'expected 3 fields, found 2'), (4, "invalid status 'L'")])

Error Handling

The program handles:

- FileNotFoundError
- PermissionError
- InvalidRecord

Time Complexity

O(n) – Each line in the attendance file is processed once.

Conclusion

This task demonstrates how Python exception handling improves program reliability. It helps identify invalid attendance records, manage file-related errors, and prevent unexpected program termination.

Files Included

- "task3.py" – Python source code
- "README.md" – Task documentation
- "output.png" – Program execution screenshot
