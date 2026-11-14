
import csv

# Read student names from text file
try:
    with open("attendance.txt", "r") as file:
        original_names = file.readlines()

except FileNotFoundError:
    print("Attendance file not found!")
    original_names = []

# Clean names using list comprehension
cleaned_names = [
    name.strip().title()
    for name in original_names
    if name.strip()
]

# Find unique students using set
unique_students = set(cleaned_names)

# Sort student names alphabetically
sorted_students = sorted(unique_students)

# Save cleaned attendance to CSV file
with open("attendance_clean.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Student Name"])
    
    for student in sorted_students:
        writer.writerow([student])

# Display attendance summary
print("\n===== STUDENT ATTENDANCE REPORT =====")

print("Original Records:", len(original_names))
print("Unique Students:", len(unique_students))

print("\n----- CLEANED ATTENDANCE LIST -----")

for student in sorted_students:
    print(student)

print("\nCleaned attendance saved successfully!")
