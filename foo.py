pages = int(input("pages?"))
if(pages < 100):
    print("This book is a short book.")
elif(pages < 300):
    print("This book is an average book.")
else:
    print("This book is a long book.")   