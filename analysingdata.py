from API_Interaction import readAllBooks

books = readAllBooks()
total = 0
count = 0
for book in books:
    total += book["price"]
    count += 1

print ("average of ", count, "books is ", total/count )