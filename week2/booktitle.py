instructions =  """
Write a program that will ask the user to input a book title, and the author’s

full name. Then print out the book’s title, and author’s name, making 

sure there are no spaces at the start or end of the title/author and making 

sure that the first letter of each word in the title is capitalized, as well as 

capitalizing the author’s names.
"""

bookTitle = input("Input your book title:")
authorName = input("Input the authors full name:")

bookTitle = bookTitle.strip()
bookTitle = bookTitle.title()
authorName = authorName.strip()
authorName = authorName.title()

print("The book title is",bookTitle)
print("The authors name is",authorName)
