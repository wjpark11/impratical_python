"""
generate silly sidekick names
"""
import sys
import random

print('Welcome to the Psych "Sidekick Name Picker".\n')
# Load a list of surnames
first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
    "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
    'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
    'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
    'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
    'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
    'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
    'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
    'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
    'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
    'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
    "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
    'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
    'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
    "Winston 'Jazz Hands'", 'Worms')
last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
    'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
    'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
    'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
    'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
    'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
    'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
    'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
    'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
    'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
    'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
    'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
    'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
    'Woolysocks')

while True:
# Choose a first name at random
# Assign the name to a variable
    firstName = random.choice(first)
# Choose a surname at random
# Assign the name to a variable
    lastName = random.choice(last)
# Print the names to the screen in order and in red font
    print("\n\n")
    print(f"{firstName} {lastName}", file=sys.stderr)
# Ask the user to quit or play again
    print("\n\n")
    answer = input("Play again? (Input 'n' for quit) : ")
# If user plays again:
# repeat
# Else:
# End and exit
    if answer.upper() == 'N':
        break
print('Good-bye')
