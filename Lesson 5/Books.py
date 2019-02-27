import json

book1 = dict(title = "Learning Python", author = "Mark Lutz", PubDate = 2013 )
book2 = dict(title = "As I Lay Dying", author = "William Faulkner", PubDate = 930 )

tempTitle = input("Enter Title: ")
tempAuthor = input("Enter author: ")
tempPubDate = int(input("Enter Publication Year: "))

books = [book1, book2]

book3 = dict(title = tempTitle, author = tempAuthor, PubDate = tempPubDate )
books.append(book3)

json.dump(books, fp=open('myFile.txt','w'), indent=4)

newBook = json.load(open('myFile.txt'))
print(newBook)
print(len(newBook))

for book in newBook:
    print(book["title"])