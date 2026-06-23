import random


def slot_spin(bet):
    symbols = ["🍒", "🍋", "🍇"]
    
    spin_result = random.choices(symbols, k=3)
    slot_display = [spin_result[0], spin_result[1], spin_result[2]]
    len_result = len(set(spin_result))

    if len_result == 1:
        prize_mult = 3

    elif len_result == 2:
        prize_mult = 1.5

    else:
        prize_mult = 0
    
    return slot_display, prize_mult, bet * prize_mult