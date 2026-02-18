from blind_auction_logo import logo
print(logo)
print("Welcome to the secret aution program")


name = input("What is your name? : ")
bid = int(input("What's your bid?: "))
bidding_data = {}

def bidding(name_of_bidder, placed_bid):
  bidding_data[name_of_bidder] = placed_bid

  continuation = input("Are there any other bidders, Type 'yes' or 'no'").lower()
  if continuation == "yes":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    name = input("What is your name? : ")
    bid = int(input("What's your bid?: "))
    bidding(name_of_bidder= name, placed_bid= bid)
  else:
    bids = 0
    winner = " "
    for bidders in bidding_data:
      if int(bidding_data[bidders]) > bids:
        bids = bidding_data[bidders]
        winner = bidders
    print(f"The winner is {winner} is  with a bid of ${bids} ")
    print(bidding_data)

bidding(name_of_bidder= name, placed_bid= bid)

