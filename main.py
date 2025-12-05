import sys
import runpy
print('Fantasy Quest // Version 0.1 \n 1. New Game \n 2. Load Game \n 3. Exit')
choice = input('Enter your choice: ')
match choice:
    case '1':
        print('Starting a new game...')
        runpy.run_path('newgame.py')
    case '2':
        print('Continuing your adventure...')
        #file select logic
    case '3':
        print('Farewell quester!')
        sys.exit()
    case _:
        print('Invalid choice. Try again.')
        choice = input('Enter your choice: ')