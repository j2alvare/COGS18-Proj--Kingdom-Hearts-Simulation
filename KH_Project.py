#!/usr/bin/env python
# coding: utf-8

# # Project Description

# This project is a video game simulation inspired by the Kingdom Hearts franchise. The user must input their username password, etc. before being granted access to the game. The user will then interact in conversation with Mickey and discuss about the user's origins, name, and weapon. Ultimately, the user will have to challenge a monster using the weapon selected. Once the monster is defeated the player will complete Level 1.
# 
# The game uses classes, functions, and a chatbot. In order to progress into the game, the user must select the right choices. The user will unlock graphics as they progress through the game, with the final graphic being the image of the monster that they will fight.
# 
# I borrowed code from the chatbots assignment but I added in my own inputs and outputs for the chatbot to respond to.

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[ ]:


get_ipython().system(' pip install --user pillow')
get_ipython().system(' pip install --user playsound')
#Package that will import playsound which will allow us to run code thatt plays mp3 files stored in our project.
get_ipython().system(' pip install --user PyObjC')
#Package that is needed to be installed to use playsound.


# In[7]:


from PIL import Image
#We are importing the image function from Pillow to display the image.
import matplotlib.pyplot as plt
#We are going to use a plot to display our image.

img = Image.open('./Pillow/KingdomHeartsLogo.jpg')

plt.imshow(img)


# In[ ]:


from playsound import playsound
playsound('Intro.mp3')


# In[ ]:


import string
import random
import nltk


# In[ ]:


print('Please enter your username, password, edition, and Begin to start. Would you like to show game data? ')


# In[ ]:



    """Converts the user's data inputs into dictionary pairs.
    
    Parameters
    ---------
    username: str
    password: str
    volue: str
    status: str
    display: str
    
    Returns
    -------
    display : dictionary
        Inputs are printed out as dictionary pairs.
    
    """
        
    def display(username, password, volume, status, display):
        game_data = {'User:': username,
                     'Password:': password,
                     'Edition:': volume,
                     'Status:' : status,
                     'Show game data?:': display  
        }
        
        for key,value in game_data.items():
    
            print(key,value)
        
        return display
# This class begins the game after the user has input their information. If there is an error the game won't begin.


# In[ ]:


def begin_game(start):
    """Receives a inputs and returns a string or none.
    
    Parameters
    ----------
    start : string 
    
    Returns
    -------
    begin_game : string 
        String either welcoming the user to the video game, a cannot start message, or None.
        
    """
    
    
    
    if start == 'Begin':
        print('Welcome to Kingdom Hearts!') 
        
    elif start == 'No':
        print('Cannot Start')
        
    else:
        None 
            
    return begin_game


# In[ ]:


user_input = display('jenny_xoxo','Ilovepizza','VI','Begin','Yes')


# In[ ]:


print('Would you like to begin? Select: Yes or No')


# In[ ]:


start_1 = begin_game('Begin')


# In[ ]:


print('Please select your character below from the list based on character name, weapon, team, and  world.')


# In[ ]:


def choosecharacter(character_name,weapon ,team , world):
       character_data = {'Character:': character_name,
                    'Weapon:': weapon,
                    'Team:': team,
                    'World:' : world, 
       }
       
       for key,value in character_data.items():
   
           print(key,value)
       
       return choosecharacter


# In[ ]:


character_input = choosecharacter('Sora','Keyblade','Light','Destiny Island')


# In[ ]:


input_string = ''
def is_question(input_string):
    for item in input_string:
        if '?'in input_string:
            output = True
        else:
            output = False
        return output


# In[ ]:


def remove_punctuation(input_string):
    out_string = ""
    for char in input_string:
        if char not in string.punctuation:
            out_string = out_string + char                 
    return out_string


# In[ ]:


def prepare_text(input_string):
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return out_list


# In[ ]:


def respond_echo(input_string,number_of_echoes,spacer):
        
        if input_string is not None:
            input_string = input_string + spacer
            echo_output = number_of_echoes*(input_string)

        else:
            echo_output = None 
            
            
        return echo_output


# In[ ]:


def selector(input_list,check_list,return_list): 
    output = None
    for item in input_list:
        while item in check_list:
            output = random.choice(return_list)
            break 
            
    return output 


# In[ ]:


def end_chat(input_list):
    for item in input_list:
        if 'quit'in input_list: 
            return True 
        else:
            return False
        return input_list


# In[ ]:


def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None


# In[ ]:


def mickey(talk):
    """Unlocks a graphic when the user responds correctly
    
    Parameters
    ----------
    talk: str
    
    Returns
    -------
    select_answer : img 
        If talk = 'Yes', it will display an image file. If talk = else, it will print an error message.
    
    """
    if talk == 'Yes':

        from PIL import Image
        import matplotlib.pyplot as plt

        img_2 = Image.open('./Pillow/Mickey.png')

        plt.imshow(img_2)

    else:
        print('Try again!')


# In[ ]:


select_answer = mickey('Yes')
print(select_answer)


# In[ ]:


GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
GREETINGS_OUT = ["Hey there. Want some help? [Select: Yes or No]", 'Are you lost? Want some help? [Select one: Yes or No]' ,  "Hey - let me help you! [Select: Yes or No]"]

RESPONSE_IN = ['yes','Yes','No','no']
RESPONSE_OUT = ['Alright, let me show you around! What weapon do you have?[Select: Keyblade, Shield, Staff]']

from PIL import Image
import matplotlib.pyplot as plt

img_3 = Image.open('./Pillow/Weapons.jpg')

plt.imshow(img_3)

WEAPON_IN = ['Keyblade','keyblade', 'Shield','shield', 'Staff','staff']
WEAPON_OUT = ["Great choice, that'll be useful later on. What is your name? [Select one: Sora, Kairi, Namine, Riku]",             "Woah no way!? That's awesome. What's your name? [Select one: Sora, Kairi, Namine, Riku]",             "Hm I'm not sure about that one. What's your name? [Select one: Sora, Kairi, Namine, Riku]",             "I heard it's one of a kind! What's your name? [Select one: Sora, Kairi, Namine, Riku]"]
from PIL import Image
import matplotlib.pyplot as plt

img_4 = Image.open('./Pillow/Mickey2.png')

plt.imshow(img_4)

PEOPLE_IN = ['Sora', 'Kairi','Namine', 'Riku']
PEOPLE_OUT = ['sounds familiar, what world are you from?!', 'is my friends name. What world are you from?','nice name! What world are you from?']
PEOPLE_NAMES = {'Sora', 'Kairi', 'Namine', 'Riku'}

WORLD_IN = ['Atlantis', 'Destiny Island', 'Twilight Town','hahaha', 'lol']
WORLD_OUT = ['I/ve been there, I used to visit my friend everday till he disappeared', 'I/ve heard of that town. One of my friends used to live there'] 

UNKNOWN = ['Sorry, could you repeat what you said? Huh wait watch out!']

QUESTION = "I'm too shy to answer questions. What do you want to talk about?"


# In[ ]:


def mickey():
    """Main function to run our chatbot."""
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('Me :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Sora'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))

            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, RESPONSE_IN, RESPONSE_OUT))
            
            # Check if the input message looks like a weapon, add a weapon if so 
            outs.append(selector(msg, WEAPON_IN, WEAPON_OUT))
            
            outs.append(selector(msg, PEOPLE_IN, PEOPLE_OUT))
                        
            # Check if the input mentions a person that is specified, add a person output if so
            if is_in_list(msg, PEOPLE_IN):
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name], name.capitalize(),
                                            selector(msg, PEOPLE_IN, PEOPLE_OUT)], ' '))

            # Check if the input looks like a joke, add a repeat joke output if so
            outs.append(respond_echo(selector(msg, WORLD_IN, WORLD_OUT), 3, ''))
        

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('Mickey Mouse:', out_msg)


# In[ ]:


# Talk to our chatbot
mickey()


# In[ ]:


print('As you are chatting with Mickey you suddenly hear a big roar...') 
print('A monster is approaching, hurry and use your weapon now!')
print('Choose now!: Fight! or Run!')


# In[ ]:


playsound('bossattack.mp3')


# In[ ]:


def activate_monster(your_response):
    """unlocks a monster graphic when the user provides the correct input
    
    Parameters
    ----------
    your_response: str
    
    Returns
    -------
    
    
    """
    if your_response == 'Fight!':
        from PIL import Image
        import matplotlib.pyplot as plt

        img_2 = Image.open('./Pillow/monster.png')

        plt.imshow(img_2)
        
    else:
        print('Are you sure?')


# In[ ]:


my_response = activate_monster('Fight!')


# In[ ]:


from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('./Pillow/Sora.png')

plt.imshow(img)

def attack_choices(attack1, attack2, attack3, attack4, attack5):
        list_of_attacks = {'Attack 1:': attack1,
                     'Attack 2:': attack2,
                     'Attack 3:': attack3,
                     'Attack 4:' : attack4,
                     'Attack 5:' : attack5,
                
        }
        
        for key,value in list_of_attacks.items():
    
            print(key,value)
        
        return attack_choices


# In[ ]:


chosen_attacks = attack_choices('Dodge -> 1pt', 'Roll -> 2pt', 'Shield -> 3pt','Staff -> 4pt', 'Keyblade -> 5pt' )


# In[ ]:


def fight(chosen_attacks):
    """Uses a counter to add the total amount for a list of numbers that the user inputs.
    
    Parameters
    ----------
    total : int
    val : int list
    
    Returns
    -------
    total : int
        Returns the total number of items added from the int list.
    
    """
    total = 0
    
    for val in chosen_attacks:
        total += val
    
    if total >= 1:
        print('Well done, the monster is now defeated! You have successful completed Level 1.'          
               ' Total Number  of Attacks =')
        return total


# In[ ]:


user_chosen_attacks = [1,2,3,4,5]
print (fight(user_chosen_attacks))


# In[ ]:


from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('./Pillow/Ending.png')

ending_scene = plt.imshow(img)


# In[ ]:


print('Would you like to resume your game? Select: Yes or No')

def resume_game(continue_game):
    """Receives a string input and returns a string output. 
    
    Parameters
    ----------
    continue_game = string
    
    Returns
    -------
    resume_game = string
        Returns a string informing the user about their decision with the appropriate output.
    
    """
    
    if continue_game == 'Yes':
        print('Loading your next game. Please standby . . .')
        
    elif continue_game =='No':
        print('Thank you for playing Kingdom Hearts. You may exit. Getting ready to shutdown your game. . .')
    
    else: 
        print('Error, please try again.') 
    return resume_game


# In[ ]:


continue_game = resume_game('Yes')


# In[ ]:


playsound('ending.mp3')


# In[ ]:


from my_module.functions import functions
from my_module.classes import classes


# #### Extra Credit (*optional*)
# 
# Replace all of this text with a brief explanation (~3 sentences) of: 
# 1. Your Python Background
# 
# I have no previous experience using Python before. Everything that I learned to do
# in Python was from this class.
# 
# 2. How your project went above and beyond the requirements of the project and/or how you challenged yourself to learn something new with the final project
# 
# I learned how to install and use the Pillow module to insert images into my project.
# This package allowed me to make my simulation more interactive and feel more like 
# a video game for the user. I also learned how to install the playsound package to
# add music to my project. I struggled a bit with setting up the module since I have
# a Mac so I did research and figured it out. The music includes the introduction, scene 
# with Mickey,and finally the boss battle. The music is accurate to the actual game.
#     

# In[9]:


get_ipython().system('pylint my_module/classes.py')


# In[8]:


get_ipython().system(' pip install --user pep8')


# In[ ]:





# In[ ]:




