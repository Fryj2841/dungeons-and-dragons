import characters

# D&D Character Creation Loop

def load_character(name: str) -> characters.Character:
    return characters.Character.load(name=name)

def create_character():
    # Character class selection
    class_choice = input("Choose a character class (Barbarian, Monk, Paladin, Ranger, Sorcerer, Warlock, Druid, Rogue): ")

    # Character name input
    character_name = input("Enter character name: ")

    # Character level input
    character_level = int(input("Enter character level: "))

    # Character creation based on class
    if class_choice.lower() == "barbarian":
        character = characters.Barbarian(character_name)
    elif class_choice.lower() == "monk":
        character = characters.Monk(character_name)
    elif class_choice.lower() == "paladin":
        character = characters.Paladin(character_name)
    # Add the remaining character classes here
    else:
        print("Invalid character class choice.")

    # Set character level
    character.level = character_level

    # Additional traits based on character class
    if isinstance(character, characters.Barbarian):
        character.rage_uses = int(input("Enter the number of rage uses: "))
    elif isinstance(character, characters.Monk):
        character.ki_points = int(input("Enter the number of ki points: "))
    elif isinstance(character, characters.Paladin):
        character.lay_on_hands_points = int(input("Enter the number of Lay on Hands points: "))
    # Add additional traits for the remaining character classes

    # Character summary
    print("\nCharacter Summary:")
    print(f"Name: {character.name}")
    print(f"Class: {character.__class__.__name__}")
    print(f"Level: {character.level}")
    if isinstance(character, characters.Barbarian):
        print(f"Rage Uses: {character.rage_uses}")
    elif isinstance(character, characters.Monk):
        print(f"Ki Points: {character.ki_points}")
    elif isinstance(character, characters.Paladin):
        print(f"Lay on Hands Points: {character.lay_on_hands_points}")
    # Add summary for the remaining character classes
        
    return character
    
    
if __name__ == "__main__":
    options_list = ['Character Creation Menu',
                    '1. Create New Character',
                    '2. Load Existing Character',
                    '3. Quit',
                    'Enter your choice (1-3):']
    
    # Character creation loop
    while True:
        choice = int(input('\n'.join(options_list)))

        if choice == 1:
            character = create_character()
            # Prompt for other character traits and assign them
            
            if input(f"do you wish to save this character named {character.name}? (Y/N)").lower() == 'y':
                character.save()
            else:
                print(f"exiting without saving character named {character.name}")

        elif choice == 2:
            name = input("Enter character name to load: ")
            loaded_character = characters.Character.load(name)

            if loaded_character:
                # Use the loaded character for further actions
                print("Loaded Character Summary:")
                print(f"Name: {loaded_character.name}")
                print(f"Level: {loaded_character.level}")
                print(f"Health: {loaded_character.current_hit_points}")
                print(f"Inventory: {loaded_character.inventory}")

        elif choice == 3:
            break