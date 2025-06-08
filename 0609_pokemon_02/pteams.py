import json # import the json library
import random # using the random library


def load_pokedex() -> dict:
    """Load pokemon data from json

    Returns:
        dict: The pokedex.
    """
    # import our .json data
    with open("data/pokemon.json", mode="r", encoding="utf-8") as context_manager:
        pokedex = json.load(context_manager)
    return pokedex


# creating the pokemon selection function
def pick_mon(pokedex:dict) -> str:
    """Given user input, tests name of pokemon if in pokedex, or a random pokemon name if name not found.

    Args:
        pokedex (dict): Pokemon dictionary to search

    Returns:
        str: A pokemon name
    """

    #prompt the user for a pokemon name
    name = input("What pokemon do you want to add to your team?")

    # if the name is found, return it!
    if name.lower() in pokedex:
        print(f"Added {name} to your team!")
        return name
    
    # otherwise return a random name
    random_mon = random.choice(list(pokedex.keys())) # we need to convert the keys to a normal list to use the random.choice function
    print(f"Couldn't find {name}. {random_mon} was added to your team instead!")
    return random_mon


# picking multiple pokemon
def pick_team(team_num:int, pokedex:dict) -> list[str]:
    """Prompts user 'team_num' times to pick a pokemon.
       Returns a list of all picked pokemon names.

    Args:
        team_num (int): Number of pokemon on team
        pokedex (dict): The pokemon dictionary

    Returns:
        list[str]: The names of the pokemon on user's team
    """

    team = [] # create empty list to hold team member names

    # iterate 'team_num' times
    for i in range(team_num):
        team_member = pick_mon(pokedex) # run the pick pokemon function
        team.append(team_member) # add the member to the team
    
    return team


# creating a function to pick opponents' team
def opponent_team(num_mons:int, pokedex:dict) -> list[str]:
    """Given 'num_mons', returns that many pokemon for opponent's team.

    Args:
        num_mons (int): Number of pokemon on opponent's team
        pokedex (dict): Dictionary of pokemon

    Returns:
        list[str]: The names of the pokemon on opponent's team
    """

    team = [] # empty list to hold pokemon names

    for i in range(num_mons):
        random_mon = random.choice(list(pokedex.keys())) # pick a random pokemon
        team.append(random_mon) # Add it to the list

        # Add the message
        print(f"Your opponent chose {random_mon}!")

    return team