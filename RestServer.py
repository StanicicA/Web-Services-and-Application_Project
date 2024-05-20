from flask import Flask, url_for, request, redirect, abort
app = Flask(__name__, static_url_path='', static_folder='staticpages')
@app.route('/')
def index():
 return "hello"
if __name__ == "__main__":
  app.run(debug=True)
@app.route('/books', methods=['GET'])
def getall():
 return "get all"
@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
 return "find by id"

@app.route('/books', methods=['POST'])
def create():
 jsonstring = request.json
 return f"create {jsonstring}"
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
 jsonstring = request.json
 return f"update {id} {jsonstring}"
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
 return f"delete {id}"

def getall():
 return [{}]
# returning one book
def findById(id):
 return {}
#creating a book into the database
def create(book):
 return book
# updating the book
def update(id, book):
 return book
# deleting the book with the id
def delete(id):
 return True