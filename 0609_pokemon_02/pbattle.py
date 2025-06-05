import random

def _get_multiplier(attacker:str, defender:str, pokedex:dict) -> float:
    """Get's the attack multiplier for a pokemon

    Args:
        attacker (str): The attacking monster
        defender (str): The monster that is being attacked.
        pokedex (dict): The pokemon dictionary

    Returns:
        float: The multiplier
    """

    # get the dictionaries for each pokemon name
    attack_stats = pokedex[attacker]
    defend_stats = pokedex[defender]

    # get the two types of the second pokemon
    attacker_types = []
    if attack_stats["type1"] != None: 
        attacker_types.append(attack_stats["type1"])
    if attack_stats["type2"] != None: 
        attacker_types.append(attack_stats["type2"])

    # create a base multiplier
    multiplier = 1

    #adjust the multiplier for each of defenders types
    for mon_type in attacker_types:
        mult_key = f"against_{mon_type}" # for example 'bug' -> 'against_bug' - get the key for mon1 dict
        mult_val = defend_stats[mult_key]
        multiplier *= mult_val # multiply the multiplier

    return multiplier  

def attack(attacker:str, defender:str, pokedex:dict) -> float:
    """Calculates the damage done from an attack

    Args:
        attacker(str): Attacker's name
        defender (str): Defender's name
        pokedex (dict): Pokemon dictionary

    Returns:
        float: Damage dealt
    """


    # calculating the damge ------------------------------------

    # get the dictionaries for each pokemon name
    attacker_stats = pokedex[attacker]
    defender_stats = pokedex[defender]

    # calculate attack multiplier
    att_mult = _get_multiplier(attacker, defender, pokedex)

    # calculate damage
    damage = attacker_stats["attack"] * att_mult - defender_stats["defense"] / att_mult

    # just in case
    if damage <= 0:
        damage = 5.0

    # creating a message ------------------------------

    # effectiveness of the attack
    if damage <= 5: 
        effect_lvl = "It's not very effective!"
    elif damage >= 100:
        effect_lvl = "It's VERY effective!"
    else:
        effect_lvl = "" # No comment on the effect level

    # choosing a random attack ability
    ability = random.choice(attacker_stats["abilities"])

    # compose and print the message
    attack_msg = f"{attacker} uses {ability} on {defender}. {effect_lvl}"
    print(attack_msg)

    return damage