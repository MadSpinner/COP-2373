
#This program mainly utilizes regular expressions, so import re
import re

#Note: I feel like I should be using a class to contain these functions

def is_phone_number_valid(user_phone_number):
    '''
    Matches user's phone number with the raw string of the format of a phone number.
    Parameters:
        user_phone_number (string): The user's phone number that is being checked.
    Variables:
        phone_number_pattern (re.pattern): The correct format of a phone number.
    Logic:
        1. Initializes phone_number_pattern.
        2. Checks to see of the pattern matches the parameter.
        3. If it matches returns true.
        4. Else, it returns false.
    Return:
        Boolean: Returns either True or False based on whether the parameter matches the format.
    '''

    #checks if the format is 3 digits, 3 digits, 4 digits. The seperator can be interchangeable between space and hyphen
    phone_number_pattern = re.compile(r'\d{3}[ -]\d{3}[ -]\d{4}')
    #I ran type on this and it came up re.pattern


    if re.fullmatch(phone_number_pattern, user_phone_number):
        return True
    else:
        return False

def is_social_security_number_valid(user_social_security_number):
    '''
    Matches user's ssn with the raw string of the format of a ssn.
    Parameters:
        user_social_security_number (string): The user's social security number that is being checked.
    Variables:
        social_security_number_pattern (re.pattern): The correct format of a social security number.
    Logic:
        1. Initializes social_security_number_pattern.
        2. Checks to see of the pattern matches the parameter.
        3. If it matches returns true.
        4. Else, it returns false.
    Return:
        Boolean: Returns either True or False based on whether the parameter matches the format.
    '''

    #checks if the format is 3 digits, 2 digits, 4 digits. The seperator can be interchangeable between space and hyphen
    social_security_number_pattern = re.compile(r'\d{3}[ -]\d{2}[ -]\d{4}')

    if re.fullmatch(social_security_number_pattern, user_social_security_number):
        return True
    else:
        return False

def is_zip_code_valid(user_zip_code):
    '''
    Matches user's zip code with the raw string of the format of a zip code.
    Parameters:
        user_zip_code (string): The user's zip code that is being checked.
    Variables:
        zip_code_pattern (re.pattern): The correct format of a zip code.
    Logic:
        1. Initializes zip_code_pattern.
        2. Checks to see of the pattern matches the parameter.
        3. If it matches returns true.
        4. Else, it returns false.
    Return:
        Boolean: Returns either True or False based on whether the parameter matches the format.
    '''

    #checks if the format is 5 digits. The seperator can be interchangeable between space and hyphen
    zip_code_pattern = re.compile(r'\d{5}')

    if re.fullmatch(zip_code_pattern, user_zip_code):
        return True
    else:
        return False

if __name__ == '__main__':

    user_phone_number = input('Please input your phone number using the correct format:\t')
    user_social_security_number = input('Please input your social security number using the correct format:\t')
    user_zip_code = input('Please input your zip code using the correct format:\t')

    user_phone_number_validity = is_phone_number_valid(user_phone_number)
    user_social_security_number_validity = is_social_security_number_valid(user_social_security_number)
    user_zip_code_validity = is_zip_code_valid(user_zip_code)
    
    #This section below is a series of if statements that tells the user if they met the correct format

    if user_phone_number_validity: print('Your phone number is:\tValid')
        
    elif user_phone_number_validity == False: print('Your phone number is:\tInvalid')
        
    if user_social_security_number_validity: print('Your social security number is:\tValid')
        
    elif user_social_security_number_validity == False: print('Your social security number is:\tInvalid')
        
    if user_zip_code_validity: print('Your zip code is:\tValid')
        
    elif user_zip_code_validity == False: print('Your zip code is:\tInvalid')
        
    if user_phone_number_validity == user_social_security_number_validity == user_zip_code_validity and user_zip_code_validity == True:

        #I didn't make this single line as it went off-screen
        print('\nCongratulations! Everything is valid.')

    else: print('\nPlease run the program again but with the correct formatting.')