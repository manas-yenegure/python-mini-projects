def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder, bid_amount in bidding_dictionary.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The Winner is {winner} with a bid of ${highest_bid}.")


bids = {}

while True:
    name = input("What is your name?: ").strip()
    price = int(input("What is your bid?: $"))

    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
    if should_continue == "no":
        break

find_highest_bidder(bids)