import random

def play():
    user = input("guess any ??? 'r' for rock ,'p' for paper, 's' for scissors:\n ")[0].lower()
    if user.isdigit():
        print("please enter letter not digit")
    com = random.choice(['r','p','s'])
    print(com)

    if user == com:
        return  "it is a tie"
    if is_win(user,com):
        return  'you won'
    else:
        return "you lose"

def is_win(player,oppent):

    if(player== 'r' and oppent == 's') or (player== 's' and oppent == 'p') or (player== 'p' and oppent == 'r'):
        return True


print(play())