from art import logo

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")

print(logo)
bidders = {}
auction_ongoing = True
while auction_ongoing:
    name = input("What is you name?: ")
    bid = int(input("What's your bid?: $ "))
    bidders[name] = bid

    more_bidders = input("Are there any more bidders? Type 'yes' or 'no'.").lower()
    if more_bidders == "yes":
        print("\n" *  20)
    else:
        auction_ongoing = False
        find_highest_bidder(bidders)