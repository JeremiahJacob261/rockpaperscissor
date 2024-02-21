# This is a sample Python script.
import random
import string


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    dist = { 0:'r',1:'p',2:'s' }
    full = { 'r' : "Rock", 'p':"Paper", 's': "Scissor"}
    # Use a breakpoint in the code line below to debug your script.\
    # Press Ctrl+F8 to toggle the breakpoint.
    print("Welcome To Jerry RPS\n")
    print("This is a rock, paper and scissor game\n let's play\n")
    decision = input("Choose your path Rock (r) or Paper (p) or Scissor (s) \n")
    rand = random.choice(string.digits)
    if(decision == dist[int(rand)%3]):
        print(f'You win, you chose {full[decision]}')
    else:
        print("you kinda lost")
        print(int(rand)%3)
    askagain()

def askagain():
    cvn = input('Do you wish to play again y/n ?\n')
    if cvn == 'y':
        print_hi()
    else:
        print('Thanks for playing, Come again')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
