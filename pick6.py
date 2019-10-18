from random import randint

payouts = [0, 4, 7, 5E4, 1E6, 25E7]
    
def six_picks():
    return [randint(1, 99) for i in range(6)]
  
def matches(winner, ticket):
    matches = 0
    for i in range(len(ticket)):
        if ticket[i] == winner[i]:
            matches += 1
    return matches
        
def main():
    MAX_ITER = int(1E5)
    balance = 0
    expenses = 0
    winner = pick_six()


    for i in range(MAX_ITER):
        expenses += 2
        matches = compare_matches(winner, pick_six())
        balance += payouts[matches]

    print(f'\n Balance: {balance}\n Expenses: {expenses} \n ROI: {(balance - expenses) / expenses}\n')

main()