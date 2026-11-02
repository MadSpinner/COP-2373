import csv

def create_student_grades_csv(number_of_students):
    '''
    Takes the amount of students and uses user input to add elements to a csv file.
    Parameters:
        number_of_students (int): The amount of students that was inputed into the program.
    Variables:
        student_writer (_csv.writer): This is used to write the csv rows.
        student_first_name (str): Takes user input to grab a student's first name.
        student_last_name (str): Takes user input to grab a student's last name.
        student_first_exam (int): Takes user input to grab a student's first exam score.
        student_second_exam (int): Takes user input to grab a student's second exam score.
        student_third_exam (int): Takes user input to grab a student's third exam score.
    Logic:
        1. Opens grades.csv to write.
        2. Writes the headers.
        3. runs a for loop to gain user data.
        4. inside of for loop write the user data to the next row.
        5. inform user when the program is complete.
    Return:
        None
    '''

    with open('grades.csv','w', newline='') as csv_file:
        student_writer = csv.writer(csv_file)

        student_writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2','Exam 3'])

        #starts the range at 1 so the prompts make sense to user
        for n in range( 1, number_of_students + 1):

            #placed all variables tabs close to eachother for better readability.
            student_first_name = input(f"Please enter the {n} student's first name:\t")

            student_last_name = input(f"Please enter the {n} student's last name:  \t")

            student_first_exam = int(input(f"Please enter the {n} student's exam 1 grade: \t"))

            student_second_exam = int(input(f"Please enter the {n} student's exam 2 grade:\t"))

            student_third_exam = int(input(f"Please enter the {n} student's exam 3 grade: \t"))

            student_writer.writerow([student_first_name, student_last_name, student_first_exam, student_second_exam, student_third_exam])

        print('All students have been added to the file')


if __name__ == '__main__':

    number_of_students = int(input('Please enter the amount of students you have:\t'))

    if not number_of_students or number_of_students <= 0: print('You have no students.')
    else: create_student_grades_csv(number_of_students)