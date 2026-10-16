# todo1 ; choose a random word from wordlist and assign it to  avariable and print it
# todo2 ; ask the user to guess a letter and make the guess to lower case
# todo3 ; check if the user gussed(guess) the right letter or not if yes then print 'right' else 'wrong'


import random
word_list=["apple", "cheery", "banana"]
choosen_word = random.choice(word_list)
print(choosen_word)

#guess = input("guess a letter: ").lower()

# for words in choosen_word:
#     if  guess == words:
#         print("right")
#     else:
#         print("wrong")

   
#todo1 ; create a placeholder to the random words with _
placeholder = ""
#todo2 create a "display" that put the guess letter in the tight position

# for words in choosen_word:
#     if  words == guess:
#         placeholder += guess
#     else:
#         placeholder += "_"
# print(placeholder)  

correct_letter = []
#todo1 ; use while loop to give another chance to type
game_over = False

lives = 6
stages = ["", "+", "++","+++", "++++", "+++++", "++++++" ]


while not game_over:
    guess = input("guess a letter: ").lower()

    placeholder = ""


#todo2 ; change the for loop so that you keep the previous correct
    
    # for words in choosen_word:
    #     if  words == guess:
    #         placeholder += words
    #         correct_letter.append(guess)
    #     elif words in correct_letter:
    #         placeholder+=  words
    #     else:
    #         placeholder += "_"
    # print(placeholder)  


    # if "_" not in placeholder:
    #     game_over = True
    #     print("game over you've won")

#todo1 ; create a variable called "lives" to keep track of the number of lives left
# set 'lives' to equal 6.


    for words in choosen_word:
        if  words == guess:
            placeholder += words
            correct_letter.append(guess)
        elif words in correct_letter:
            placeholder+=  words
        else:
            placeholder += "_"
    print(placeholder)  
    
#todo2 ; if guess is not the choosen_word then reduce lives by 1
# if lives went 0 then the game end and print you lose


    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            game_over= True
            print("game over you've lost")



    if "_" not in placeholder:
        game_over = True
        print("game over you've won")
#todo3 ; print ascii art from list that corresponds current numbers of lives

    print(stages[lives]) 
