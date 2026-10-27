def count_cards(cards: list[str]) -> int:
    """Calculates the total value of the given cards in a blackjack game.

    Face cards (J, Q, K) count as 10, numbered cards count as their value,
    and Aces count as 11 or 1, adjusting to avoid going over 21.

    Args:
        cards (list of str): A list of card values, e.g., ['A', '7', 'K'].
	"""
    card_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10, 'K': 10, 'A': 11
        }

    total = 0
    aces = 0
    for card in cards:
        if card not in card_values:
            raise ValueError(f"Invalid card: {card}")

        # Add card value to total
        total += card_values[card]
        if card == 'A':
            aces += 1

    # Adjust for Aces if total is over 21
    while total >= 21 and aces:
        total -= 10
        aces -= 1

    return total