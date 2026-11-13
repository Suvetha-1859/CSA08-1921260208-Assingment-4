CSA08 – PYTHON PROGRAMMING

ASSIGNMENT 4 – CO4

Student Details

- Name: Suvetha.S
- Register Number: 1921260208
- Department: B.Tech Information Technology
- 
- Course Code: CSA08
- Course: Python Programming
- Course Outcome: CO4
- Assignment: Assignment 4
- Task: Task 2 – From Requirement to File-Processing Design

---

1. Objective

To design a biometric attendance processing system that reads daily attendance files, calculates monthly attendance percentages, identifies students below 75% attendance and records damaged lines.

2. Concepts Used

- File Handling
- Dictionary
- Lists and Tuples
- Python pathlib Module
- File Modes
- Pseudocode
- Data Processing
- Exception Handling

3. Input File Format

Each daily attendance file contains:

- Register Number
- Date
- Attendance Status (P/A)

Example:

192311001,2026-10-01,P
192311002,2026-10-01,A
192311003,2026-10-01,P

4. Data Structures

- Dictionary: Stores present and absent counts for each student.
- List: Stores damaged attendance records.
- Tuple: Stores attendance count information.

5. File Operations

- "r" – Read attendance files.
- "w" – Write monthly attendance reports.
- "a" – Append additional records when required.
- "with open()" – Safely opens and closes files.
- "UTF-8" – File encoding.

6. Processing Method

1. Identify all daily attendance files using pathlib.
2. Read each file line by line.
3. Validate the attendance records.
4. Accumulate present and absent counts using a dictionary.
5. Calculate attendance percentages.
6. Identify students below 75%.
7. Record damaged lines with filenames and line numbers.
8. Generate the monthly reports.

7. Output Files

attendance_report.txt

- Register number
- Present days
- Absent days
- Attendance percentage
- Students below 75%

damaged_records.txt

- File name
- Line number
- Damaged record details

8. Complexity Analysis

- Dictionary Method: O(f × l)
- Re-reading Method: O(s × f × l)

Where:

- s = Number of students
- f = Number of daily files
- l = Number of lines per file

The dictionary method is more efficient because each file is processed only once.

9. Conclusion

The biometric attendance processing design provides an efficient method for calculating monthly attendance percentages. It identifies students below 75% attendance and records damaged data for correction. Using dictionaries and line-by-line file processing improves efficiency and reduces unnecessary memory usage.

---


