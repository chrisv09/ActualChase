# The Chase Python Edition

import random
import time
import logging
import threading
import pyautogui
from tkinter import *

#TODO: Make point system for each player

def thread_function(name,qno=[],lines=[]):
    if name == 1:

        logging.info("Thread %s: starting", name)

        # Wait for enter button to start
        input('')
        print(qno)

        global points
        points = 0
        i = 0

        print(lines[i])

        # Go through cash builder questions
        while finish == False:

            
            stop = input('')

            # Stop if 's' is inputted
            if stop == 's' or finish == True:
                print("Final points: " + str(points))
                break

            # Give a point if 'a' is inputted
            elif stop == 'a':
                points += 1
                print(points)
            else:
                pass

            i += 1
            print(lines[i])
            
        logging.info("Thread %s: finishing", name)

def run_game():
    global finish
    finish = False

    # SETTINGS
    TIME_BEFORE_START = 1
    CASH_BUILDER_TIMER = 10

    # CASH BUILDER
    with open('cash_builder_qns.txt') as f:
        lines = f.read().splitlines()

    # Generate questions
    qno = random.sample(range(len(lines)), 15)

    # Start timer thread
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,qno,lines))

    logging.info("Main    : before running thread")
    x.start()

    logging.info("Main    : wait for the thread to finish")
    
    root = Tk()

    second = StringVar()
    timer = Label(textvariable = second, font = ('Times New Roman', 40))
    second.set("60")

    timer.pack()

    for i in range(1, TIME_BEFORE_START):
        second.set("Starting in" + str(TIME_BEFORE_START - i))
        root.update()
        time.sleep(1)
    
    for i in range(0,CASH_BUILDER_TIMER):
        # Temporary timer (will use tkinter to display)
        second.set(str(CASH_BUILDER_TIMER - i))
        root.update()
        time.sleep(1)
    
    second.set("0")
    root.update()

    
    
    finish = True

    # Automatically press enter to finish
    pyautogui.press('enter')

    x.join()

    

    print('Points (From main thread): ' + str(points))
    
    logging.info("Main    : all done")  

# Menu

if __name__ == "__main__":
    
    option = 0

    while option not in ['1', '2']:
        option = input("""Choose an option:
        1. Play Game
        2. Add Questions

        """)

    if option == '1':
        run_game()
    else:
        print("wip")
