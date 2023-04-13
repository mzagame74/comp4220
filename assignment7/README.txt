Matt Zagame
Machine Learning
March 22, 2023
Assignment 7

assigment7.py prompts the user for all UML computer science courses they have
taken by course number and recommends which courses they should take over the
next year. A dictionary between course numbers and course titles is used to
define a vocabulary of valid cs courses. The user must enter valid cs courses
or simply hit enter to see the courses they should take next as well as courses
remaining with prerequisites. The highest level course taken is used to
establish which courses are available to take over the next year.

Currently, the program only works with required cs courses and makes the
assumption that all courses 2 or more levels above the current level have
prerequisites that have not been met. A more complete solution for devising a
program of study would involve asking questions about the student to also
suggest elective courses and accurately handling prerequisite courses. For
instance, the program could ask simple yes/no questions about a student's
interests to influence the suggestion of elective courses or project sequences.
Additionally, each course not yet taken should map to the appropriate
prerequisite courses in order to determine which courses are eligible to be
taken next. Given this information, the program would need to check several
conditions before recommending a program of study.
