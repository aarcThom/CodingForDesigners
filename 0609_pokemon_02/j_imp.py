import json # import the json library

def import_json():
    with open("data/pokemon.json", mode="r", encoding="utf-8") as context_manager:
        pokedex = json.load(context_manager)
        return pokedex