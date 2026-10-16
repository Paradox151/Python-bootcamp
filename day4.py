#creating rock paper sessiors game using randomizationand other statements
import random
print("welcome to rock paper sessiors type 0 for rock 1 for paper 2 for scissors")
player = int(input(""))
computer = random.randint(0,2)
computer2 = random.randint(0,2)
if player == 0:
    print(''' your choose
                _______
            --'   ____)
                (_____)
                (_____)
                (____)
            --.__(___)
                        ''')
elif player == 1:
    print('''you choose
                    _______
                ---'   ____)____
                        ______)
                        _______)
                        _______)
                ---.__________)
                ''')
elif player ==2:
    print('''you choose
                _______
            ---'   ____)____
                    ______)
                __________)
                (____)
            --.__(___)''')
else:
    print("invalid response choosing random")
    print(computer)
    if  computer== 0:
        print(''' your choose
                _______
            --'   ____)
                (_____)
                (_____)
                (____)
            --.__(___)
                        ''')
    elif  computer == 1:
        print('''you choose
                    _______
                ---'   ____)____
                        ______)
                        _______)
                        _______)
                ---.__________)
                ''')
    elif  computer ==2:
        print('''you choose
                _______
            ---'   ____)____
                    ______)
                __________)
                (____)
            --.__(___)''')

if  computer2  == 0:
    print(''' computer choose 0
                _______
            --'   ____)
                (_____)
                (_____)
                (____)
            --.__(___)
                        ''')
elif  computer2  == 1:
    print('''computer choose 1
                    _______
                ---'   ____)____
                        ______)
                        _______)
                        _______)
                ---.__________)
                ''')
elif computer2 ==2:
    print('''computer choose 2
                _______
            ---'   ____)____
                    ______)
                __________)
                (____)
            --.__(___)''')


    