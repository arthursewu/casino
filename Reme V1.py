import random
import time

a = 4
b = -5
global player_money
player_money = 1000
player_count = list()
house_count = list()
player_hand = list()
house_hand = list()
deck = ["♠️", "2 ♠️", "3 ♠️", "4 ♠️", "5 ♠️", "6 ♠️", "7 ♠️", "8 ♠️", "9 ♠️", "10 ♠️", "K ♠️", "Q ♠️", "J ♠️", "♥", "2 ♥", "3 ♥", "4 ♥", "5 ♥", "6 ♥", "7 ♥", "8 ♥", "9 ♥", "10 ♥", "K ♥", "Q ♥", "J ♥", "♣️", "2 ♣️", "3 ♣️", "4 ♣️", "5 ♣️", "6 ♣️", "7 ♣️", "8 ♣️", "9 ♣️", "10 ♣️", "K ♣️", "Q ♣️", "J ♣️", "♦️", "2 ♦️", "3 ♦️", "4 ♦️", "5 ♦️", "6 ♦️", "7 ♦️", "8 ♦️", "9 ♦️", "10 ♦️", "K ♦️", "Q ♦️", "J ♦️" ]


def main():
    print(" Welcome to the Casino !")
    main_page()

def main_page(): #Main Page
    print("--------------------------", "What would you like to do?", "1. Casino", "2. Reme", "3. Blackjack", "4. Exit", sep="\n")
    while True:
        try:
            action = int(input("Select an action by it's index number : "))
            if action in [1,2,3,4]:
                break
            else:
                print("Error : Please select a valid number")
        except ValueError:
            print("Error : Please select a valid number") 
    if action == 1:
        casino()
    elif action == 2:
        reme()
    elif action == 3:
        blackjack()
    else:
        print("Thanks for playing !")
        exit()
                      
def casino(): #Full casino code
    global player_money
    print(f"{'===== Casino =====' : ^30}", "How much would you like to bet ?", f"{'-Type 0 to go back-' : >25}", sep="\n")
    print(f"{'Your Balance is : $' : >22}", player_money)
    while True:
        try:
            bet = int(input("Bet : $"))
            if 0 <= bet <= player_money:
                break
            else:
                print("Error : Please enter a valid amount")
        except ValueError:
            print("Error : Please enter a valid amount")
    if bet == 0:
        main_page()
    else:
        player_money = player_money - bet
        player = random.randint(0,36)
        house = random.randint(0,36)
        time.sleep(2)
        print("House : ", house)
        time.sleep(2)
        print("Player : ", player)
        time.sleep(1)
        if player == 0:
            if house == 0:
                print(" ! Better luck next time !")
                casino()
            else:
                player_money = player_money + bet * 2
                print(" ! Congratulations you have won ! ")
        elif house > player or house == 0:
            print(" ! Better luck next time !")
            casino()
        else:
            player_money = player_money + bet * 2
            print(" ! Congratulations you have won ! ")
            casino()

def reme(): #Full reme code
    global player_money
    print(f"{'===== Reme =====' : ^30}", "How much would you like to bet ?", f"{'-Type 0 to go back-' : >25}", sep="\n")
    print(f"{'Your Balance is : $' : >22}", player_money)
    while True:
        try:
            bet = int(input("Bet : $"))
            if 0 <= bet <= player_money:
                break
            else:
                print("Error : Please enter a valid amount")
        except ValueError:
            print("Error : Please enter a valid amount")
    if bet == 0:
        main_page()
    else:
        player_money = player_money - bet
        player = str(random.randint(0,36))
        house = str(random.randint(0,36))
        time.sleep(2)
        print("House : ", house)
        time.sleep(2)
        print("Player : ", player)
        time.sleep(1)
        try:
            player_reme = int(player[0]) + int(player[1])
        except:
            player_reme = int(player[0])
        try:
            house_reme = int(house[0]) + int(house[1])
        except:
            house_reme = int(house[0])
        if player_reme == 0:
            if house_reme == 0:
                print(" ! Better luck next time !")
                reme()
            elif house_reme != 0:
                player_money = player_money + bet * 3
                print(" ! Congratulations you have won ! ")
                reme()
        elif house_reme == 0 or house_reme > player_reme:
            print(" ! Better luck next time !")
            reme()
        elif house_reme == player_reme:
            print(" ! Better luck next time !")
            reme()
        elif player_reme > house_reme:
            player_money = player_money + bet * 2
            print(" ! Congratulations you have won ! ")
            reme()

def blackjack_hit():
    global a
    global player_value
    for _ in range(1):
        a = a + 6
        player_hand.append(deck[a])
    for i in player_hand:
        print(i)
    player_value = 0
    blackjack_bust()

def blackjack_bust():
    global player_value
    for i in player_hand:
        match i:
            case "2 ♠️" | "2 ♥" | "2 ♣️" | "2 ♦️":
                value = 2
            case "3 ♠️" | "3 ♥" | "3 ♣️" | "3 ♦️":
                value = 3
            case "4 ♠️" | "4 ♥" | "4 ♣️" | "4 ♦️":
                value = 4
            case "5 ♠️" | "5 ♥" | "5 ♣️" | "5 ♦️":
                value = 5
            case "6 ♠️" | "6 ♥" | "6 ♣️" | "6 ♦️":
                value = 6
            case "7 ♠️" | "7 ♥" | "7 ♣️" | "7 ♦️":
                value = 7
            case "8 ♠️" | "8 ♥" | "8 ♣️" | "8 ♦️":
                value = 8
            case "9 ♠️" | "9 ♥" | "9 ♣️" | "9 ♦️":
                value = 9
            case "10 ♠️" | "10 ♥" | "10 ♣️" | "10 ♦️":
                value = 10
            case "K ♠️" | "K ♥" | "K ♣️" | "K ♦️":
                value = 10
            case "Q ♠️" | "Q ♥" | "Q ♣️" | "Q ♦️":
                value = 10
            case "J ♠️" | "J ♥" | "J ♣️" | "J ♦️":
                value = 10
            case "♠️" | "♥" | "♣️" | "♣️" | "♦️":
                value = 11
        player_count.append(value)
    player_value = sum(player_count)
    if player_value > 21:
        print("You lost")
        exit()
    else:
        blackjack_ask()

def blackjack_ask():
    while True:
        try:
            hit_action = int(input("Select an action : "))
            if hit_action in [1,2]:
                break
            else:
                print("Error : Please select an action by it's index")
        except:
            print("Error : Please select an action by it's index")
    if hit_action == 1:
        blackjack_hit()
    else:
        blackjack_stand()

def blackjack_stand():
    global house_value
    try:
        print( f"House Hand : {house_hand[0]}, {house_hand[1]}", {house_hand[2]})
    except:
        print( f"House Hand : {house_hand[0]}, {house_hand[1]}",)
    house_value = 0
    for i in house_hand:
        match i:
            case "2 ♠️" | "2 ♥" | "2 ♣️" | "2 ♦️":
                value = 2
            case "3 ♠️" | "3 ♥" | "3 ♣️" | "3 ♦️":
                value = 3
            case "4 ♠️" | "4 ♥" | "4 ♣️" | "4 ♦️":
                value = 4
            case "5 ♠️" | "5 ♥" | "5 ♣️" | "5 ♦️":
                value = 5
            case "6 ♠️" | "6 ♥" | "6 ♣️" | "6 ♦️":
                value = 6
            case "7 ♠️" | "7 ♥" | "7 ♣️" | "7 ♦️":
                value = 7
            case "8 ♠️" | "8 ♥" | "8 ♣️" | "8 ♦️":
                value = 8
            case "9 ♠️" | "9 ♥" | "9 ♣️" | "9 ♦️":
                value = 9
            case "10 ♠️" | "10 ♥" | "10 ♣️" | "10 ♦️":
                value = 10
            case "K ♠️" | "K ♥" | "K ♣️" | "K ♦️":
                value = 10
            case "Q ♠️" | "Q ♥" | "Q ♣️" | "Q ♦️":
                value = 10
            case "J ♠️" | "J ♥" | "J ♣️" | "J ♦️":
                value = 10
            case "♠️" | "♥" | "♣️" | "♣️" | "♦️":
                value = 11
        house_count.append(value)
    house_value = sum(house_count)
    blackjack_house()

def blackjack_house():
    if house_value < 17:
        house_hand.append(deck[-16])
        blackjack_stand()
    else:
        blackjack_final()

def blackjack_final():
    if house_value > 21 or player_value > house_value:
        print("You Win")
        player_money = player_money + bet * 2
    elif house_value == player_value:
        print("Draw")
    else:
        print("You Lost")

def blackjack():
    global player_money
    global house_hand
    global player_hand
    print(f"{'===== Blackjack =====' : ^32}", "How much would you like to bet ?", f"{'-Type 0 to go back-' : >25}", sep="\n")
    print(f"{'Your Balance is : $' : >22}", player_money)
    while True:
        try:
            bet = int(input("Bet : $"))
            if 0 <= bet <= player_money:
                break
            else:
                print("Error : Please enter a valid amount")
        except ValueError:
            print("Error : Please enter a valid amount")
    if bet == 0:
        main_page()
    else:
        player_money = player_money - bet
    random.shuffle(deck)
    x = 3
    y = -4
    for _ in range(2):
        player_hand.append(deck[x])
        house_hand.append(deck[y])
        x = x + 6
        y = y -6
    print("=============================",f"House Hand : {house_hand[0]}", f"Player Hand : {player_hand[0]}, {player_hand[1]}", "*What would you like to do ?*", "1. Hit", "2. Stand", sep="\n")
    blackjack_bust()
    while True:
            try:
                action = int(input("Select an action : "))
                if action in [1,2,3]:
                    break
                else:
                    print("Error : Please select an action by it's index")
            except:
                print("Error : Please select an action by it's index")
    if action == 1:
        blackjack_hit()
    elif action == 2:
        blackjack_stand()

main()