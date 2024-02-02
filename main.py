import card

while True:
    plyr_points = sum(card_value(card) for card in plyr_card)
    house_points = sum(card_value(card) for card in house_points)

    print("Players cards: " + plyr_card)
    print("Players points: " + plyr_points)
    
    choice = input('What do you want? ["hit me" to get another card, "stop" to stop]: ').lower