# i am using website template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

#initialize global variables
secret_number=42
num_range=100

# helper function to start and restart the game
def new_game():
    
    
    #global secret_number,num_range
    #num_range=100
    #secre_number=random.randint (0,100)
      
        
    print 'New game.Range is from 0 to 100 22'
    

    

# define callback functions for control panel 
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range,secret_number
    num_range=100
    secret_number=random.randint (0,100)
    
print 'New game. Range is from 0 to 100 '
    
   

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range,secret_number
    num_range=1000
    secret_number=random.randint (0,1000)
    
    
    print 'New game. Range is from 0 to 1000 '




def input_guess(guess_number):
    guess_number = int(guess_number)
    if guess_number > secret_number: 
        print "number is highter!"
    elif guess_number == secret_number:
        print "number is correct!"

    elif guess_number < secret_number:
        print "number is lower!"
    else:
        print "number is exist!"
    

    
# create frame

frame = simplegui.create_frame("guess_the_number", 300, 250) 


# register event handlers for control elements and start frame
frame.add_button("Range is [0,100]", range100 , 200)
frame.add_button("Range is [0,1000]",range1000, 200)
frame.add_input("Enter range  number", input_guess,200)

# call new_game 
new_game()

# start game

frame.start()
# always remember to check your completed program against the grading rubric
