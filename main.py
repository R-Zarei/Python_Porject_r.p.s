import random as ran

n_game = 0
n_equal = 0


def check_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True


def game():
    global n_game
    n_game += 1
    while 1:
        user = input("Enter your choice -> 'p' for paper, 's' for scissor, 'r' for rock:")
        if user == 'r' or user == 'p' or user == 's':
            break
    computer = ran.choice(['p', 's', 'r'])

    if user == computer:
        global n_equal
        n_equal += 1
        print(f"Equalised! Computer choice is {computer}")
        return game()
    elif check_win(user, computer):
        print(f"Points for you! Computer choice is {computer}")
        return 1
    elif not check_win(user, computer):
        print(f"Points for computer! Computer choice is {computer}")
        return 0


def R_P_S():
    n_computer = 0
    n_user = 0
    computer = 0
    user = 0
    win = 'n'
    while not ((abs(n_user - n_computer) == 5) or (abs(user - computer) >= 10)):
        g = game()
        if g and (win == 'n' or win == 'c'):
            n_user += 1
            user += 1
            win = 'u'
            n = 0
        elif g and win == 'u':
            n += 1
            n_user += 1
            user += 2 ** n
        elif not g and (win == 'n' or win == 'u'):
            n_computer += 1
            computer += 1
            win = 'c'
            m = 0
        elif not g and win == 'c':
            m += 1
            n_computer += 1
            computer += 2 ** m
        print(user, computer)

    if user > computer:
        print("__________YOU_WIN__________ :)")
    else:
        print("__________YOU_LOST__________ :(")

    print(f"game :{n_game}      equal :{n_equal}\nPlayer          Computer\nWin:{n_user}           Win:{n_computer}\nPoint:{user}         Point:{computer}")

    while 1:
        x = input("New Game?(yes/no):")
        if x == "yes" or x == "no":
            break
    if x == "yes":
        R_P_S()


R_P_S()












