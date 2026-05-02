# GradeMaster: Teacher Grading System
# Group Members: Ceniza, Doloriel
# Description: Automatically computes grades with weighted scores, 
#              shows remarks and passing/failing status

# -------------------------- FUNCTIONS --------------------------
def get_valid_input(prompt, min_num=0, max_num=100):
    # Check if input is valid number within range
    while True:
        try:
            value = float(input(prompt))
            if min_num <= value <= max_num:
                return value
            print("Oops! Enter number from " + str(min_num) + " to " + str(max_num) + " only")
        except ValueError:
            print("Invalid input! Numbers only please~")
            
def compute_subject_grade(formative, alternative, summative):
    # Calculate grade: 25% Formative, 30% Alternative, 45% Summative
    return (formative * 0.25) + (alternative * 0.30) + (summative * 0.45)

def get_remark_and_status(average):
    # Get performance remark and passing status
    if average >= 90:
        remark = "Excellent"
    elif average >= 80:
        remark = "Good"
    else:
        remark = "Needs Improvement"
    
    status = "Passing" if average >= 75 else "Failing"
    return remark, status

# -------------------------- MAIN PROGRAM --------------------------
print("===== GRADEMASTER: TEACHER GRADING SYSTEM =====")
print()

# Get number of students
num_students = int(get_valid_input("Enter total number of students: ", min_num=1))
subjects = ["English", "Math", "Science", "Computer Science", "Social Science"]

# Process each student
for student_num in range(num_students):
    print("\n----- STUDENT " + str(student_num + 1) + " DETAILS -----")
    name = input("Enter student name: ")
    
    total = 0
    all_grades = []

    # Get scores per subject
    for subject in subjects:
        print("\n--- " + subject + " ---")
        formative = get_valid_input("Formative Score: ")
        alternative = get_valid_input("Alternative Score: ")
        summative = get_valid_input("Summative Score: ")

        grade = compute_subject_grade(formative, alternative, summative)
        all_grades.append(grade)
        total += grade

    # Compute results
    average = total / len(subjects)
    highest = max(all_grades)
    lowest = min(all_grades)
    remark, status = get_remark_and_status(average)

    # Display results
    print("\n" + "-"*50)
    print("Student Name: " + name)
    print("Overall Average: " + str(round(average, 2)))
    print("Highest Grade: " + str(round(highest, 2)))
    print("Lowest Grade: " + str(round(lowest, 2)))
    print("Remark: " + remark)
    print("Status: " + status)
    print("-"*50)

print("\nAll done! Thank you for using GradeMaster!:)")
