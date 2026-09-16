


def check_email(list_of_phrases, email):
    """
    Checks user email to see if it contains spam messages

    Parameters:
        list_of_phrases (list): list of phrases that are considered spam
        email (str): email that could possibly be spam
    Variables:
        spam_score (int): The number goes up every time a spam phrase is found
        phrase(str): The current index of list_of_phrases
    Logic:
        1. Initializes accumulator
        2. Checks to see if there is an email
        3. Loops through list of phrases to check if a phrase is found in the email
    Return:
        Accumulator: the amount of spam messages found
    """
    spam_score = 0

    #checks to see if email is there
    if email == None or email == '':

        print ('There is no email, please restart the program but with an email')
        return

    #loops phrases through email
    for phrase in list_of_phrases:
        
        if str(phrase).lower() in str(email).lower():
            
            spam_score += 1

    #returns accumulator
    return spam_score

def get_email():
    """
    Returns the user's email to the program
    
    Parameters:
        None
    Variables:
        None
    Logic:
        1. Asks the user for the suspected spam email and returns it
    Return:
        String: This function returns a user's email
    """

    #I decided to save on space by putting the command on the return line
    return str(input('Please place the suspected spam email:\t'))

#I probably should change the numbers so that they aren't mysterious, but those numbers are the threshold in my mind.
def spam_score_responses(score):
    """
    Based on spam score the void function prints how likely the email is spam.

    Parameters:
        Score (int): Amount of spam phrases found in email
    Variables:
        None
    Logic:
        1. Checks if score is above 15, if so it prints message
        2. Checks if score is above 5, if so it prints message
        3. Checks if score isn't 0, if so it prints message
        4. Checks if score is 0, if so it prints message
        5. if anything else, print error message
    Return:
        None
    """
    if score >= 16: print(f'Your email contains {score} spam phrases. There is a high chance that this email is spam.')
    elif score >= 6: print(f'Your email contains {score} spam phrases. There is a medium chance this email is spam.')
    elif score > 0: print(f'Your email contains {score} spam phrases. There is a low chance this email is spam.')
    elif score == 0: print('There are no commonly used spam phrases in your email. Remember to stay safe out there.')
    else: print('An error has most likely occured.')
    

if __name__ == "__main__":

    #took 32 phrases from this site https://www.activecampaign.com/blog/spam-words
    # I don't know if I can make this neater 
    list_of_spam = [
                    '#1','100%','Potential earnings','Once in a lifetime','Risk-free','Satisfaction guaranteed','Giveaway',
                    'Act now','Limited time','Please read','Urgent','You have been selected','Dear friend',"This won't last",
                    'No fees','Financial freedom','Free money','Incredible deal','Do it today',"Don't delete",'Join millions',
                    'Terms and conditions','Not junk','Not spam','No strings attached',"This isn't a scam",'Requires initial investment',
                    'No hidden','Multi-level marketing','Congratulations','All new','As seen on'
                    ]

    #asks user for email
    user_email = get_email()

    """
    Test emails I'll be using to check: #note that last two emails are seperated into multiple lines.

    Hey your doorbell isn't working and I am currently stuck outside your home. (Should contain 0 spam messages)

    Dear friend, please send over the homework file. This is urgent! (Should contain 2 spam messages)

    Don't delete this email. Our #1 product has the potential to gain you financial freedom! No strings attached!
    Join millions for the all new product as seen on hit T.V show how-to-scam! No hidden fees! (Should contain 8 spam messages)
    
    Dear friend, please read! You have been selected for an incredible deal. 
    Join this Once in a lifetime giveaway for a chance at free money! This won't last as it is VERY urgent. 100% satisfaction guaranteed! 
    Requires initial investment to start your journey to financial freedom! Act now and this no strings attached deal can be yours. 
    Congratulations on your risk-free limited time only deal. Do it today! (Should contain 19 spam messages)
    """
    #checks email to see if it matches with the spam phrases
    spam_score = check_email(list_of_spam, user_email)

    #made it a void function as all it does is display possible responses
    spam_score_responses(spam_score)