import runpy
print('Welcome to Fantasy Quest! Enter your character details to begin your adventure.')
name = input('Enter your character name: ')
race = input('1. Human \n 2. Elf \n 3. Dwarf \n 4. Orc \n Choose a race: ')
match race:
    case '1':
        race = 'Human'
    case '2':
        race = 'Elf'
    case '3':
        race = 'Dwarf'
    case '4':
        race = 'Orc'
    case _:
        print('Invalid selection. Try again.')
        race = input('Choose a race: \n1. Human\n2. Elf\n3. Dwarf\n4. Orc\n Choose a race: ')
level = 1
health = 10
inventory = []
confirm = input(f'{name}, {race} \n 1. Yes \n 2. No \n Is this correct?: ')
match confirm:
    case '1':
        from player import charClass
        player = charClass(name, race, level, health, inventory)
        print(player.name + ' the ' + player.race + ', embarks on a grand adventure!')
        #game start
    case '2':
        print('Restarting character creation...')
        runpy.run_path('newgame.py')
    case _:
        print('Invalid selection. Try again.')
#create save