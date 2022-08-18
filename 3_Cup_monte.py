from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return(mylist)
    
def player_guess():
    
    guess=''
    
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0,1 or 2: ")
        
    return int(guess)
    
def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print('Correct!')
    else:
        print("Wrong guess!")
        print(mylist)
        
        
#inital List
mylist = ['','0','']

#Shuffle List
mixedup_list = shuffle_list(mylist)

#user guess
guess = player_guess()

#Check Guess
check_guess(mixedup_list,guess)
