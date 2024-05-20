from flask import Flask, url_for, request, redirect, abort, jsonify
from BookDao import bookDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"
@app.route('/books')
def getAll():
    return jsonify(bookDao.getAll())
@app.route('/books/<int:ISBN>')
def findById(ISBN):
    return jsonify(bookDao.findById(ISBN))
@app.route('/books', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)

    book = {
        "ISBN": request.json["ISBN"],
        "title": request.json["title"],
        "author": request.json["author"],
        "price": request.json["price"]
    }
    return jsonify(bookDao.create(book))
@app.route('/books/<int:ISBN>', methods=['PUT'])
def update(ISBN):
    foundBook=bookDao.findById(ISBN)
    print (foundBook)
    if foundBook == {}:
        return jsonify({}), 404
    currentBook = foundBook
    if 'title' in request.json:
        currentBook['title'] = request.json['title']
    if 'author' in request.json:
        currentBook['author'] = request.json['author']
    if 'price' in request.json:
        currentBook['price'] = request.json['price']
    bookDao.update(currentBook)

    return jsonify(currentBook)
@app.route('/books/<int:ISBN>', methods=['DELETE'])
def delete(ISBN):
    bookDao.delete(ISBN)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)