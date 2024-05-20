#Getting data from URL/ all the books
from xml.dom.minidom import Identified
import requests
url = "https://andrewbeatty1.pythonanywhere.com/books"

#Converting that into a function:
def readAllBooks():
    response = requests.get(url)
#checking for correct response code
    return response.json()

 #Writing the function for find by id and testing it
def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
# we could do checking for correct response code
    return response.json()

def createbook(book):
    response = requests.post(url, json=book)
# checking the response
    return response.json()

def updatebook(id, bookdiff):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=bookdiff)
    return response.json()

def deletebook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

if __name__ == "__main__":
    #book = {
    #    'author':"Paulo Coelho",
     #   'title':"The Alchemist", 
      #  "price": 25.50
    #}
    book = {
        'author':"Paulo Coelho",
        'title':"Veronika Decides to Die", 
        "price": 26.50
    }
    bookdiff = {
        "price": 33.50
    }
    #print (readAllBooks())
    #print (getBookById(545))
    #print (deletebook(567))
    print (createbook(book))
    #print (updatebook(1,bookdiff))
