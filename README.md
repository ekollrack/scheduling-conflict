# Scheduling Conflict Program
## Developed for the University of Vermont Tutoring Center

### Program Description
This Python program checks for scheduling conflicts between tutoring times and lecture schedules based on a provided CSV file of enrollment data. Users enter their tutoring time slots, specify the day, and choose a course to verify if any of their tutoring sessions conflict with lecture times on a specific day.

### Features
- **User Input**: Enter multiple tutoring slots in `hh:mm AM/PM-hh:mm AM/PM` format, separated by commas.
- **Conflict Detection**: Compares tutoring times with course lecture times for potential conflicts.
- **Flexible Day Selection**: Users select the day (Monday through Friday) to match with lecture schedules.
- **Multiple Course Checking**: Check conflicts for more than one course in a single session.

### Requirements
- **Python 3.x**
- **pandas library** (install via `pip install pandas` in terminal)

### How To Run:

#### Terminal
1. Ensure Python 3 and Pandas are installed.
2. Navigate to the directory containing the program files and run:

- Mac: Go to Terminal and enter 'python main.py' or 'python3 main.py'
- Windows:

#### PyCharm (free with educational license)
1. Open PyCharm and the project containing main.py.
   - Either download the github code to your computer
2. Ensure the enrollment_f24.csv file is in the same directory as main.py.
3. Run the program by selecting the play button in the upper right corner

#### VSCode
1. Open the folder containing main.py in VSCode.
2. Ensure the enrollment file is in the same directory as main.py.
3. Open main.py in the editor and click the play button in the upper right corner


Enter your tutoring times in the format hh:mm AM/PM-hh:mm AM/PM, separated by commas for multiple slots:
10:00 AM-11:00 AM, 1:00 PM-2:00 PM
What day are these times for (only enter 1 day)?
Enter 'M' for Monday, 'T' for Tuesday, 'W' for Wednesday, 'R' for Thursday, 'F' for Friday:
M
Enter course abbreviation (e.g., 'CHEM'):
CHEM
Enter course number (e.g., 1400):
1400
Checking conflicts for CHEM 1400...
Conflict: Tutor slot 10:00 AM-11:00 AM and Lecture slot 10:15 AM-11:15 AM on Monday
Would you like to check another class? (yes/no):
no

***NOTE*** please make sure you follow the specified format when entering times. If you enter your times incorrectly, it should prompt you to enter the times again.








