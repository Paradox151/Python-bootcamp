game_on= True
players={}

while game_on:
    name=input("enter your name:  ")
    bid = int(input("enter your bid amount:  "))
    players[name]=bid
    play= input("is there any other bidder 'yes' or 'no'? ").lower()
    if play == "yes" :
         print("\n"*100)
         
       
    else:
         
         winner= max(players, key=players.get)
         winner_bid = players[winner]
         print(f" the winner is {winner} with the bid amount of $ {winner_bid}")
         game_on=False


    