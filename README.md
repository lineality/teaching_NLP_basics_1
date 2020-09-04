
# Notes For ReadMe Adventures

draft notes:

flexibity for various curricula

# teaching_NLP_basics_1
Teaching Python NLP and Data Structure Basics using a dugeon-game study as a concrete context for cumulative use.

# Macro Lessons

1. hello world, hello dungeon
 
2. "slicing" [:] string slicing, list slicing
 
3. list comprehensions

4. functions, lambdas, command line, notebooks
 
5. reading files and saving your files:

....

instructional interface options...
text-based or RPG-maker type story parallel to a colab/repl

...

content map
skill-tree (if initial)
for python-based NLP starters
- using terminal
- using directories
  - to do: fix file path lesson notes
- using files
  -
  - .open()
  - .close()
  - .read()
  - .readlines()
  
  - (make, open, read (reset cursor with .seek(0), print), close file with .close() )
  
- varibles (filling, retyping, mutibility)
- slicing[:]
- len()
- replace()

text misc:
- 'escape characters'
- \n


...

ReadMe.txt Adventures! www.readmeadventures.com

paired: 
ReadMe.txt + Day_x.py

Stories of stand-alone scenes, learning and using new skills.


platforms:
- linux
- macOS
- BSD
- chromeOS
- iOS
- android
- DOS
- windows
- fushia


Self organize team/Group lessons

self-directed dungeons

pipenv based jupyter environments

...
Group lessons, designed around SCRUM...

...

notes:

content map
skill-tree (if initial)
for python-based NLP starters
- using terminal
- using directories
  - to do: fix file path lesson notes
- using files
  - .open("file", mode) https://www.w3schools.com/python/ref_func_open.asp
Modes: e.g. r / rt / rb  
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exist
In addition you can specify if the file should be handled as binary or text mode
e.g rb / rt / w+(overwrites existing file)
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"+" - reading and writing

  - .close()
  - .read() 

  - .readlines()
- delete file... os.remove("demofile.txt") 
  
  - (make, open, read (reset cursor with .seek(0), print), close file with .close() )
  
- variables (filling, retyping, mutibility)
slicing[:]
len()
.split() / .split(",")
		e.g. (prints individuals words)
		for line in list_of_lines:
			print(line.split()[0]
.replace(old, new)

text misc:
- 'escape characters'
- \n



quest:
#. replace characters to make more readable
#. print words only that start with a symbol character

...

context what??? awsome
"context manager"
# this will automatically close the file afterwards...neat.
with open('file.txt', 'r') as thing_to_open:
	storage_variable = thing_to_open.readlines()


....

pdf??

...

character choice options for group lessons...hmm...

maybe an automated cutup of sections of puzzles?
(this could acomodate any number of players...
e.g. a group of andoroid, whatever that number is, 
is found outside or inside the dungeon hiding)
etc

...


cut-ups of lessons...

And inner prompt to open a jupyter pipenv using lock file created by .py... maybe that can work...


make a piplock
new terminal:
CD
run a ...create?
pipeven run jupyter lab
