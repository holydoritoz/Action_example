from art import logo
import operator
from replit import clear

print(logo)
print('Welcome to the secret auction program.')
anotherUserFlag=True

while anotherUserFlag:
    userName=input('Whats your name?: ').lower()
    bidPrice=int(input('Whats your bid price?:$ '))
    bidList={}
            #key     #valor
    bidList[userName]=bidPrice

    anotherUser=input('If there another user who want to bid? Type "Yes" or "No": ').lower()
    if anotherUser != 'yes':
        anotherUserFlag=False
        for highestBid in bidList:
            highestBid=max(bidList.items(), key=operator.itemgetter(1))[0]
            print(f'The Winner of this Auction is {highestBid} with {bidList[highestBid]}')
    else:
        clear()
            


           


