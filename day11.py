# creating blackjack game
from ast import Return
import random
import art

 
# your_card = [random.choice(cards)]
# comp_card = [random.choice(cards)]
# current_score = sum(your_card)
# final_hand= 0

# # def comp_final():
# #     while sum(comp_card) < 17:
# #         comp_card.append(random.choice(cards))
# #     final_hand = sum(comp_card)
# #     return(f"computers final hand: {comp_card} , final score : {final_hand}")
    
        
# # def display():
# #     your_card.append(random.choice(cards))
# #     current_score = sum(your_card)

# #     print(f'''your card: {your_card} , current score : {current_score}
# #         computers first card: {comp_card}''')
# #     return

# choice =input("do you want to play gam of black jack? type 'y' for yes 'n' for no : ").lower()

# playgame = "True"
# while playgame:
#     if choice == "y":
#         print("\n" * 20)
#         print(art.blackjack)
#         display()
            
#         replay =input("\ntype 'y' to get another card , 'n' to pass: ").lower()
#         while replay == "y":
            
#             if current_score <= 21:
#                 display()
#                 replay = input("type 'y' to get another card , 'n' to pass: ").lower()
#             else:   
#                 print("you went over 21, you lose😒")
#                 break
#         if replay == "n":
#             print("yur final hand: ", your_card, "final score: ", current_score)
#             print(comp_final())
#             if sum(comp_card) > 21:
#                 print("computer went over 21, you win😎")
#             elif sum(comp_card) > current_score:
#                 print("you lose😒")
#             elif sum(comp_card) < current_score:
#                 print("you win😎")
#             else:
#                 print("its a draw😐")
#         break

           
        
#     else:
#         playgame = "False"    

#     choice =input("do you want to play gam of black jack? type 'y' for yes 'n' for no : ").lower()            
            
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]



