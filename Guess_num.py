# i am using website template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console



import simplegui
import random
import math
    



# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number= 54
    
    global guess_number
    
    
def remaining_guesses() : 
    
    remaining_guesses == 7
    

    # remove this when you add your code    
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    input_number=random.randrange (0,100)
    print range100  
    
    return
    
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    range1000=random.randrange (0,1000)
    print range1000
    return
    
    
    pass




def input_guess(guess_number):
    guess_number = int(guess_number)
    
    
  
    if guess_number > 54 and guess_number < 1000 : 
        
        print "number is highter!"
    elif guess_number == 54:
        print "number is correct!"
    elif guess_number < 54 and guess_number > 0:
        print "number is lower!"
    else:
        print "number is exist!"
    
        

    pass

    
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

