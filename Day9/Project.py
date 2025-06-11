import os
# Bidder
print("""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\      
""")

answer = 'yes'
bids = {}
while answer == 'yes':
   name = input('What is your name?: ')
   bid = int(input ('What is your bid?: $'))
   bids[name] = bid
   answer = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
   os.system("clear")


   
winner = { "name": "", "bid": 0}
for key in bids:
   if bids[key] > winner["bid"]:
      winner["name"] = key
      winner["bid"] = bids[key]
   
print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")