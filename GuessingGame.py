from random import randint

print()
print('*******Welcome to my Guessing Game*******')
print('')
print('This Progarma picks a random integer from 1 to 100, and has players guess the number.')
print('The rules are:')
print('2. On a player first turn, if their guess is' +
            'a. within 10 of the number, return "WARM!"' +
            'b. further than 10 away from the number, return "COLD!"')
print('3. On all subsequent turns, if a guess is'+
            'closer to the number than the previous guess return "WARMER!"'+
            'farther from the number than the previous guess, return "COLDER!"')

print('')
print('')

print("Let's start")
prev_num = None
count = 0
comp_num = randint(1,100)
#print(comp_num)
while True: 
    print('')
    print('Press 2 to Quit')
    print ('Press 1 to Play')
    user_choice = int(input('Please select your choice'))
    if(user_choice == 2):
        break
    elif(user_choice ==1 ):
        count = count +1
        user_num = int(input('Please guess your number'))  
        if (user_num < 1 or user_num >100):
            print('')
            print('OUT of Bounds, number should we within [1-100] range number inclusive')
        elif(prev_num is None):
            prev_num = user_num
            if (user_num < 1 or user_num >100):
                print('')
                print('OUT of Bounds, number should we within [1-100] range number inclusive')
            elif(user_num >= (comp_num-10) and user_num <= (comp_num +10)):
                print('')
                print('WARM!')
            else:
                print('')
                print('COLD!')
        elif(user_num == comp_num):
            print('You Have Gussed Correctly!!!! in {} chances.'.format(count))
            print('quitting the game')
            break
            
        else:
            prev_diff = abs (prev_num - comp_num)
            curr_diff = abs(user_num - comp_num)
            if(prev_diff > curr_diff):
                print('')
                print('Warmer!!! you are moving closer')
            else:
                print('')
                print('Colder!!! your current guess is moving away from correct guess')
            prev_num = user_num
        
    else:
        print('You have entered bad choice')
        
       