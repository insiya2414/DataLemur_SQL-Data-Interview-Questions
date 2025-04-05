def max_satisfaction(expectations, cards):
    expectations.sort()
    cards.sort()
    
    expectation_index = 0  # pointer for expectations
    card_index = 0         # pointer for cards
    
    while expectation_index < len(expectations) and card_index < len(cards):
        if cards[card_index] >= expectations[expectation_index]:
            expectation_index += 1
        card_index += 1
    
    return expectation_index
    