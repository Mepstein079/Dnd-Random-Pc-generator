import random

print("Hello, welcome to my random DnD Character Maker")
print("-----------------------------------------------")

# list of DnD 5e races
races = {
    'Chromatic Dragonborn', 'Draconblood Dragonborn', 'Gem Dragonborn', 'Metallic Dragonborn', 'Ravenite Dragonborn',
    'Dwarf', 'Hill Dwarf', 'Mountain Dwarf', 'Mark of Warding Dwarf', 
    'Elf', 'Aereni High Elf', 'Aereni Wood Elf', 'Dark Elf', 'High Elf', 'Mark of Shadow Elf', 'Pallid Elf', 'Valenar High Elf', 'Valenar Wood Elf', 'Wood Elf', 
    'Gnome', 'Forest Gnome', 'Mark of Scribing Gnome', 'Rock Gnome', 
    'Half-Elf', 'Aquatic Half-Elf', 'Drow Half-Elf', 'High Half-Elf', 'Mark of Detection Half-Elf', 'Mark of Storm Half-Elf', 'Wood Half-Elf', 
   'Halfing', 'Ghostwise Halfing', 'Lightfoot Halfing', 'Lotusden Halfing', 'Mark of Healing Halfing', 'Mark of Hospitality Halfing', 'Stout Halfing', 
    'Half-Orc', 'Mark of Finding Half-Orc',
    'Human', 'Mark of Finding Human', 'Mark of Handling Human', 'Mark of Making Human', 'Mark of Passage Human', 'Mark of Sentinel Human', 'Variant Human', 
    'Tiefling', 'Variant Tiefling', 
    'Aarakocra', 
    'Aasimar', 
    'Air Genasi', 
    'Bugbear', 
    'Changling', 
    'Deep Gnome', 
    'Duergar', 
    'Earth Genasi', 
    'Eladrin', 
    'Fairy', 
    'Firebolg', 
    'Fire Genasi', 
    'Githyanki', 
    'Githzerai', 
    'Goblin', 
    'Goliath', 
    'Harengon', 
    'Hobgoblin', 
    'Kenku', 
    'Kobold', 
    'Lizardfolk', 
    'Minotaur', 
    'Orc', 
    'Satyr', 
    'Sea Elf', 
    'Shadar-kai', 
    'Shifter', 
    'Tabaxi', 
    'Tortle', 
    'Triton', 
    'Water Genasi', 
    'Yuan-ti', 
    'Kender', 
    'Astral Elf', 
    'Autognome', 
    'Giff', 
    'Hadozee', 
    'Plasmoid', 
    'Thri-kreen', 
    'Owlin', 
    'Leonin', 
    'Kalashtar', 
    'Warforged', 
    'Verdan', 
    'Loxodon', 
    'Simic Hybrid', 
    'Vedalken', 
    'Feral Tiefling', 
    'Locathah', 
    'Grung',
}
# list of DnD 5e classes
classes = {
    'Barbarian': ['Path of the Ancestral Guardian', 'Path of the Battlerager', 'Path of the Beast', 'Path of the Berserker', 'Path of the Storm Herald', 'Path of the Totem Warrior', 'Path of the Zealot', 'Path of Wild Magic'],
    'Bard': ['College of Creation', 'College of Eloquence', 'College of Glamour', 'College of Lore', 'College of Spirits', 'College of Swords', 'College of Valor', 'College of Whispers'],
    'Cleric': ['Divine Domain', 'Arcana Domain', 'Death Domain', 'Forge Domain', 'Grave Domain', 'Knowledge Domain', 'Life Domain', 'Light Domain', 'Nature Domain', 'Order Domain', 'Peace Domain', 'Tempest Domain', 'Tempest Domain', 'Trickery Domain', 'Twilight Domain', 'War Domain'],
    'Druid': ['Circle of Dreams', 'Circle of Spores', 'Circle of Stars', 'Circle of the Land', 'Circle of the Moon', 'Circle of the Shepherd', 'Circle of the Wildfire'],
    'Fighter': ['Arcane Archer', 'Battle Master', 'Cavalier', 'Champion', 'Echo Knight', 'Eldritch Knight', 'Gunslinger', 'Psi Warrior', 'Purple Dragon Knight', 'Rune Knight', 'Samurai'],
    'Monk': ['Way of Mercy', 'Way of Shadow', 'Way of Acendant Dragon', 'Way of the Astral Self', 'Way of the Cobalt Soul', 'Way of the Drunken Master', 'Way of the Four Elements', 'Way of the Kensei', 'Way of the Long Death', 'Way of the Open Hand', 'Way of the Sun Soul'],
    'Paladin': ['Oath of Conquest', 'Oath of Devotion', 'Oath of Glory', 'Oath of Redemption', 'Oath of the Ancients', 'Oath of the Crown', 'Oath of the Open Sea', 'Oath of the Watchers', 'Oath of Vegeance', 'Oathbreaker'],
    'Ranger': ['Beast Master', 'Drakewarden','Fey Wanderer', 'Gloom Stalker', 'Horizon Walker', 'Hunter', 'Monster Slayer', 'Swarmkeeper'],
    'Rogue': ['Arcane Trickster', 'Assassin', 'Inquistive', 'Mastermind', 'Phantom', 'Scout', 'Soulknife', 'Swashbuckler', 'Thief'],
    'Sorcerer': ['Abberant Mind', 'Clockwork Soul', 'Divine Soul', 'Draconinc Bloodline', 'Lunar Sorcery', 'Shadow Magic', 'Storm Sorcery', 'Wild Magic'],
    'Warlock': ['The Archfey', 'The Celestial', 'The Fathomless', 'The Fiend', 'The Genie', 'The Great Old One', 'The Hexblade', 'The Undead', 'The Undying'],
    'Wizard': ['Bladesinging', 'Chronurgy Magic', 'Graviturgy Magic', 'Order of Scribes', 'School of Abjuration', 'School of Conjuration', 'School of Divination', 'School of Enchantment', 'School of Evocation', 'School of Illusion', 'School of Necromancy', 'School of Transmutation', 'War Magic'],
    'Artificer': ['Alchemist', 'Armorer', 'Artillerist', 'Battle Smith'],
    'Blood Hunter': ['Order of Ghostslayer', 'Order of Lycan', 'Order of the Mutant', 'Order of the Profane Soul']
}
# list of DnD 5e Backgrounds
backgrounds = ['Acolyte', 'Anthropologist', 'Achaeologist', 'Astral Drifter', 'Athlete', 'Azorius Functionary', 'Boros Legionnaire', 'Celebrity Adventurers Scion', 'Charlatan', 'City Watch', 'Clan Crafter', 'Cloistered Scholar', 'Cloistered Scholar', 'Courtier', 'Criminal', 'Dimir Operative', 'Entertainer', 'Faceless', 'Faction Agent', 'Failed Merchant', 'Far T raveler', 'Feylost', 'Fisher', 'Folk Hero', 'Gambler', 'Gladiator', 'Golgari Agent', 'Grinner', 'Gruul Anarch', 'Guild Artisan', 'Haunted One', 'Hermit', 'House Agent', 'Inheritor', 'Investigator', 'Izzet Engineer', 'Knight', 'Knight of Solamnia', "Knight of the Order", 'Lorehold Student', 'Mage of High Sorcery', 'Marine', 'Mercenary Veteran', 'Noble', 'Orzhov Representative', 'Outlander', 'Pirate', 'Plaintiff', 'Prismari Student', 'Quandrix Student', 'Rakdos Cultist', 'Rival Intern', 'Sage', 'Sailor', 'Selesnya Initiate', 'Shipwright', 'Silverquill Student', 'Simic Scientist', 'Smuggler', 'Soldier', 'Spy', 'Urban Bounty Hunter', 'Urchin', 'Uthgardt Tribe Member', 'Volstrucker Agent', 'Waterdhavian Noble', 'Wildspacer', 'Witchlight Hand', 'Witherbloom Student']

# "rolls" dice for stats
def roll_dice():
    dice_rolls = [random.randint(1,6) for _ in range(4)]
    min_value = min(dice_rolls)
    min_index = dice_rolls.index(min_value)
    dice_rolls.pop(min_index)

    return dice_rolls


#  takes the total from roll_dice and rerolls it if total is below 8
def total_stat():
    while True:
        desired_number = 8
        each_roll = roll_dice()
        totalSum = sum(each_roll)
        if totalSum > desired_number:
            return each_roll, totalSum


# bring everything together to make the character
def generate_character():
    race = random.choice(list(races))
    char_class = random.choice(list(classes.keys()))
    sub_class = random.choice(classes[char_class])
    background = random.choice(backgrounds)
    strength = total_stat()
    dexterity = total_stat()
    constitution = total_stat()
    intelligence = total_stat()
    wisdom = total_stat()
    charisma = total_stat()

    # puts the generated character together
    character = {
        'Race': race,
        'Class': char_class,
        'Sub Class': sub_class,
        'Background': background,
        'Strength': strength,
        'Dexterity': dexterity,
        'Constitution': constitution,
        'Intelligence': intelligence,
        'Wisdom': wisdom,
        'Charisma': charisma
    }

    return character

# takes the generated character and puts it in a form more condensed for the print function
def print_character(character):
    print("Race:", character['Race'])
    print("Class:", character['Class'])
    print("Sub Class:", character['Sub Class'])    
    print("Background:", character['Background'])
    print("Strength:", character['Strength'])
    print("Dexterity:", character['Dexterity'])
    print("Constitution:", character['Constitution'])
    print("Intelligence:", character['Intelligence'])
    print("Wisdom:", character['Wisdom'])
    print("Charisma:", character['Charisma'])


character = generate_character()

print("Random Character:")
print_character(character)
