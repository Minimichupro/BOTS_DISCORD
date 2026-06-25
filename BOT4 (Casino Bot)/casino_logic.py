import random


def slot_spin(bet):
    symbols = ["🍒", "🍋", "🍇", "🍊", "💎"]
    
    spin_result = random.choices(symbols, k=3)
    slot_display = [spin_result[0], spin_result[1], spin_result[2]]
    len_result = len(set(spin_result))

    if len_result == 1:
        prize_mult = 3

    elif len_result == 2:
        prize_mult = 1.5

    else:
        prize_mult = 0

    final_prize = int(bet * prize_mult)
    
    return slot_display, prize_mult, final_prize


def pick_daily():
    outcomes = ["standard", "loss", "jackpot"]
    probabilities = [0.70, 0.20, 0.10]

    chosen_outcome = random.choices(outcomes, weights=probabilities)[0]
    
    if chosen_outcome == "standard":
        reward = random.randint(50, 150)
        msg = daily_insult_giver_standard()

    elif chosen_outcome == "loss":
        reward = random.randint(-1000, -500)
        msg = daily_insult_giver_loss()
    
    else:
        reward = random.randint(3000, 4000)
        msg = daily_insult_giver_jackpot()

    return chosen_outcome, reward, msg




## INSULT GIVERS
def slots_insult_giver_broke():
    insult_list =[
                "99% of gamblers quit right before they hit it big. Too bad you literally can't afford to be the 1%.",
                "Go sell a kidney and come back. The jackpot is calling your name.",
                "Your wallet is emptier than your promises to stop gambling.",
                "Your wife took the kids, and now the machine is taking your dignity. Balance: $0."
                ]
    
    insult = random.choice(insult_list)
    return insult



def balance_insult_giver_broke():
    insult_list =["Time to sell a kidney. You don't really need two of them to gamble anyway.",
                  "Your bank account is a perfect visual representation of a mid-life crisis.",
                  "Congratulations, you've hit rock bottom. The only way from here is up... or a sketchy payday loan.",
                  "Your credit score just took a look at your balance and died on the spot."
                  ]
    
    insult = random.choice(insult_list)
    return insult


def balance_insult_giver_poor():
    insult_list =["Enough to buy a cheap bottle of whiskey to forget your terrible life choices.",
                  "You are officially one bad bet away from selling feet pics on the internet.",
                  "This is pathetic. Even the local strip club wouldn't let you past the front door.",
                  "Just enough for a fast-food meal, assuming you skip the drink. Pure luxury."
                  ]
    
    insult = random.choice(insult_list)
    return insult


def balance_insult_giver_mid():
    insult_list =["Not bad. Enough to pay rent, but being responsible is for nerds. Go double it on red.",
                  "A solid stack. Enough to make your ex regret leaving you, at least until tomorrow.",
                  "You are officially rich enough to make stupid decisions with absolute confidence.",
                  "Respectable. You can actually afford to buy a round of drinks without checking your bank app first."
                  ]
    
    insult = random.choice(insult_list)
    return insult


def balance_insult_giver_sugar_daddy():
    insult_list =["Look at you, absolute sugar daddy material. The dealers are putting on extra perfume for you.",
                  "Yeah, yeah, lots of cash. But imagine how much bigger it would look if you risked it all on the next bet.",
                  "You've won enough to fund a premium mid-life crisis. Go wild.",
                  "Careful, with that much cash you might accidentally start looking like a functional member of society."
                  ]
    
    insult = random.choice(insult_list)
    return insult



def daily_insult_giver_standard():
    insult_list =["Here is your basic daily allowance. Don't spend it all in one place, peasant.",
                  "Just the regular amount for a regular user. Nothing fancy.",
                  "Your daily crumbs have been delivered. Enjoy being slightly less broke."]
    
    insult = random.choice(insult_list)
    return insult


def daily_insult_giver_loss():
    insult_list =["Unlucky! You tripped on your way to the bank and dropped your daily reward down a sewer.",
                  "The server tax collected your daily payment instead. Imagine being this broke.",
                  "You tried to claim your daily pay, but the wallet system went bankrupt. You actually lost cash."]
    
    insult = random.choice(insult_list)
    return insult


def daily_insult_giver_jackpot():
    insult_list =["HOLY COW! You actually hit the jackpot! The casino admins are crying right now.",
                  "Are you hacking? You just won the daily jackpot! Go buy something ridiculous.",
                  "The universe miscalculated and gave you the jackpot. Enjoy it before we patch it."]
    
    insult = random.choice(insult_list)
    return insult


## TITLE GIVERS
def daily_title_giver_standard():
    title_list =["The Usual Crumbs",
                 "Bare Minimum Achieved",
                 "Mediocre Payday",
                 "Just Another Day, Just Another Dollar",
                 "Slightly Less Broke Now"]
    
    title = random.choice(title_list)
    return title


def daily_title_giver_jackpot():
    title_list =["🎰 ABSOLUTE JACKPOT! 🎰",
                 "RNJesus Has Blessed You 🙏",
                 "Sugar Daddy Status Unlocked 🤑",
                 "Bro Is Actually Rich Now",
                 "Stop Hacking The Bot! 🛑",
                 "Infinite Wealth Glitch",
                 "We Are Bankrupt 💸",]
    
    title = random.choice(title_list)
    return title


def daily_title_giver_loss():
    title_list =["Skill Issue 💀",
                 "L + Ratio + Broke 📉",
                 "F In The Chat",
                 "Robbed By The Tax System 💸",
                 "Tax Evader Caught 👮"]
    
    title = random.choice(title_list)
    return title