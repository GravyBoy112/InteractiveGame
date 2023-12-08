from asyncio import events
from random import choice
import sys

#imports key prompts
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_1,
    K_2,
    K_3,
    QUIT,
)

#import and initialize packages
import pygame
import time
import os
import pygame_widgets as pw
from pygame_widgets.button import Button

pygame.init()

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#keep loop running
running = True

def ending(running, choice, choices):
    while running == True:
        screen.fill((0, 0, 0))
        
        white = ((255, 255, 255))
        
        #establishes font and size for words appearing on screen
        Font = pygame.font.SysFont('arial', 30)

        #generates surfaces for images and wordds to set on and the images themselves
        endingscreen1 = pygame.Surface(((SCREEN_WIDTH/1.025), (SCREEN_HEIGHT/1.51)), pygame.SRCALPHA, 32)
        chatbox = pygame.Surface(((SCREEN_WIDTH/1.025), (SCREEN_HEIGHT/ 3.17)), pygame.SRCALPHA, 32)
        chatbox1 = pygame.Surface(((SCREEN_WIDTH/1.031), (SCREEN_HEIGHT/ 3.27)), pygame.SRCALPHA, 32)
        endscene1 = (pygame.image.load(os.path.join("Scenes", "New Piskel (1).gif")))
        endscene1 = pygame.transform.scale(endscene1, ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)))
        
        #Creates variable for epilogue
        epilogue = Font.render(f"You ended up choosing {choice}.", True, white)
        
        #"paints" surfaces for images to set on
        endingscreen1.fill((255, 255, 255))
        rect = endingscreen1.get_rect() 
        chatbox.fill((255, 255, 255))
        rect = chatbox.get_rect()
        chatbox1.fill((0, 0, 0))
        rect = chatbox1.get_rect()

        #places images and rectangles on screen
        screen.blit(chatbox, ((SCREEN_WIDTH/83.3), (SCREEN_HEIGHT/1.48)))
        screen.blit(chatbox1, ((SCREEN_WIDTH/66), (SCREEN_HEIGHT/1.47)))
        screen.blit(endscene1, ((SCREEN_WIDTH/4), (SCREEN_HEIGHT/20)))   

        screen.blit(epilogue, ((SCREEN_WIDTH/40), (SCREEN_HEIGHT/1.45)))        

        #look at queued events
        for event in pygame.event.get():
        #user hit key?
            if event.type == KEYDOWN:
                #was it escape? If so, exit loop
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        pygame.display.update()

#game loop
def Beginning(running, scene1):
    #Names the window Game
    pygame.display.set_caption("Game")
    
    while running == True:
        screen.fill((0, 0, 0))
        choices1 = {"1": "Sword", "2": "Hammer", "3": "Apple"}
        
        #Establishes font and word size for words appearing on screen      
        Font = pygame.font.SysFont('arial', 30)
        
        white = ((255, 255, 255))

        #creates variable for both the prompt and options
        prompt = Font.render("You wake up in cold cell. You have no idea how you got there, but you can hear voices coming toward you.", True, white)
        prompt2 = Font.render("Before you lies a hammer, a sword, and an apple. Which do you take? ", True, white)
        choices = Font.render("(Use number keys) 1) Sword 2) Hammer 3) Apple ", True, white)
        
        #recreates surfaces on new scren
        imagebox = pygame.Surface(((SCREEN_WIDTH/1.27), (SCREEN_HEIGHT/1.51)), pygame.SRCALPHA, 32)
        inventory = pygame.Surface(((SCREEN_WIDTH/5.5), (SCREEN_HEIGHT/ 1.51)))
        chatbox = pygame.Surface(((SCREEN_WIDTH/1.025), (SCREEN_HEIGHT/ 3.17)), pygame.SRCALPHA, 32)
        scene1 = pygame.Surface(((SCREEN_WIDTH), (SCREEN_HEIGHT)), pygame.SRCALPHA, 32)
        endscene1 = pygame.Surface(((SCREEN_WIDTH), (SCREEN_HEIGHT)), pygame.SRCALPHA, 32)
        
        #loads in the beginning scene image
        #There were going to be more images following the same format, but I ra out of time
        scene1 = (pygame.image.load(os.path.join("Scenes", "New Piskel.gif")))
        scene1 = (pygame.transform.scale(scene1, ((SCREEN_WIDTH/1.278), (SCREEN_HEIGHT/1.53))))
        endscene1 = (pygame.image.load(os.path.join("Scenes", "New Piskel (1).gif")))



        #fills surface colors with color
        imagebox.fill((255, 255, 255))
        rect = imagebox.get_rect()
        inventory.fill((255, 255, 255))
        rect = inventory.get_rect()
        chatbox.fill((255, 255, 255))
        rect = chatbox.get_rect()
        chatbox1.fill((0, 0, 0))
        rect = chatbox1.get_rect()
        
        #Places rectangles, text, and images in place
        imagebox.blit(scene1,((SCREEN_WIDTH/400), (SCREEN_HEIGHT/201)))
        screen.blit(imagebox, ((SCREEN_WIDTH/5), (SCREEN_HEIGHT/150)))
        screen.blit(inventory, ((SCREEN_WIDTH/83.3), (SCREEN_HEIGHT/ 150)))
        screen.blit(chatbox, ((SCREEN_WIDTH/83.3), (SCREEN_HEIGHT/1.48)))
        screen.blit(chatbox1, ((SCREEN_WIDTH/66), (SCREEN_HEIGHT/1.47)))
        
        screen.blit(prompt, ((SCREEN_WIDTH/40), (SCREEN_HEIGHT/1.45)))
        screen.blit(prompt2, ((SCREEN_WIDTH/40), (SCREEN_HEIGHT/1.36)))
        
        imagebox.blit(scene1, ((SCREEN_WIDTH/400), (SCREEN_HEIGHT/201)))                 
            
        #checks to make sure the loop hasn't been exited and to see if a pressed key matches one of the number keys, executing a function if it was
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == pygame.K_1:
                    choice = choices1["1"]
                    
                    ending(running, choice, choices)
                    
                    return choice
                elif event.key == K_2:
                    print("key 2 pressed")
                    choice = choices1["2"]
                    
                    ending(running, choice, choices)
                    
                    return choice
                elif event.key == K_3:
                    print("key 3 pressed")
                    choice = choices1["3"]
                    
                    ending(running, choice, choices)

                    return choice
            elif event.type == QUIT:
                running = False
            else:
                running = True
        
        pygame.display.update()
        
    return running    

def Settings():
        print("Sorry, didn't have time for a propper menu")

#main loop
while running == True:
    #look at queued events
    for event in pygame.event.get():
        #user hit key?
        if event.type == KEYDOWN:
            #was it escape? If so, exit loop
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
            
    #fills screen
    screen.fill((0, 0, 0))

    #creates surfaces of different widths and heights
    imagebox = pygame.Surface(((SCREEN_WIDTH/1.27), (SCREEN_HEIGHT/1.51)), pygame.SRCALPHA, 32)
    inventory = pygame.Surface(((SCREEN_WIDTH/5.5), (SCREEN_HEIGHT/ 1.51)))
    chatbox = pygame.Surface(((SCREEN_WIDTH/1.025), (SCREEN_HEIGHT/ 3.17)), pygame.SRCALPHA, 32)
    iib = pygame.Surface(((SCREEN_WIDTH/1.278), (SCREEN_HEIGHT/1.53)), pygame.SRCALPHA, 32)
    scene1 = pygame.Surface(((SCREEN_WIDTH), (SCREEN_HEIGHT)), pygame.SRCALPHA, 32)
    chatbox1 = pygame.Surface(((SCREEN_WIDTH/1.031), (SCREEN_HEIGHT/ 3.27)), pygame.SRCALPHA, 32)

    #fills surface colors with colors and makes them rectangles and sets images and sizes them
    imagebox.fill((255, 255, 255))
    rect = imagebox.get_rect()
    inventory.fill((255, 255, 255))
    rect = inventory.get_rect()
    chatbox.fill((255, 255, 255))
    rect = chatbox.get_rect()
    
    iib = (pygame.image.load(os.path.join ("TitleScreen", "Games1.png")).convert_alpha()) #establishes the iib (image in image box) and makes it transparent
    iib = pygame.transform.scale(iib, ((SCREEN_WIDTH/1.278), (SCREEN_HEIGHT/1.53))) #scales the iib

    #actaully puts the surface on the screen
    imagebox.blit(iib, ((SCREEN_WIDTH/400), (SCREEN_HEIGHT/201)))
    screen.blit(imagebox, ((SCREEN_WIDTH/5), (SCREEN_HEIGHT/150)))
    screen.blit(inventory, ((SCREEN_WIDTH/83.3), (SCREEN_HEIGHT/ 150)))
    screen.blit(chatbox, ((SCREEN_WIDTH/83.3), (SCREEN_HEIGHT/1.48)))
    

    def Settings():
        print("Sorry, haven't had time for that one yet, but you're welcome to go to the game.")
    
    start_button = Button(
    # Mandatory Parameters
    screen,  # Surface to place button on
    (SCREEN_WIDTH/1.993),  # X-coordinate of top left corner
    (SCREEN_HEIGHT/2.65),  # Y-coordinate of top left corner
    (SCREEN_WIDTH/5.18),  # Width
    (SCREEN_HEIGHT/18.5),  # Height

    # Optional Parameters
    textColour = (255, 255, 255), # color of font
    text='Start',  # Text to display   
    fontSize = 50,  # Size of font
    margin = 20,  # Minimum distance between text/image and edge of button
    inactiveColour = (0, 0, 0),  # Colour of button when not being interacted with
    hoverColour = (105, 105, 105),  # Colour of button when being hovered over
    pressedColour = (0, 200, 20),  # Colour of button when being clicked
    radius = 9,  # Radius of border corners (leave empty for not curved)
    onClick = lambda: Beginning(running, scene1)  # Function to call when clicked on
    )
    
    options_button = Button(
    # Mandatory Parameters
    screen,  # Surface to place button on
    (SCREEN_WIDTH/1.997),  # X-coordinate of top left corner
    (SCREEN_HEIGHT/2.215),  # Y-coordinate of top left corner
    (SCREEN_WIDTH/5.1),  # Width
    (SCREEN_HEIGHT/19.5),  # Height

    # Optional Parameters
    textColour = (255, 255, 255), # color of font
    text='Settings',  # Text to display   
    fontSize = 50,  # Size of font
    margin = 20,  # Minimum distance between text/image and edge of button
    inactiveColour = (0, 0, 0),  # Colour of button when not being interacted with
    hoverColour = (105, 105, 105),  # Colour of button when being hovered over
    pressedColour = (0, 200, 20),  # Colour of button when being clicked
    radius = 9,  # Radius of border corners (leave empty for not curved)
    onClick = lambda: Settings()  # Function to call when clicked on
    )

    Exit_button = Button(
    # Mandatory Parameters
    screen,  # Surface to place button on
    (SCREEN_WIDTH/2.005),  # X-coordinate of top left corner
    (SCREEN_HEIGHT/1.905),  # Y-coordinate of top left corner
    (SCREEN_WIDTH/5),  # Width
    (SCREEN_HEIGHT/19.9),  # Height

    # Optional Parameters
    textColour = (255, 255, 255), # color of font
    text='Exit',  # Text to display   
    fontSize = 50,  # Size of font
    margin = 20,  # Minimum distance between text/image and edge of button
    inactiveColour = (0, 0, 0),  # Colour of button when not being interacted with
    hoverColour = (105, 105, 105),  # Colour of button when being hovered over
    pressedColour = (0, 200, 20),  # Colour of button when being clicked
    radius = 9,  # Radius of border corners (leave empty for not curved)
    onClick = lambda: pygame.quit() # this exits the game, but it also results in an exception when the window closes. I think this is just how the function works.
    )
    
    pw.update(events)  # Call once every loop to allow widgets to render and listen
    pygame.display.update()
         