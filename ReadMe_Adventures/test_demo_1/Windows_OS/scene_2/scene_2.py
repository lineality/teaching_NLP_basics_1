scene = "Scene_2_witch_map"
import os
import random

# clear screen (for windows or...everything else)
os.system('cls' if os.name == 'nt' else 'clear')

#################
### Create Files
#################

# create ReadMe.txt file
readme_text = '''
Scene 2: Witch Map

Instructions:
1. run .py in terminal
wget https://raw.githubusercontent.com/lineality/teaching_NLP_basics_1/master/ReadMe_Adventures/test_demo_1/Windows_OS/scene_2.py


(Optional)
Tips:
Steps to check the length of two files in python:
1. open python:
    python3
2. import both files (as different variables)
3. check the lenth with len()

e.g.
You could use a word processor to check the length,
but it is worthwhile to learn in python.
The easy part is getting the lenth of anything:
len(x)
It takes more steps to open the file and copy the contents to a variable,
but still just a few steps. ( lines that start with # are a comment)

# import the files as separate variables
map1_intermediary_file = open("map_1.txt", "r")
map2_intermediary_file = open("map_2.txt", "r")

# file_to_read = open("map_1.txt", "r")
map1_text = map1_intermediary_file.read()
map2_text = map2_intermediary_file.read()

# print out the lengths, using len(x)
print(len(map1_text))
print(len(map2_text))
'''

# create, write-to, & save .txt file
file_to_create = open("ReadMe.txt", "w")
file_to_create.write(readme_text)
file_to_create.close()

# #open, read, & print the file
# file_to_read = open("ReadMe.txt", "r")
# print(file_to_read.read())



###
## Setting Up
###

# general_wrong_answer_responces
responses = [
            "Huh?",
  		      "What was that?",
		        "Really?",
            "I didn't catch that...",
            "Come again?",
            "Are you sure about that?",
            "What?",
            "You're pulling my leg!",
            "I'm sorry, my mind was wondering. What was that again?",
            "Ha ha hah ahahahhahahhh, that's a good one.",
            "You have to be joking."
            ]



#################
# Materials Files
#################

# create map_1 file
map_1 = '''
Welcome to the historic dungeons of
Spring Falls Imperial Forest Reserves,
home to the most highly reviewed dungeon restaurants
and a family friendly enchanted forest retreat center.
From the impasses of blister bay to the seasonal favorite
'house of blood' that delight family travelers,
you can also stop by our xylophone emporium for an acoustic mystery
the family will never forget. (All instruments are made by humans
on the premises accorded to Imperial law.)
Fasting, loitering, and pets are prohibited.
Directions: Head east past the Axis Mountains then follow
the South Ridge mountains continuing south until you
get to the third old growth pine forest
and turn west at the base of the mountain.
'''

# create, write-to, & save .txt file
file_to_create = open("map_1.txt", "w")
file_to_create.write(map_1)
file_to_create.close()

# # #open, read, & print the file
# map1_file_to_read = open("map_1.txt", "r")
# print(map1_file_to_read.read())

# # #count length
# map1_file_to_read = open("map_1.txt", "r")
# map1_text = map1_file_to_read.read()
# print(len(map1_text))



# create map_2 file
map_2 = '''
Here at the Murkland Designated Sites,
we are proud to have received recognition
for our 100% magic-free locally grown produce.
Tours are temporarily behind schedule
due to a wagon guild strike.
Information about the fence around the park
may be obtained with a freedom of information request
submitted before the next full moon
to the Bureau of Parks and Sacrifices. May the
the great empire prevailed over threats of technology.
Seasonal passes will resume availability
during the livestock relation season.
Due to a decrease in demand, trumpet filters will no longer be
available even with a judicial order on park grounds. All hail the humans.
Directions: Go to the base of Blossom ridge mountain.
'''

# create, write-to, & save .txt file
file_to_create = open("map_2.txt", "w")
file_to_create.write(map_2)
file_to_create.close()

# # #open, read, & print the file
# map2_file_to_read = open("map_2.txt", "r")
# print(map2_file_to_read.read())

# # #count length
# map2_file_to_read = open("map_2.txt", "r")
# map2_text = map2_file_to_read.read()
# print(len(map2_text))



######################
# setting up question:
pronoun = input("What is your character's pronoun?\n")
# making lower case
pronoun = pronoun.lower()

# fix (he vs. him etc.)
if pronoun == 'him':
    pronoun = 'he'

if pronoun == 'her':
    pronoun = 'she'

# pronoun2
if pronoun == 'he':
    pronoun2 = 'him'
elif pronoun == 'she':
    pronoun2 = 'her'
else:
    pronoun2 = 'them'


################
### The Action!
################

# clear screen (for windows or...everything else)
os.system('cls' if os.name == 'nt' else 'clear')

print(scene)

# Main Story
print('''
\n
You walk to the back,
carying the hot pizza,
over creaking wooden floor boards.
\nThe rooms get quieter as you get further from the bar.
You walk up to a round table in the back up against the wall
with a small round dusty window overhead.\n
Something splashes against the window.
\n"Hey," someone at the table says as they look up.
"Is that our pizza? I'm starving."
''')

answer = input("Your Answer: Is this their pizza? (yes/no)\n")

# clear screen (for windows or...everything else)
os.system('cls' if os.name == 'nt' else 'clear')

answer = answer.lower()
if answer == 'yes':
    print('''
    "Yayy!!!!"

    You put the pizza on the table
    and they start to grab slices and eat.
    ''')
else:
    print('"...but it smells so good..."\n')

# Tip
print(f'''
"Ok, everyone, let's focus. What are we going to do
about these maps?"

"I think that one looks longer."

"But it could be off by just one character.
We need the one with the shorter text."

"I know, I tried counting them last night but
I kept coming up with slightly different numbers."

"Can we just try them both?"

"They lead in opposite directions, it takes days to get there,
one them is probably a trap, and we have classes on Monday."

"And I have to walk my Dog."

"And Q has to walk her dog."

"My Aunt's dog."

"Her Aunt's dog. It's your Aunt's dog? Anyway, we shouldn't try them both."\n
''', f'"Hang on...I bet {pronoun} can count...can you count?"\n'
)

print("All voices go silent as everyone turns their gaze to you.\n")

answer_check = False
# keep asking until answer is correct
while answer_check == False:
  answer = input('"...can you count?" (yes/no)\n')
  answer = answer.lower()
  if answer == 'yes':
      answer_check = True
  if answer_check == False:
      print(f'"{random.choice(responses)}"')

# clear screen (for windows or...everything else)
os.system('cls' if os.name == 'nt' else 'clear')

print('''"You can? Oh my gosh, ok, which of these is longer?"

"...I was thinking, they're almost more like pamphlets than maps, really."

"We could call them...Folded-Publications?"

"We got them from witches, are witches 'publishers'?
I always wondered about that."

"Whatever, map-pamphlets, leaflets, can you count how long they are? Like,
how many characters are printed on each one? Like, letters and numbers?"''')

print("n\(Compare the length of the two files.)")

# lengths
map1_file_to_read = open("map_1.txt", "r")
map1_text = map1_file_to_read.read()
map1_length = len(map1_text)

map2_file_to_read = open("map_2.txt", "r")
map2_text = map2_file_to_read.read()
map2_length = len(map2_text)

map_length_dict = {
"map_1": map1_length,
"map_2": map2_length
}

#print(map1_length, map2_length)

answer_check = False
# keep asking until answer is correct
while answer_check == False:
  answer = input('"...How long is the first map?"\n')
  answer = int(answer)
  answer_check = (answer == map_length_dict["map_1"])
  if answer_check == False:
      print(f'"{random.choice(responses)}"')

answer_check = False
# keep asking until answer is correct
while answer_check == False:
  answer = input('"...How about the second one?"\n')
  answer = int(answer)
  answer_check = (answer == map_length_dict["map_2"])
  if answer_check == False:
      print(f'"{random.choice(responses)}"')

# clear screen (for windows or...everything else)
os.system('cls' if os.name == 'nt' else 'clear')

print('\n"That was awsome. Ok, quick vote: Should we bring the android?"\n')

print(f'"You can\'t just bring {pronoun2} if {pronoun} doesn\'t want to come?"\n')

print(f'"That\'s not what I meant but, whatever. Do we invite {pronoun2}?"\n')

print(f'"{pronoun.title()} can hear us...{pronoun}\'s standing right there."\n')

print('''"Yes, awkward, sorry, bad planning here, but what's the vote?
Who says yes?"

Everyone immidiately raises their hand.

"Do you want to come find a dungeon?
We'll tell you all about it on the way.
Well, we don't know all about it,
but, do you want to come?"\n
''')

answer = input("(yes/no)\n")

# clear screen (for windows or...everything else)
os.system('cls' if os.name == 'nt' else 'clear')

if answer == 'yes':
    print("\n\nEnd of Scene 2")
