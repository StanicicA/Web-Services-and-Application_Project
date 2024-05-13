from flask import Flask, url_for, request, redirect, abort
app = Flask(__name__, static_url_path='', static_folder='staticpages')
@app.route('/')
def index():
 return "hello"
if __name__ == "__main__":
  app.run(debug=True)

#Modifyng the Flask Server to deal with the required URL mappings (the functions can be
#just skeletons at this stage)
#10. Creating a mapping and function for each of the possible API calls

@app.route('/books', methods=['GET'])
def getall():
 return "get all"
@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
 return "find by id"
#creating
@app.route('/books', methods=['POST'])
def create():
# reading json from the body
 jsonstring = request.json
 return f"create {jsonstring}"
# updating
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
 jsonstring = request.json
 return f"update {id} {jsonstring}"
#deleting
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
 return f"delete {id}"

#Testing everything using CURL test at each of mine endpoints

# getall
# curl http://127.0.0.1:5000/books
# find by id
# curl http://127.0.0.1:5000/books/1
#create
#curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books
# update
# curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books/1
#delete
# curl -X DELETE http://127.0.0.1:5000/books/1

#Future: create the DAO 12. Create another file for interacting with the database, 
#mine is for books so is called bookdao.py

# returns all the books in the database table
def getall():
 return [{}]
# returns one book
def findById(id):
 return {}
# inserts a book into the database
def create(book):
 return book
# updates the book
def update(id, book):
 return book
# deletes the book with the id
def delete(id):
 return True