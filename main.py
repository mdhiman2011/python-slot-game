import random

# Min bets a player can put
MIN_BET=5 
# MAx bets a player can put
MAX_BET=50
#MAx Line Player can choose that decides the occurence of selected character for Win
MAX_LINES=5

#defining rows and cols to create the combination of matrix. Keep usually the SLOT ROws and MAX Lines Same
SLOT_ROWS=5
SLOT_COLS=3

#symbols used to create matrix
symbol_list={
    "P" : 2,
    "Q" : 4,
    "R" : 6
}

# count(times) for each symbol which decided the win
win_list={
    "P" : 8,
    "Q" : 5,
    "R" : 2
}

# def to ask for the amount to deposit to start play
def deposit_amount():
    while True:
        deposit_amt=input("What amount would you like to deposit? $")
        if (deposit_amt.isdigit()):
            deposit_amt=int(deposit_amt)
            if(deposit_amt>0):
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number for Deposit.")

    return deposit_amt

# def to get the number of lines player has to choose
def get_no_of_lines():
    while True:
        lines=input(f"Enter the number of line to bet on ranges between 1 - {MAX_LINES} ? ")
        if lines.isdigit():
            lines=int(lines)
            if(1 <= lines <= MAX_LINES):
                break
            else:
                print(f"You can put the bet line between 1 - {MAX_BET}.")   
        else:
            print("Please enter a number for bet line.")

    return lines

# def to get the bet amount of each line selected
def get_bet_amt():
    while True:
        bet_amount=input("What amount you want to bet on each line? $")
        if (bet_amount.isdigit()):
            bet_amount=int(bet_amount)
            if(MIN_BET<= bet_amount <=MAX_BET):
                break
            else:
                print(f"You can bet an amount between {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number for bet amount.")

    return bet_amount


#def to create a nested List to with the symbols mentioned  in symbol list defined above 
def get_slot_machine_list(rows,cols,symbols):
    symbols_all=[]
    for symbol,symbol_count in symbols.items():
            for i in range(symbol_count):
                  symbols_all.append(symbol)
    # print(symbols_all)

    # for _ in range(rows):
    #     column_symbols=symbols_all[:]
    #     choiceval=random.choice(column_symbols)
    #     print(choiceval)
    #     column_symbols.remove(choiceval)
    #     print(column_symbols)
    

    columns=[]
    for _ in range(rows):
          column=[]
          column_symbols=symbols_all[:]
          for _ in range(cols):
                choiceval=random.choice(column_symbols)
                column_symbols.remove(choiceval)
                column.append(choiceval)
                # print(column) 
          columns.append(column)     
    
    return(columns)

# def just to print the created nested list in fine way
def nice_print_slot_result(slot):
      if len(slot)>0:
       for row,data_row in enumerate(slot):
            for i in range(len(data_row)):
                # print(len(data_row))
                if i==len(data_row)-1:
                    print(data_row[i] ,end=" ")
                else:   
                    print(data_row[i], end=" | ")
            print()        

# def which calculate the no of occurences of selected character in the randomly created nested list                    
def winning_game(slots_list_v,lines,entered_symbol):
    winnings_count=0
    for line in range(lines):
        rows_to_check=slots_list_v[line]
        # print(rows_to_check)
        # print(len(rows_to_check))
        for i in range(len(rows_to_check)):
            checking_symbol=rows_to_check[i]
            # print(checking_symbol)
            if entered_symbol ==checking_symbol:
                winnings_count+=1
            else: 
                pass
            i+=i
    return winnings_count

# running the games until the player didn't quit
def game_run(deposited_amount):
    user_entered_bet_symbol=input("Please enter a symbol between P, Q and R for bet: ")
    bet_lines=get_no_of_lines()
    while True:
        bet_amount=get_bet_amt()
        total_bet_amount= bet_lines * bet_amount
        if(total_bet_amount>deposited_amount):
            print(f"Your total bet amount ({total_bet_amount}) exceeds the deposited amount ({deposited_amount})")
        else:
            break    

    print(f"You are betting on lines {bet_lines} with bet amount on each line as {bet_amount}. Total bet_amount is: {total_bet_amount}") 
    
    slot_list=get_slot_machine_list(SLOT_ROWS,SLOT_COLS,symbol_list)  
    # print(slot_list)
    nice_print_slot_result(slot_list)
    
    total_win_count=winning_game(slot_list,bet_lines,user_entered_bet_symbol)
    print(total_win_count)
    total_win=(total_win_count*win_list[user_entered_bet_symbol])*bet_amount
    if(total_win>0):
        print(f"Your Won!. Your Total Win is :{total_win}")
        remaining_balance=(deposited_amount-total_bet_amount)+total_win
    else:
        print("You Loose :)")
        remaining_balance=(deposited_amount-total_bet_amount)    
    return remaining_balance

                


#main def
def main():
    # slot_list=[['R', 'Q', 'R'], ['R', 'B', 'Q'], ['P', 'P', 'Q'], ['Q', 'R', 'Q'], ['R', 'Q', 'Q']]  
    # bet_line=2
    # bet_amount=10
    # win_list_values=win_list
    # user_entered_bet_symbol="Q"
    dep_amount=deposit_amount()
    while True:
        print(f"Your Total Deposited Balance is ${dep_amount}")
        game_play_flag=input("Please Press Enter to Play (q for Quit!): ")
        if game_play_flag=="q":
            break
        else:
            dep_amount=game_run(dep_amount)
    
# Calling of the main
main()   