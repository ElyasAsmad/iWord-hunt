import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from music import MusicUtil
import string
import random
import pygame
from timeit import default_timer as timer
import sys

# alphabet_list = list(string.ascii_lowercase)

keys_list = []

for letter in range(pygame.K_a, pygame.K_z + 1):
    keys_list.append(letter)

# class HangmanGame():
#     def __init__(self, game_window: tk.Toplevel):
#         self.chances = 10
#         self.window = game_window
        
#     def start(self):
#         with open("answers.txt") as f:
#             words_list = f.readlines()
            
#         self.game_word = random.choice(words_list)
        
#         self.window.bind('<Key>', lambda e: self.on_key_pressed(e.keysym.lower()))

#     def on_key_pressed(self, key):
#         match key:
#             case key if key in alphabet_list:
white = (255, 255, 255)
black = (0, 0, 0)
lightred = (255, 165, 145)
darklightred = (255, 97, 81)
lightblue = (126,178,255)
darklightblue = (42, 129, 255)
lightgrey = (192, 192, 192)

width = 800
height = 600

textBoxSpace = 5
textBoxNumber = 0

fps = 30
music = MusicUtil("sdhr.mp3")

pygame.init()

def game_scaffold():
    
    global guesses, guessLett
    
    guesses = ''
    guessLett = ''
    
    print("islamic")
    music.start_playback()
    hangmanGame()

def hangman():
    global textBoxSpace, textBoxNumber
    while play == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                music.stop_playback()
                pygame.quit()
                sys.exit()

        screen.fill(white)
        space = 10
        textBoxSpace = 5
        
        text = pygame.font.Font("freesansbold.ttf",20)
        textSurf = text.render("Happy Eid Mubarak!",True,black)
        textRect = textSurf.get_rect()
        textRect.center = ((width/2),(height/2))
        screen.blit(textSurf, textRect)
        
        button("Start The Game",280,50,250,100,black,lightgrey,game_scaffold)
                    
        pygame.display.update()
        clock.tick(fps)
                
def button(word,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))

    buttonText = pygame.font.Font("freesansbold.ttf",20)
    buttonTextSurf = buttonText.render(word, True, white)
    buttonTextRect = buttonTextSurf.get_rect()
    buttonTextRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(buttonTextSurf, buttonTextRect)
    
def placeLetter(letter):
    global pick, pickSplit
    space = 10
    wordSpace = 0
    while wordSpace < len(pick):
        text = pygame.font.Font('freesansbold.ttf',40)
        if letter in pickSplit[wordSpace]:
            textSurf = text.render(letter,True,black)
            textRect = textSurf.get_rect()
            textRect.center = (((150)+space),(200))
            screen.blit(textSurf, textRect)
        wordSpace += 1
        space += 60

    pygame.display.update()
    clock.tick(fps)
    
def quitGame():
    music.stop_playback()
    pygame.quit()
    sys.exit()
    
def endGame():
    global textBoxSpace, textBoxNumber, end, start
    end = timer()
    print("Time it took: ",end - start)
    timeTaken = (end - start)
    textBoxSpace = 5
    textBoxNumber = 0
    message = "Time taken: " + str(round(timeTaken)) + "s"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                music.stop_playback()
                pygame.quit()
                sys.exit()
                
        button("Yes",(width/2)-50,420,100,50,darklightred,lightred,quitGame)
        button("No",(width/2)-50,500,100,50,darklightred,lightred,hangman)
        
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf = largeText.render("End Game?",True,darklightred)
        TextRect = TextSurf.get_rect()
        TextRect.center = (width / 2, height / 2)
        screen.blit(TextSurf, TextRect)

        textSurf = largeText.render(message,True,darklightred)
        textRect = textSurf.get_rect()
        textRect.center = (width/2,200)
        screen.blit(textSurf, textRect)
        
        pygame.display.update()
        clock.tick(fps)
    
def textBoxLetter(letter):
    global textBoxSpace, textBoxNumber
    if textBoxNumber <= 5:
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf = text.render(letter,True,black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace),(350))
        screen.blit(textSurf, textRect)

    elif textBoxNumber <= 10:
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf = text.render(letter,True,black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace),(400))
        screen.blit(textSurf, textRect)

    elif textBoxNumber <= 15:
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf = text.render(letter,True,black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace),(450))
        screen.blit(textSurf, textRect)

    elif textBoxNumber <= 20:
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf = text.render(letter,True,black)
        textRect = textSurf.get_rect()
        textRect.center = (((105)+textBoxSpace),(500))
        screen.blit(textSurf, textRect)  
        
    pygame.display.update()
    clock.tick(fps)
    
def on_key_pressed(key):
    
    global guesses, guessLett, failed, textBoxSpace, textBoxNumber, chances
    
    match key:
        case key if key in keys_list:
            
            key = chr(key)
            
            guessLett = guessLett + key
            guesses += guessLett
            print("letter a guessed")
            print("")
            for char in pick:
                if char in guesses:
                    print(char)
                else:
                    print("_")
                    failed += 1

            if guessLett in pick:
                placeLetter(key)
    
            if failed == 0:
                print("You got the word")
                print(pick)
                endGame()

            if guessLett not in pick:
                textBoxSpace += 40
                textBoxNumber += 1
                chances = chances - 1
                print("")
                print(textBoxNumber)
                print("")
                print("That letter is not in the word")
                textBoxLetter(key)

            if chances == 0:
                print("Sorry you have lost")
                print("The word was",pick)
                endGame()

def hangmanGame():
    
    with open("answers.txt") as f:
        words_list = f.readlines()
    
    global pause, pick, pickSplit, textBoxSpace, textBoxNumber, start, chances
    start = timer()
    chances = 10
    pick = random.choice(words_list)
    pickSplit = [pick[i:i+1] for i in range(0, len(pick), 1)]
    
    screen.fill(white)
    
    wordSpace = 0
    space = 10
    while wordSpace < len(pick):
        text = pygame.font.Font("freesansbold.ttf",40)
        textSurf1 = text.render("_",True,black)
        textRect1 = textSurf1.get_rect()
        textRect1.center = (((150)+space),(200))
        screen.blit(textSurf1, textRect1)
        space = space + 60
        wordSpace += 1
            
    gamePlay = True
    while gamePlay == True:

        if textBoxNumber == 5:
            textBoxSpace = 5
        if textBoxNumber == 10:
            textBoxSpace = 5
        if textBoxNumber == 15:
            textBoxSpace = 5

        pygame.draw.rect(screen, white, [550,20,200,20])
        text = pygame.font.Font("freesansbold.ttf",20)
        textSurf = text.render(("Chances: %s" % chances),False,black)
        textRect = textSurf.get_rect()
        textRect.topright = (700,20)
        screen.blit(textSurf, textRect)

        textTitle = pygame.font.Font("freesansbold.ttf",40)
        textTitleSurf = textTitle.render("Islamic Hangman", True, black)
        textTitleRect = textTitleSurf.get_rect()
        textTitleRect.center = ((width/2),50)
        screen.blit(textTitleSurf, textTitleRect)

        pygame.draw.rect(screen, black, [100,300,250,250],2)
        
        if chances == 19:
            pygame.draw.rect(screen,black,[450,550,100,10])
        elif chances == 18:
            pygame.draw.rect(screen,black,[550,550,100,10])
        elif chances == 17:
            pygame.draw.rect(screen,black,[650,550,100,10])
        elif chances == 16:
            pygame.draw.rect(screen,black,[500,450,10,100])
        elif chances == 15:
            pygame.draw.rect(screen,black,[500,350,10,100])
        elif chances == 14:
            pygame.draw.rect(screen,black,[500,250,10,100])
        elif chances == 13:
            pygame.draw.rect(screen,black,[500,250,150,10])
        elif chances == 12:
            pygame.draw.rect(screen,black,[600,250,100,10])
        elif chances == 11:
            pygame.draw.rect(screen,black,[600,250,10,50])
        elif chances == 10:
            pygame.draw.line(screen,black,[505,505],[550,550],10)
        elif chances == 9:
            pygame.draw.line(screen,black,[550,250],[505,295],10)
        elif chances == 8:
            pygame.draw.line(screen,black,[505,505],[460,550],10)
        elif chances == 7:
            pygame.draw.circle(screen,black,[605,325],30)
        elif chances == 6:
            pygame.draw.rect(screen,black,[600,350,10,60])
        elif chances == 5:
            pygame.draw.rect(screen,black,[600,410,10,60])
        elif chances == 4:
            pygame.draw.line(screen,black,[605,375],[550,395],10)
        elif chances == 3:
            pygame.draw.line(screen,black,[605,375],[650,395],10)
        elif chances == 2:
            pygame.draw.line(screen,black,[605,465],[550,485],10)
        elif chances == 1:
            pygame.draw.line(screen,black,[605,465],[650,485],10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                global failed
                failed = 0
                print("Failed",failed)
                print("Chance", chances)
                
                if event.key == pygame.K_SPACE:
                    pause()
                    
                if event.key == pygame.K_ESCAPE:
                    gamePlay = False
                    
                on_key_pressed(event.key)
                
        pygame.display.update()
        clock.tick(fps)

    pygame.display.update()
    clock.tick(fps)

    

class MainWindow():

    def __init__(self, bg_image, window):
        self.music_player = MusicUtil("sdhr.mp3")

        self.window = window
        self.window.geometry('600x400')
        self.window.title("Game menu")

        #Set Dimensions
        self.canvas = tk.Canvas(self.window, width=600, height=400)
        self.canvas.pack()

        # Create Background image
        self.canvas.create_image(0, 0, anchor="nw", image=bg_image)

        frame = tk.Frame()
        frame.pack()

        # Create a label for the title
        self.title_label = tk.Label(self.window, text="iWord Hunt!", font=("Inter", 24))
        self.title_label.pack(pady=30)

        # Create a button to start the game
        self.start_button = tk.Button(self.window, text="Start Game", command=self.start_game, font=("Inter", 16))
        self.start_button.pack(pady=10)

        # Create a option button
        self.option_button = tk.Button(self.window, text="Option", command= self.option_page , font=("Inter", 16))
        self.option_button.pack(pady=10)

        # Create a button to exit the game
        self.exit_button = tk.Button(self.window, text="Exit", command=self.exit_program, font=("Inter", 16))
        self.exit_button.pack(pady=10)
        
        self.window.protocol("WM_DELETE_WINDOW", self.exit_program)

    # Define function to start the game
    def start_game(self):
        #  Create the game window
        self.game_window = tk.Toplevel(self.window)
        self.game_window.title("My Game")
    
        # Create the game content
        # self.game_label = tk.Label(self.game_window, text="iWord Hunt!", font=("Inter", 24), bg="blue", width=400, height=300)
        # self.game_label.pack(pady=20)

        hangmanGame()
        # game = HangmanGame(self.game_window)
                
        # Hide the main menu window
        self.window.withdraw()
        
        self.game_window.protocol("WM_DELETE_WINDOW", self.exit_program)

    def option_page(self):
        # Create option window
        game_option = tk.Toplevel(self.window)
        game_option.title("Game Option")

        # Create option content
        game_option_label = tk.Label(game_option, text="Game Option", font=("Inter", 24), bg="green", fg="black", width=400, height=300)
        print("1.Language 2.Volume")

    def exit_program(self):
        
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.music_player.stop_playback()
            self.window.destroy()

    def run(self):
        self.music_player.start_playback()
        self.window.mainloop()

if __name__ == "__main__":

    global clock, screen, play
    play = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Islamic Hangman!")

    while True:
        hangman()
    
    # global screen, clock
    
    # screen = pygame.display.set_mode((width, height))
    # clock = pygame.time.Clock()
    
    # main_window = tk.Tk()

    # bg_image = tk.PhotoImage(file="eid.png")

    # w = MainWindow(bg_image, main_window)
    # w.run()