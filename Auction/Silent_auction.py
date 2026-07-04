from logo_bid import logo
auction={}
print(logo, "\nWelcome to the silent auction program.")
conti = "y"
while conti == "y":
    bidder = input("Enter the name of bidder: ")
    bid = int(input("Enter the bid amount: $"))
    auction[bidder] = bid
    print("\n" * 30)
    conti = input("Are there more bids? y/n : ").lower()

highest_bidder = max(auction, key=auction.get)
highest_bid = auction[highest_bidder]
print(f"{highest_bidder} with the bid of ${highest_bid} has won the auction!!")
