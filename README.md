# Scheduling Conflict Program
## Developed for the University of Vermont Tutoring Center

### Program Description
The Scheduling Conflict Program is a Python tool designed to help tutors at the University of Vermont check for conflicts between their tutoring sessions and class lecture schedules. Based on an enrollment CSV file, users can input their weekly tutoring time slots, specify the day, and select a course to verify if any conflicts exist with that day's lecture times.

### Features
- **User-Friendly Input**: Tutors can input multiple time slots in the format `hh:mm AM/PM-hh:mm AM/PM`, separated by commas for multiple slots.
- **Detailed Conflict Detection**: The program cross-checks tutoring times with course lecture times to identify any scheduling overlaps.
- **Flexible Day Selection**: Users select a single day (Monday through Friday) to check against lecture schedules for potential conflicts.  
  **Note:** Only one day can be checked per run of the program.
- **Multi-Course Checking**: Users can check for conflicts with multiple courses in one session, making it easy to review different courses without restarting the program.

### Requirements
- **Python 3.x**
- **pandas library**  
  *(Install via terminal: `pip install pandas`)*

### How To Run

#### Running from the Terminal
1. Ensure Python 3 and the Pandas library are installed.
2. Open a terminal, navigate to the directory containing `main.py`, and execute:

   ```bash
   python main.py

#### PyCharm (free with educational license)
1. Open PyCharm and the project containing main.py.
2. Ensure the enrollment_f24.csv file is in the same directory as main.py.
3. Run the program by selecting the play button in the upper right corner

#### VSCode
1. Open the folder containing main.py in VSCode.
2. Ensure the enrollment file is in the same directory as main.py.
3. Open main.py in the editor and click the play button in the upper right corner


Enter your tutoring times in the format hh:mm AM/PM-hh:mm AM/PM, separated by commas for multiple slots:
10:00 AM-11:00 AM, 01:00 PM-02:00 PM
What day are these times for (only enter 1 day)?
Enter 'M' for Monday, 'T' for Tuesday, 'W' for Wednesday, 'R' for Thursday, 'F' for Friday:
M
Enter course abbreviation (e.g., 'CHEM'): CHEM
Enter course number (e.g., 1400): 1400
Checking conflicts for CHEM 1400...
Conflict: Tutor slot 01:00 PM-02:00 PM and Lecture slot 01:10 PM-02:00 PM on Monday
Conflict: Tutor slot 10:00 AM-11:00 AM and Lecture slot 10:50 AM-11:40 AM on Monday
Would you like to check another class? (yes/no): yes
Enter course abbreviation (e.g., 'CHEM'): MATH
Enter course number (e.g., 1400): 1234
Checking conflicts for MATH 1234...
Conflict: Tutor slot 01:00 PM-02:00 PM and Lecture slot 01:10 PM-02:00 PM on Monday
Conflict: Tutor slot 10:00 AM-11:00 AM and Lecture slot 09:40 AM-10:30 AM on Monday
Conflict: Tutor slot 10:00 AM-11:00 AM and Lecture slot 10:50 AM-11:40 AM on Monday
Would you like to check another class? (yes/no): n


### Important Notes
- **Format Validation**: Please make sure to follow the specified format when entering tutoring times. If times are entered incorrectly, the program will prompt you to re-enter them until the format is correct.
- **Single Day Selection**: The program is designed to handle only one day at a time per run. To check for conflicts on a different day, simply rerun the program.

### Updating Enrollment Data
Each semester, the enrollment CSV file (`enrollment_f24.csv`) needs to be updated to reflect the current lecture schedules:
1. Download the updated schedule CSV file from the university.
2. Save it in the same directory as `main.py` with the name `enrollment_f24.csv`.

### Contributing
If you would like to make improvements to this program or add new features, feel free to fork this repository. 

### Contact Information
For questions, feedback, or support, please reach out:

**Author**: Elisabeth Kollrack  
**Email**: [elisabethkollrack@gmail.com](mailto:elisabethkollrack@gmail.com)








