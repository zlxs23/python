''' CLI User Interface for Tic-Tac-Toie game.
    Use as the main program, no reusable functions'''

import oxo_logic
import tkinter
import tkinter.messagebox as mb

menu = ["Start new game",
        "Resume saved game",
        "Display help",
        "Quit"]

def getMenuChoice(aMenu):
    ''' getMenuChoice(amenu) -> int

        takes a list of strings as input,
        displays as a numbered menu and
        loops until user selects a valid number'''
    
    if not aMenu: raise ValueError('No menu content')
    while True:
        for index, item in enumerate(aMenu, start=1):
            print(index, "\t", item)
        try:
            choice = int(input("\nChoose a menu option: "))
            if 1 <= choice <= len(aMenu):
                return choice
            else: print("Choose a number between 1 and", len(aMenu))
        except ValueError:
            print("Choose the number of an option")


def startGame():
    return oxo_logic.newGame()

def resumeGame():
    return oxo_logic.restoreGame()

def displayHelp():
    print('''
    Start new game:  starts a new game of tic-tac-toe
    Resume saved game: restores the last saved game and commences play
    Display help: shows this page
    Quit: quits the application
    ''')

def quit():
    print("Goodbye...")
    raise SystemExit

def executeChoice(choice):
    ''' executeChoice(int) -> None

        Execute whichever option the user selected.
    If the choice produces a valid game then
    play the game until it completes.'''
    
    dispatch = [startGame, resumeGame, displayHelp, quit]
    game = dispatch[choice-1]()
    if game:
        playGame(game)

def printGame(game):
    display = '''
      1 | 2 | 3      {} | {} | {}
     ----------     -----------
      4 | 5 | 6      {} | {} | {}
      ---------     -----------
      7 | 8 | 9      {} | {} | {}
      '''
    print(display.format(*game))

def playGame(game):
    result = ""
    while not result:
        printGame(game)
        choice = input("Cell[1-9 or q to quit]: ")
        if choice.lower()[0] == 'q':
            save = mb.askyesno("Save game","Save game before quitting?")
            if save:
                oxo_logic.saveGame(game)
            quit()
        else:
            try:
                cell = int(choice)-1
                if not (0 <= cell <= 8):
                    raise ValueError
            except ValueError:
                print("Choose a number or 'q' to quit")
                continue

            try:
                result = oxo_logic.userMove(game,cell)
            except ValueError:
                mb.showerror("Invalid cell", "Choose an empty cell")
                continue
            if not result:
                result = oxo_logic.computerMove(game)
            if not result:
                continue
            elif result == 'D':
                printGame(game)
                mb.showinfo("Result", "It's a draw")
            else:
                printGame(game)
                mb.showinfo("Result", "Winner is {}".format(result))

def main():
    top = tkinter.Tk()
    top.withdraw()
    while True:
       choice = getMenuChoice(menu)
       executeChoice(choice)

if __name__ == "__main__": main()
