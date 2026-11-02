import csv

#this is the result of being on stack overflow for way too long
def read_csv_file(csv_file_name):
    '''
    reads the csv file based on the parameter.
    Parameters:
        csv_file_name (str): The name of the file being read. It has to be a csv file to work.
    Variables:
        file_reader (_csv.reader): This is used to read the csv rows. It is used twice (I should probably change that, but the name is practical).
        max_length_in_csv_file (list): A list that takes in the max of each row in the csv file, then is used as the width of the center method.
    Logic:
        1. Opens parameter to read.
        2. Reads and appends the longest maximum of each row to the list.
        3. Opens parameter again to read.
        4. inside of for loop display the data after centering based on the maximum of the list.
    Return:
        None
    '''
    with open(csv_file_name, 'r', newline='') as csv_file:

        file_reader = csv.reader(csv_file)

        max_length_in_csv_file = []

        #should take the longest index and append it to max_length_in_csv_file
        for row in file_reader:    max_length_in_csv_file.append(len(max(row)))

    #csv doesn't have a seek command so I have to reopen the file
    with open(csv_file_name, 'r', newline='') as csv_file:

        file_reader = csv.reader(csv_file)

        for row in file_reader:

            for index in range(len(row)):

                #replaces each index in the row with a centered version of itself
                row[index] = row[index].center(max(max_length_in_csv_file))

            #displays the centered row
            print(', '.join(row))

if __name__ == '__main__':
    #90% sure this doesn't have to be assigned to something
    read_csv_file('grades.csv')