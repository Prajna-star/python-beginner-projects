bid_dict = {}
def entry():
    name = input("What is your name? ")
    bid = float(input("Your bid amount: $"))
    bid_dict[name] = bid
    new_entry = input("Is there anybody else to enter the bid? 'y' for Yes and 'n' for No \n").lower()
    if new_entry == 'y':
        print('\n' *100)
        entry()
    elif new_entry == 'n':
        print('\n' *100)
        key = ''
        value = 0
        for entry1 in bid_dict:
            if bid_dict[entry1] > value:
                key = entry1
                value = bid_dict[entry1]
        print(f'The winner is {key} with the bid {value}!')
entry()