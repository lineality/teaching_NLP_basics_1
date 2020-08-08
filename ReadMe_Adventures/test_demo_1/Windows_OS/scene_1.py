scene = "Scene_1"
# scene 1: where you begin
import os
import random

# clear screen (for windows or...everything else)
os.system('cls' if os.name == 'nt' else 'clear')

#################
### Create Files
#################

# create .txt file of inn's guest log for user:
readme_text = '''
Scene 1: Find Your Friends


Instructions:
1. Open Terminal
2. Get file       wget https://raw.githubusercontent.com/lineality/teaching_NLP_basics_1/master/ReadMe_Adventures/test_demo_1/Windows_OS/scene_1.py
3. Run file       Command: python3 scene_1.py


(Optional)
Tips:
1. When given a choice or a question,
type in your answer and hit return.

2. Since it is lying on the bar-counter in front of you,
you can 'access' the inn's guest-register.
(This will help you to answer
the red-nosed innkeeper's question.)

3. Running the .py file will create new files
that you can use during the scene. Look for those files
the directory (folder) that your command terminal is open in.
(This file may be updated as well.)


'''

# create, write-to, & save .txt file
file_to_create = open("ReadMe.txt", "w")
file_to_create.write(readme_text)
file_to_create.close()
#open, read, & print the file
file_to_read = open("ReadMe.txt", "r")
#print(file_to_read.read())


# create .txt file of inn's guest log for user:
inn_guest_log_text = '''
(*loyal customer)
- Old Martha McSally
Items Purchased:
- capon (stuffed rooster)
- sauce
- fortified wine, two gallons
- one crouton of Bread

(seasonal traveler)
- Captn. Wilda Wooster
Items Purchased:
- bag of potatoes
- 1 *live rooster

(Those Meddlesome Kids)
- Friend 1: Baldwin
- Friend 2: Merln
- Friend 3: McCavity
- Friend 4: Q
Items Purchased:
- three pizzas
- 1 gallon of ginger-brew
- 1 cup of tea
- 1 book of dubious maps for tourists

(regulars)
- Four men in Kendal Green (difficult to see)
Items Purchased:
- fish'n chips x 4
- coffee x 8
- 2 books of crossword puzzles
- a dish towel
'''

# create, write-to, & save .txt file
file_to_create = open("inn_guest_log.txt", "w")
file_to_create.write(inn_guest_log_text)
file_to_create.close()
#open, read, & print the file
file_to_read = open("inn_guest_log.txt", "r")
#print(file_to_read.read())


################
### The Action!
################

print(scene)

# Main Story
print('''
\nYou are in The Mos Inn.
You are standing at the bar.
The bartender eyes you suspiciously.

"We don't allow droids in here...", the barman says.
"Not usually...but...who are you with?
Who are your friends?"
''')

# Tip
print('''
(Tip: Since it is lying on the bar-counter in front of you,
you can 'access' the inn's guest-register. Check your file directory again.)
''')

friends_dict = {
"first": "Baldwin",
"second": "Merln",
"third": "McCavity",
"fourth": "Q"
}

tip = '''\n\n(Tip: Check the ReadMe file if you are out of ideas.)\n'''

responses = ["Who?",
             "Hmm...not sure I know anyone by that name..."
             "What was that?",
             "I didn't catch that...",
             "Come again?",
             "Are you sure about that?",
             "What?",
             "I'm sorry, my mind was wondering. What was that again?",
             "How would you spell that...doesn't sound familiar...",
             "Ha ha hah ahahahhahahhh. that's a good one.",
             "Ok, who are your friends, really?"
             ]

# function to check if the person's name is correct
def correct_name(person, name):
    return friends_dict[person] == name

# loop through and ask about each person:
for person_number in friends_dict:
    # reset flag
    friend_name_check = False

    # keep asking until the friends' names are given
    while friend_name_check == False:
      friend_name = input(f'"What was your {person_number} friend\'s name?"\n')
      friend_name_check = correct_name(person_number, friend_name)
      if friend_name_check == False:
          print(f'"{random.choice(responses)}"', tip)

print('''\n
"Oh, those crazy kids.
They're in the back at table eight.
Here, their pizza just game out of the oven
you might as well bring it with you.
Their tables' just back there."
''')
