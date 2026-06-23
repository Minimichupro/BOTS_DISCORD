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


def insult_giver():
    insult_list =[
                "99% of gamblers quit right before they hit it big. Too bad you literally can't afford to be the 1%.",
                "Go sell a kidney and come back. The jackpot is calling your name.",
                "Your wallet is emptier than your promises to stop gambling.",
                "Your wife took the kids, and now the machine is taking your dignity. Balance: $0."
                ]
    
    insult = random.choice(insult_list)
    return insult