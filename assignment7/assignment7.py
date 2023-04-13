# assignment7.py
# Matt Zagame
# 3/22/23
# The following program prompts the user for all computer science courses they
# have taken and recommends which courses they should take next. The program
# makes the assumption that all courses 2 or more levels above the current level
# have prerequisites that have not been met and separates those courses.

# Define the max courses taken per year
MAX_COURSES = 8

# Define the valid cs courses
cs_courses = {
    1010: "COMP.1010 Computing I",
    1020: "COMP.1020 Computing II",
    1030: "COMP.1030 Computing I Lab",
    1040: "COMP.1040 Computing II Lab",
    2010: "COMP.2010 Computing III",
    2030: "COMP.2030 Assembly Language Programming",
    2040: "COMP.2040 Computing IV",
    3010: "COMP.3010 Organization of Programming Languages",
    3040: "COMP.3040 Foundations of Computer Science",
    3050: "COMP.3050 Computer Architecture",
    3080: "COMP.3080 Operating Systems",
    4040: "COMP.4040 Analysis of Algorithms"
}

# Prompt user to enter courses they have taken
courses_taken = input(
    "Enter all computer science courses taken by course number, separated by commas: ").split(",")

# Check for valid course numbers and get user course level
if courses_taken[0] != '':
    try:
        # Convert the user's input to integers
        courses_taken = [int(course.strip()) for course in courses_taken]
        for course in courses_taken:
            if course not in cs_courses:
                raise ValueError
    except ValueError:
        print("Please enter valid cs course numbers separated by a comma, or simply hit enter if no cs courses have been taken")
        exit(1)
    course_level = int(max(courses_taken) / 1000)
else:
    course_level = 0

# Get the courses the user should take next
courses_next = []
courses_remaining = []
count = 0
for course_num, course_name in cs_courses.items():
    if course_num not in courses_taken:
        if int(course_num / 1000) - course_level <= 1 and count < MAX_COURSES:
            # Add courses the user can take next year
            courses_next.append(course_name)
        else:
            # Add courses with additional prerequisites
            courses_remaining.append(course_name)
        count += 1

# Output the recommended courses
if courses_next:
    print("You should take the following courses next year:")
    for course in courses_next:
        print(course)
if courses_remaining:
    print("----------------------------------------")
    print("Courses remaining with prerequisites:")
    for course in courses_remaining:
        print(course)
if not courses_next and not courses_remaining:
    print("You have taken every required computer science course!")
