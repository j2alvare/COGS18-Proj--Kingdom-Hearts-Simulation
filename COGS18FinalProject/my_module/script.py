#!pylint functions.py

"""A collection of function for doing my project."""

from PIL import Image
#We are importing the image function from Pillow to display the image.
import matplotlib.pyplot as plt
#We are going to use a plot to display our image.

img = Image.open('./Pillow/KingdomHeartsLogo.jpg')

plt.imshow(img)


#from playsound import playsound
#playsound('Intro.mp3')
