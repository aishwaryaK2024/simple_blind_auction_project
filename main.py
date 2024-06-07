from art import logo
print(logo)
bid_is_on = True
dic = {}
while (bid_is_on):
    name = input("What is your name?: ")
    bid = int(input("What is your bid : $"))
    bidders = input("Are there any other bidders? Type Yes or No ")
    dic[name] = bid
    if bidders == "no":
        bid_is_on = False
    elif bidders == "yes":
        bid_is_on = True

high_bid = 0
for name in dic:
    if dic[name] > high_bid:
        high_bid = dic[name]
        winner = name
print(f"The Winner is {winner} with a bid of ${high_bid}")
