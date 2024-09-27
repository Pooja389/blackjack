# blackjack
import random
ask = input("do you want to play blackjck 'yes' or 'no' :")
cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]

list_p = [] # list of cards of player
list_c = [] # list of cards of computer


# it gets player card and append to list of cards of player
def get_player_card():
    player_card = random.choice(cards)
    list_p.append(player_card)


# it gets computer card and append to list of cards of player   
def get_computer_card():
    computer_card = random.choice(cards)
    list_c.append(computer_card)


# asking if player wants to play
if ask == 'yes':
    
    get_player_card()
    get_player_card() 

    # printing the cards of player
    print("you have",list_p) 

    # printing the cards of computer]
    get_computer_card()
    print("computer have",list_c)  
    get_computer_card()

    while True:

        another_card = input("do you want to take another card 'yes' or 'no' :")
        if another_card == "yes":
            get_player_card()  
            print("you have",list_p)    
        else:
            break   
        computer_cards_sum = sum(list_c)
        if computer_cards_sum <= 17:
            get_computer_card()  

        player_cards_sum = sum(list_p)

        if player_cards_sum > 21:
            break


    player_cards_sum = sum(list_p)
    computer_cards_sum = sum(list_c)

    if player_cards_sum > 21 and computer_cards_sum > 21:
        print("draw, because computer have",list_c)    
    elif player_cards_sum > 21:
        print("computer won, because computer have", list_c)
    elif computer_cards_sum > 21:
        print("you won, because computer have", list_c)
    elif computer_cards_sum < player_cards_sum :
        print("you won, because computer have",list_c)    
    elif sum (list_p) < computer_cards_sum:
        print("computer won, because computer have",list_c)    
    else:
        print("draw,because computer have",list_c)    

else :
    print("bye bye")


