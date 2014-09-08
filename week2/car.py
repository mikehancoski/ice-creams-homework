instructions = """ 
Write a program that will ask the user to input a book title, and the author’s

full name. Then print out the book’s title, and author’s name, making 

sure there are no spaces at the start or end of the title/author and making 

sure that the first letter of each word in the title is capitalized, as well as 

capitalizing the author’s names.
"""
carPrice = float(input("Input he car price:"))
tax = .08
license = .02
dealerPrep = 200
destCharge = 300

carPrice = carPrice + (carPrice * tax) + (carPrice * license) + dealerPrep + destCharge

print("the cars price is:", carPrice)
