logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
'''
print(logo)
print("\n***************** WELCOME TO SECRET AUCTION *****************\n")
should_continue = True
clients = {}
list_value = []

while should_continue:
    name = input("What is your name : ")
    bid = int(input("what's your bid? : Rs."))
    clients[name] = bid
    list_value.append(bid)
    restart = input("Are there any other bidders? Type 'yes' or 'no' : \n")
    if restart == "no":
        should_continue = False
        win = max(list_value)
        for key, value in clients.items():
            if win == value:
                print(f"The Winner is {key} with a bid of {win}")
                print(f" ************* Congratulations {key}! *************")
    else:
        print("\n"*100)
