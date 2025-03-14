def print_scientists():
    scientists = [
        {"name": "Ada Lovelace", "birth_year": 1815},
        {"name": "Lise Meitner", "birth_year": 1878},
        {"name": "Cecila Payne", "birth_year": 1900},
        {"name": "Grace Hopper", "birth_year": 1906}
    ]
    
    for scientist in scientists:
        print(f"{scientist['name']} is a great scientist born in {scientist['birth_year']}.")


print_scientists()