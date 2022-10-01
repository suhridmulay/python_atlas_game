from functools import reduce
from os import path
import random
from typing import List

# Loads data from given country file
def load_data():
    def trim_and_lcase_string(s: str): 
        return s.strip().lower();

    country_file_path = path.join('.', 'assets', 'countries.txt')
    country_list: List[str] = []
    with open(country_file_path) as country_file:
        country_list = list(
            map(
                trim_and_lcase_string, 
                country_file.read().split('\n')
            )
        )
    
    def country_list_to_dict_reducer(accumulator: dict[str, list[str]], country: str):
        dictionary = accumulator
        letter = country[0]
        if (letter in dictionary.keys()): dictionary[letter].append(country)
        else: dictionary[letter] = [country]
        return dictionary

    country_dict = reduce(
        country_list_to_dict_reducer,
        country_list,
        {}
    )

    return country_list, country_dict

def choose_response(to: str, from_list: dict[str, list[str]], used_list: set[str]):
    last_letter = to[-1]
    # If there are no countries starting with required last letter
    # Player has won, we cannot respond
    if (last_letter not in from_list.keys()): return ''

    def country_name_is_valid(country_name: str, used_set: set[str]): return country_name not in used_set
    countries_ending_with_last_letter = from_list[last_letter]
    valid_reposnses = list(
        filter(
            lambda country: country_name_is_valid(country, used_list),
            countries_ending_with_last_letter
        )
    )
    
    # If there are no valid responses to the users answer return an empty string
    if (len(valid_reposnses) == 0): return ''
    # If there are return a random one
    else: return random.choice(valid_reposnses)

def main():
    country_list, country_dict = load_data()
    used_countries = set()
    WINNER = ''
    REASON = ''
    # Begin game loop
    while True:
        user_input = input('enter a country name (or q to lose by default): ').lower()

        # When user chooses to quit by default
        if (user_input == 'q'):
            print(f"User chose to default")
            WINNER = 'computer'
            REASON = 'user defaulted'
            break
        
        # When country user mentions has already been used 
        if (user_input in used_countries): 
            print(f"Country {user_input} has already been mentioned, you cannot mention it again")
            WINNER = 'COMPUTER'
            REASON = 'User forgot country already used'
            break

        # When country used by user is fictional or not present in computer data
        if (user_input not in country_list):
            print(f"Country {user_input} not found in list of countries, does it exist?")
            WINNER = 'computer'
            REASON = 'User made up a country'
            break;

        # If all checks pass
        # Add user mentioned country to the list of used countries
        used_countries.add(user_input)
        # Ask computer to come up with a response
        computer_response = choose_response(user_input, country_dict, used_countries)

        # When the computer response is blank
        if computer_response == '':
            print(f"Ok human, you win this time")
            WINNER = 'HUMAN'
            REASON = 'Computer knowledge exhausted'
            break;

        # Continue game as usual
        print(f"Computer responds with: {computer_response}")
        used_countries.add(computer_response)

    print(f"Well played USER and COMPUTER")
    print(f"The winner is {WINNER}")
    print(f"And the reason for their victory: {REASON}")

        


if __name__ == '__main__':
    main()