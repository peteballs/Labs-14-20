import random
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '2', '3', '4', '5', '6', '7', '8', '9', '2', '3', '4', '5', '6', '7', '8', '9', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']
face_cards = ['J', 'Q', 'K']
ace = ['A']
acels = [1,11]

def first_card(card):
    return(random.choice(card))

def second_card(card):
    return(random.choice(card))

def additional_card(card):
    return(random.choice(card))

def main():

    initial_card = first_card(cards)
    print(f"The first card is.....{initial_card}")

    if initial_card in face_cards:
        initial_card = 10

    elif initial_card in ace:
        initial_card = (random.choice(acels))

    else: 
        print (initial_card)
        initial_card = int(initial_card)

    follow_card = second_card(cards)
    print(f"The second card is.....{follow_card}")

    if follow_card in face_cards:
        follow_card = 10
    
    elif follow_card in ace:
        follow_card = (random.choice(acels))

    else: 
        print(follow_card)
        follow_card = int(follow_card)

    total = (initial_card + follow_card)
    print(f"The total is {total}")

    if total == 21:
        reaction = "Congratulations Blackjack!!"
        print(reaction)
        quit()

    if total > 21:
        reaction = "Over and you automatically lost!!"
        print(reaction)
        quit()

    if total >= 17 and total <= 21:
        reaction = "Stay and you have a good chance at winning!!"
        print(reaction)
        quit()

    while True:
                
        if total < 17:
            reaction = "Hit"
            print(reaction)

            if reaction == "Hit":
                follow_card = additional_card(cards)
                print(f"The next card is {follow_card}")

                if follow_card in face_cards:
                    follow_card = 10

                elif follow_card in ace:
                    if total < 10:
                        follow_card = 11
                    if total > 10:
                        follow_card = 1

                else: 
                    print (follow_card)
                    follow_card = int(follow_card)
        
        total = (int(total)+int(follow_card))
        print(f"The total is {total}")
    
        if total == 21:
            reaction = "Congratulations Blackjack!!"
            print(reaction)
            break

        if total >= 17 and total <= 21:
            reaction = "Stay and you have a good chance at winning!!"
            print(reaction)
            break
    
        if total > 21:
            reaction = "Over and you automatically lost!!"
            print(reaction)
            break

main()


            

