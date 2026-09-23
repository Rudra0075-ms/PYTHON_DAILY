course1 = {"Ram", "sita", "rudra", "sai", "madhab"}

course2 = {"sita", "madhab", "radha", "priya", "gita"}


print("\nCourse 1 Students:", course1)
print("Course 2 Students:", course2)

both_courses = course1 & course2
print("\nStudents enrolled in BOTH courses:")
print("  ", both_courses)

only_course1 = course1 - course2
print("\nStudents enrolled ONLY in Course 1:")
print("  ", only_course1)

only_course2 = course2 - course1
print("\nStudents enrolled ONLY in Course 2:")
print("  ", only_course2)

all_students = course1 | course2
print("\nAll students enrolled in either course:")
print("  ", all_students)

print(f"Total unique students: {len(all_students)}")
