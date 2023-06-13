import os
import json
import random
import typing
from collections import OrderedDict

class Character:
    """_summary_
    """
    def __init__(self, name):
        """Generate a base character for D&D
        """
        self.player = None
        self.campaign = None
        self.creation_date = None
        self.current_xp = 0
        self.next_level_goal = 300
        self.name = name
        self.sheet_version = None
        self.race = None
        self.character_class = None
        self.alignment = None
        self.level = 1
        self.size = None
        self.base_speed = None
        self.speed_adjustment = 0
        self.adjusted_speed = None
        self.initiative_modifier = None
        self.initiative_adjustment = 0
        self.ability_scores = {
            "STR": None,
            "DEX": None,
            "CON": None,
            "INT": None,
            "WIS": None,
            "CHA": None
        }
        self.saving_throw_proficiency = {
            "STR": False,
            "DEX": False,
            "CON": False,
            "INT": False,
            "WIS": False,
            "CHA": False
        }
        self.saving_throw_adhoc_modifier = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0
        }
        self.armor_class = None
        self.max_hit_points = None
        self.current_hit_points = None
        self.temporary_hit_points = None
        self.hit_dice_type = None
        self.available_hit_dice = 1
        self.death_saves = {
            "successes": 0,
            "failures": 0
        }
        self.advantages = []
        self.disadvantages = []
        self.passive_perception = None
        self.passive_perception_adjustment = 0
        self.initiative = None
        self.inspiration = False
        self.proficiency = 2
        self.exhaustion = 0
        self.skills = {
            "Acrobatics": None,
            "Animal Handling": None,
            "Arcana": None,
            "Athletics": None,
            "Deception": None,
            "History": None,
            "Insight": None,
            "Intimidation": None,
            "Investigation": None,
            "Medicine": None,
            "Nature": None,
            "Perception": None,
            "Performance": None,
            "Persuasion": None,
            "Religion": None,
            "Sleight of Hand": None,
            "Stealth": None,
            "Survival": None
        }
        self.skills_expertise = []
        self.skills_half_proficiency = []
        self.skill_adjustments = {
            "Acrobatics": 0,
            "Animal Handling": 0,
            "Arcana": 0,
            "Athletics": 0,
            "Deception": 0,
            "History": 0,
            "Insight": 0,
            "Intimidation": 0,
            "Investigation": 0,
            "Medicine": 0,
            "Nature": 0,
            "Perception": 0,
            "Performance": 0,
            "Persuasion": 0,
            "Religion": 0,
            "Sleight of Hand": 0,
            "Stealth": 0,
            "Survival": 0
        }
        self.saving_throw_proficiency = {
            "STR": False,
            "DEX": False,
            "CON": False,
            "INT": False,
            "WIS": False,
            "CHA": False
        }
        self.saving_throw_adhoc_modifier = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0
        }
        self.armor_class = None
        self.max_hit_points = None
        self.current_hit_points = None
        self.temporary_hit_points = None
        self.hit_dice_type = None
        self.available_hit_dice = 1
        self.death_saves = {
            "successes": 0,
            "failures": 0
        }
        self.advantages = []
        self.disadvantages = []
        self.passive_perception = None
        self.passive_perception_adjustment = 0
        self.initiative = None
        self.inspiration = False
        self.proficiency = 2
        self.exhaustion = 0
        self.skills = {
            "Acrobatics": None,
            "Animal Handling": None,
            "Arcana": None,
            "Athletics": None,
            "Deception": None,
            "History": None,
            "Insight": None,
            "Intimidation": None,
            "Investigation": None,
            "Medicine": None,
            "Nature": None,
            "Perception": None,
            "Performance": None,
            "Persuasion": None,
            "Religion": None,
            "Sleight of Hand": None,
            "Stealth": None,
            "Survival": None
        }
        self.skills_expertise = []
        self.skills_half_proficiency = []
        self.skill_adjustments = {
            "Acrobatics": 0,
            "Animal Handling": 0,
            "Arcana": 0,
            "Athletics": 0,
            "Deception": 0,
            "History": 0,
            "Insight": 0,
            "Intimidation": 0,
            "Investigation": 0,
            "Medicine": 0,
            "Nature": 0,
            "Perception": 0,
            "Performance": 0,
            "Persuasion": 0,
            "Religion": 0,
            "Sleight of Hand": 0,
            "Stealth": 0,
            "Survival": 0
        }
        self.inventory = OrderedDict()

    def add_item_to_inventory(self, item_name, quantity):
        """_summary_

        Args:
            item_name (_type_): _description_
            quantity (_type_): _description_
        """
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item_from_inventory(self, item_name, quantity):
        """_summary_

        Args:
            item_name (_type_): _description_
            quantity (_type_): _description_
        """
        if item_name in self.inventory:
            if quantity >= self.inventory[item_name]:
                del self.inventory[item_name]
            else:
                self.inventory[item_name] -= quantity

    def get_inventory(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.inventory

    def calculate_adjusted_speed(self):
        """_summary_
        """
        self.adjusted_speed = self.base_speed + self.speed_adjustment

    def calculate_initiative(self):
        """_summary_
        """
        self.initiative = self.initiative_modifier + self.initiative_adjustment

    def calculate_passive_perception(self):
        """_summary_
        """
        self.passive_perception = 10 + self.skill_adjustments["Perception"] + self.passive_perception_adjustment

    def level_up(self):
        """_summary_
        """
        self.level += 1
        self.next_level_goal = self.level * 300

    def add_experience(self, experience):
        """_summary_

        Args:
            experience (_type_): _description_
        """
        self.current_xp += experience

        while self.current_xp >= self.next_level_goal:
            self.current_xp -= self.next_level_goal
            self.level_up()

    def print_character(self):
        """_summary_
        """
        print("Character Details:")
        print(f"Name: {self.name}")
        print(f"Campaign: {self.campaign}")
        print(f"Creation Date: {self.creation_date}")
        print(f"XP: {self.current_xp}")
        print(f"Next Level Goal: {self.next_level_goal}")
        print(f"Race: {self.race}")
        print(f"Class: {self.character_class}")
        print(f"Alignment: {self.alignment}")
        print(f"Level: {self.level}")
        print(f"Size: {self.size}")
        print(f"Speed: {self.adjusted_speed}")
        print(f"Initiative: {self.initiative}")
        print(f"Armor Class: {self.armor_class}")
        print(f"Max Hit Points: {self.max_hit_points}")
        print(f"Current Hit Points: {self.current_hit_points}")
        print(f"Temporary Hit Points: {self.temporary_hit_points}")
        print(f"Death Saves: {self.death_saves['successes']} successes, {self.death_saves['failures']} failures")
        print(f"Advantages: {self.advantages}")
        print(f"Disadvantages: {self.disadvantages}")
        print(f"Passive Perception: {self.passive_perception}")
        print(f"Inspiration: {self.inspiration}")
        print(f"Proficiency: {self.proficiency}")
        print(f"Exhaustion: {self.exhaustion}")
        print(f"Skills: {self.skills}")

    def take_damage(self, damage):
        """_summary_

        Args:
            damage (_type_): _description_
        """
        self.current_hit_points -= damage

        if self.current_hit_points <= 0:
            self.current_hit_points = 0
            print(f"{self.name} has been defeated!")

    def heal(self, amount):
        """_summary_

        Args:
            amount (_type_): _description_
        """
        if not self.is_alive():
            return
        self.current_hit_points = min(self.current_hit_points + amount, self.max_hit_points)
        print(f"{self.name} healed for {amount} hit points.")

    def level_up(self):
        """_summary_
        """
        self.level += 1
        self.next_level_goal = self.level * 300
        self.max_hit_points += self.hit_points_per_level

        print(f"{self.name} has reached level {self.level}!")

    def select_feature(self, feature):
        """_summary_

        Args:
            feature (_type_): _description_
        """
        if feature in self.features:
            print(f"{self.name} already has the {feature} feature.")
        else:
            self.features.append(feature)
            print(f"{self.name} has gained the {feature} feature!")

    def make_death_save(self, success=True):
        """_summary_

        Args:
            success (bool, optional): _description_. Defaults to True.
        """
        if self.current_hit_points <= 0:
            print(f"{self.name} is already defeated and cannot make death saves.")
            return

        if success:
            self.death_saves["successes"] += 1
            print(f"{self.name} has succeeded a death saving throw.")
        else:
            self.death_saves["failures"] += 1
            print(f"{self.name} has failed a death saving throw.")

        if self.death_saves["successes"] == 3:
            self.current_hit_points = 1
            self.death_saves["successes"] = 0
            self.death_saves["failures"] = 0
            print(f"{self.name} stabilized with 1 hit point.")

        elif self.death_saves["failures"] == 3:
            self.current_hit_points = 0
            self.death_saves["successes"] = 0
            self.death_saves["failures"] = 0
            print(f"{self.name} has died!")

    def attack(self, target):
        """_summary_

        Args:
            target (_type_): _description_
        """
        hit_chance = random.randint(1, 20)
        if hit_chance >= target.armor_class:
            damage = random.randint(self.attack_damage[0], self.attack_damage[1])
            target.take_damage(damage)
            print(f"{self.name} hits {target.name} for {damage} damage!")
        else:
            print(f"{self.name} misses {target.name}!")

    def defend(self, damage):
        """_summary_

        Args:
            damage (_type_): _description_
        """
        defense_chance = random.randint(1, 20)
        if defense_chance >= self.armor_class:
            reduced_damage = damage - self.damage_reduction
            if reduced_damage < 0:
                reduced_damage = 0
            self.take_damage(reduced_damage)
            print(f"{self.name} defends and takes {reduced_damage} damage!")
        else:
            print(f"{self.name} fails to defend and takes {damage} damage!")
                 
    def is_alive(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.current_hit_points > 0

    def is_defeated(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.current_hit_points <= 0
    
    def display_info(self):
        """_summary_
        """
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Hit Points: {self.current_hit_points}/{self.max_hit_points}")
        print(f"Features: {', '.join(self.features)}")
        print(f"Armor Class: {self.armor_class}")
        print(f"Attack Damage: {self.attack_damage[0]}-{self.attack_damage[1]}")
        print(f"Damage Reduction: {self.damage_reduction}")
        print(f"Death Saves: {self.death_saves['successes']} successes, {self.death_saves['failures']} failures")
              
    def level_up(self):
        """_summary_
        """
        self.level += 1
        self.max_hit_points += 10
        self.current_hit_points = self.max_hit_points
        print(f"{self.name} leveled up to level {self.level}!")     
             
    def restore_hit_points(self, amount):
        """_summary_

        Args:
            amount (_type_): _description_
        """
        self.current_hit_points = min(self.current_hit_points + amount, self.max_hit_points)
        print(f"{self.name} restored {amount} hit points.")
     
    def heal(self, target, amount):
        """_summary_

        Args:
            target (_type_): _description_
            amount (_type_): _description_
        """
        target.restore_hit_points(amount)
        print(f"{self.name} heals {target.name} for {amount} hit points.")        
              
    def can_perform_death_save(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if not self.is_alive():
            return False
        if self.death_saves['successes'] >= 3 or self.death_saves['failures'] >= 3:
            return False
        return True        
              
    def perform_death_save(self):
        """_summary_
        """
        if not self.can_perform_death_save():
            return
        roll = random.randint(1, 20)
        if roll == 1:
            self.death_saves['failures'] += 2
        elif roll < 10:
            self.death_saves['failures'] += 1
        elif roll == 20:
            self.death_saves['successes'] += 2
        else:
            self.death_saves['successes'] += 1
        print(f"{self.name} performed a death save.")      
            
    def is_stabilized(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.death_saves['failures'] >= 3:
            return True
        return False       
         
    def take_damage(self, amount):
        """_summary_

        Args:
            amount (_type_): _description_
        """
        if not self.is_alive():
            return
        self.current_hit_points = max(self.current_hit_points - amount, 0)
        print(f"{self.name} took {amount} damage.")
        if not self.is_alive():
            print(f"{self.name} has been defeated!")    
         
    def is_incapacitated(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.current_hit_points == 0:
            return True
        return False       

    def perform_saving_throw(self, attribute, target_dc):
        """_summary_

        Args:
            attribute (_type_): _description_
            target_dc (_type_): _description_

        Returns:
            _type_: _description_
        """
        if not self.is_alive():
            return False
        roll = random.randint(1, 20) + self.attributes[attribute]
        if roll >= target_dc:
            print(f"{self.name} succeeded on the {attribute} saving throw!")
            return True
        else:
            print(f"{self.name} failed the {attribute} saving throw.")
            return False        
              
    def apply_status_effect(self, effect):
        """_summary_

        Args:
            effect (_type_): _description_
        """
        if not self.is_alive() or self.is_incapacitated():
            return
        if effect not in self.status_effects:
            self.status_effects.append(effect)
            print(f"{self.name} is now affected by {effect}.")
        else:
            print(f"{self.name} is already affected by {effect}.")        
        
    def remove_status_effect(self, effect):
        """_summary_

        Args:
            effect (_type_): _description_
        """
        if effect in self.status_effects:
            self.status_effects.remove(effect)
            print(f"{self.name} is no longer affected by {effect}.")
        else:
            print(f"{self.name} is not affected by {effect}.")        
        
    def has_status_effect(self, effect):
        """_summary_

        Args:
            effect (_type_): _description_

        Returns:
            _type_: _description_
        """
        return effect in self.status_effects      
               
    def display_status_effects(self):
        """_summary_
        """
        if not self.status_effects:
            print(f"{self.name} has no status effects.")
        else:
            print(f"{self.name} is currently affected by the following status effects:")
            for effect in self.status_effects:
                print(effect)     

    def to_dict(self):
        character_dict = OrderedDict()
        character_dict["player"] = self.player
        character_dict["campaign"] = self.campaign
        character_dict["creation_date"] = self.creation_date
        character_dict["current_xp"] = self.current_xp
        character_dict["next_level_goal"] = self.next_level_goal
        character_dict["name"] = self.name
        # add other class variables to the dictionary
        # ...

        return character_dict
    
    def save(self):
        """_summary_
        """
        # Create the save folder if it doesn't exist
        save_folder = os.path.join(os.path.dirname(__file__), '../save_files')
        os.makedirs(save_folder, exist_ok=True)

        # Build the save file path
        save_file_path = os.path.join(save_folder, f'{self.name}.json')

        # Serialize the character object to JSON

        character_json = json.dumps(self.to_dict(), indent=4)

        # Save the JSON data to the file
        with open(save_file_path, 'w') as file:
            file.write(character_json)

        print("Character saved successfully.")

    @classmethod
    def load(cls, name):
        """_summary_

        Args:
            name (_type_): _description_

        Returns:
            _type_: _description_
        """
        # Build the save file path
        save_folder = os.path.join(os.path.dirname(__file__), '../save_files')
        save_file_path = os.path.join(save_folder, f'{name}.json')

        try:
            # Load the JSON data from the file
            with open(save_file_path, 'r') as file:
                character_json = file.read()

            # Deserialize the JSON data to a character object
            character = cls.from_dict(json.loads(character_json))

            print("Character loaded successfully.")
            return character
        except IOError:
            print("Error: Unable to load character.")
            return None
        
    @classmethod
    def from_dict(cls, character_dict):
        name = character_dict["name"]
        character = cls(name)
        character.player = character_dict["player"]
        character.campaign = character_dict["campaign"]
        character.creation_date = character_dict["creation_date"]
        character.current_xp = character_dict["current_xp"]
        character.next_level_goal = character_dict["next_level_goal"]
        # set other class variables from the dictionary
        # ...

        return character


class Fighter(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def __init__(self, name):
        super().__init__(name)
        self.character_class = "Fighter"
        self.maneuvers_known = 0

    def learn_maneuver(self):
        if self.level >= 3:
            self.maneuvers_known += 1
            print(f"{self.name} has learned a new maneuver!")

    def attack(self, target):
        print(f"{self.name} attacks {target}!")

    def extra_attack(self, target):
        if self.level >= 5:
            print(f"{self.name} makes an additional attack against {target}!")


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name)
        self.character_class = "Wizard"
        self.spellbook = []

    def learn_spell(self, spell):
        if self.level >= 1:
            self.spellbook.append(spell)
            print(f"{self.name} has learned a new spell!")

    def cast_spell(self, spell, target):
        if spell in self.spellbook:
            print(f"{self.name} casts {spell} on {target}!")
        else:
            print(f"{self.name} does not know the spell {spell}.")

    def study_spellbook(self):
        print(f"{self.name} studies their spellbook.")


class Rogue(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def __init__(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        super().__init__(name)
        self.character_class = "Rogue"
        self.sneak_attack_damage = "1d6"

    def sneak_attack(self, target):
        """_summary_

        Args:
            target (_type_): _description_
        """
        print(f"{self.name} performs a sneak attack on {target} for {self.sneak_attack_damage} damage!")

    def lockpick(self, target):
        """_summary_

        Args:
            target (_type_): _description_
        """
        if self.level >= 2:
            print(f"{self.name} successfully lockpicks the {target}!")
        else:
            print(f"{self.name} attempts to lockpick the {target}, but fails.")

    def evasion(self):
        if self.level >= 7:
            print(f"{self.name} evades the incoming attack!")
        else:
            print(f"{self.name} attempts to evade the attack but fails.")


class Cleric(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def __init__(self, name):
        super().__init__(name)
        self.character_class = "Cleric"
        self.channel_divinity_uses = 0

    def use_channel_divinity(self):
        if self.level >= 2:
            self.channel_divinity_uses += 1
            print(f"{self.name} uses their Channel Divinity!")
        else:
            print(f"{self.name} does not have access to Channel Divinity yet.")


class Bard(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def __init__(self, name):
        super().__init__(name)
        self.character_class = "Bard"
        self.bardic_inspiration_uses = 0

    def use_bardic_inspiration(self):
        if self.level >= 2:
            self.bardic_inspiration_uses += 1
            print(f"{self.name} uses Bardic Inspiration!")
        else:
            print(f"{self.name} does not have access to Bardic Inspiration yet.")


class Barbarian(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def __init__(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        super().__init__(name)
        self.character_class = "Barbarian"
        self.rage_uses = 0

    def rage(self):
        """_summary_
        """
        if self.level >= 1:
            self.rage_uses += 1
            print(f"{self.name} enters a state of rage!")
        else:
            print(f"{self.name} does not have access to Rage yet.")


class Monk(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def __init__(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        super().__init__(name)
        self.character_class = "Monk"
        self.ki_points = 0

    def spend_ki(self):
        """_summary_
        """
        if self.level >= 2:
            self.ki_points += 1
            print(f"{self.name} spends a ki point!")
        else:
            print(f"{self.name} does not have access to ki yet.")


class Paladin(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def __init__(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        super().__init__(name)
        self.character_class = "Paladin"
        self.lay_on_hands_points = 0

    def lay_on_hands(self, target):
        """_summary_

        Args:
            target (_type_): _description_
        """
        if self.level >= 2:
            self.lay_on_hands_points += 5
            print(f"{self.name} uses Lay on Hands on {target}!")
        else:
            print(f"{self.name} does not have access to Lay on Hands yet.")


class Ranger(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def __init__(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        super().__init__(name)
        self.character_class = "Ranger"
        self.favored_enemies = []

    def choose_favored_enemy(self, enemy):
        """_summary_

        Args:
            enemy (_type_): _description_
        """
        self.favored_enemies.append(enemy)
        print(f"{self.name} chooses {enemy} as a favored enemy!")


class Sorcerer(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def __init__(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        super().__init__(name)
        self.character_class = "Sorcerer"
        self.sorcery_points = 0

    def use_sorcery_points(self):
        """_summary_
        """
        if self.level >= 2:
            self.sorcery_points += 1
            print(f"{self.name} uses a sorcery point!")
        else:
            print(f"{self.name} does not have access to sorcery points yet.")


class Warlock(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def __init__(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        super().__init__(name)
        self.character_class = "Warlock"
        self.pact_boon = None

    def choose_pact_boon(self, boon):
        """_summary_

        Args:
            boon (_type_): _description_
        """
        self.pact_boon = boon
        print(f"{self.name} chooses {boon} as their Pact Boon!")


class Druid(Character):
    """_summary_

    Args:
        Character (_type_): _description_
    """
    def __init__(self, name):
        """_summary_

        Args:
            name (_type_): _description_
        """
        super().__init__(name)
        self.character_class = "Druid"
        self.wild_shape_uses = 0

    def wild_shape(self):
        """_summary_
        """
        if self.level >= 2:
            self.wild_shape_uses += 1
            print(f"{self.name} transforms into a beast!")
        else:
            print(f"{self.name} does not have access to Wild Shape yet.")
