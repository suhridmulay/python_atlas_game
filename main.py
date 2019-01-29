#Importing sys for exit
import sys

names = {
    #This is a dictionary containing names of countries
    #Conatins dummy names for now
    #TODO: Add actual country names
    'B' : ['Ba', 'Bb', 'Bc', '\0'],
    'A' : ['Aa', 'Ab', 'Ac', '\0'],
    'C' : ['Ca', 'Cb', 'Cc', '\0']
}

#This counts which numbered country of a particular letter we are using
#For instance counter[0] = 1 implies 2nd country in the 'A' list
counter = [0] * 3

#This is a list for user strings max length hundred
user_used = []

#This function provides the user with a reply from the computer
#Exits if it loses
def reply(end_letter:str):
    op_list = names[end_letter]
    pntr = ord(end_letter) - 65
    count = counter[pntr]
    repl =  op_list[count]
    if repl == '\0':
        print('You win human....')
        sys.exit(0)
    else:
        counter[pntr] = counter[pntr] + 1
        return repl

#This method checks whether the country user enters exists in list or not
#If it does not exist the user automatically loses
def country_exists(country_name:str):
    letter = country_name[0].upper()
    countries = names[letter]
    if country_name.capitalize() in countries:
        return 1
    else:
        print("User loses because of invalid input (non-existent country)")
        sys.exit()

#This method checks whether the computer has already used the country name
def is_not_used(country_name:str):
    countries = names[country_name[0].upper()]
    index = countries.index(country_name)
    ptr = ord(country_name[0]) - 65
    if index >= counter[ptr]:
        return 1
    else:
        print("User loses due to repetition")
        sys.exit()




print('Welcome to the game: ')
r = '\0'
while True:
    country_in = input('Please enter a country name (or Q to quit): ')
    #This is the exit part. Called when you quit the game
    if country_in == 'Q':
        print("You noob You quit !")
        sys.exit(0)
    
    #These are some implemented checks
    #this checks whether country exists
    country_exists(country_in)

    #This checks whether the last letter of computer's answer and first letter of users input match
    if r != '\0':
        if r[len(r) - 1].upper() != country_in[0].upper():
            print("User loses due to letter mismatch")
            sys.exit(0)

    #This checks whether the computer has not already used the country name
    is_not_used(country_in)

    #These lines check whether the user has used the country
    if country_in in user_used:
        print('User loses due to repetition')
        sys.exit(0)

    #This is the actual reply part which only answers if all above checks are fulfilled
    r = reply(country_in[len(country_in) - 1].upper())
    user_used.append(country_in)
    print(r)
    
