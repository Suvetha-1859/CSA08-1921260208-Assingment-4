TASK 4 – FILE AND EXCEPTION FORENSICS

Personal Details

- Name: Suvetha.S
- Register Number: 1921260208
- Python Version: Python 3.x

Objective

To identify and correct file-handling errors in a Python program using append mode, newline characters, "with" statements and exception handling.

Concepts Used

- File handling
- File modes ("r", "w", "a")
- Append mode
- "with" statement
- Exception handling
- "try-except" blocks
- Error logging
- Newline character ("\n")

Program Description

The program processes daily book-return records from three input files. The original program demonstrates data loss and missing newline problems.

The corrected program uses append mode to preserve previous records, newline characters to separate book names, and "with" statements to close files automatically. It also records missing-file errors in an error log.

Input Files

- "day1.txt"
- "day2.txt"
- "day3.txt"

Output Files

- "returns_old.log" – Demonstrates the defective output.
- "returns.log" – Stores all returned book records.
- "error.log" – Stores file-related errors.

Expected Output

The corrected log contains all six book records from the three days.

The error log records the missing "day4.txt" file.

Time Complexity

O(n) – Each book record is processed once.

Conclusion

This task demonstrates how proper file handling prevents data loss and improves program reliability through append mode, automatic file closing and error logging.

Files Included

- "task4.py" – Python source code
- "README.md" – Task documentation
- "day1.txt", "day2.txt", "day3.txt" – Sample input files
- "returns.log" – Corrected output file
- "returns_old.log" – Defective output file
- "error.log" – Error log
- "output.png" – Program execution screenshot
