class BookDAO:         
    def getAll(self):
        #TODO implement
        return [{"id":1,"title":"The Da Vinci Code","author":"Dan Brown","price":10.99}]
    def findByID(self, id):
        return {"id":2,"title":"The Twilight Saga","author":"Stephenie Meyer","price":9.99}
    def create(self, book):
        return {"id":3,"title":"blah","author":"someone","price":999}
    def update(self,id , book):
        return {"id":4,"title":"Gone with the Wind","author":"Margaret Mitchell","price":7.99}
    def delete(self, id):
        return True
        
bookDAO = BookDAO()

if __name__ == "__main__":
    book = {"id":1,"title":"blah","author":"someone","price":999} 
    print ("test getall")
    print (f"\t{bookDAO.getAll()}")
    print ("test findById(1)")
    print (f"\t{bookDAO.findByID(1)}")
    print ("test create")
    print (f"\t{bookDAO.create(book)}")
    print ("test update")
    print (f"\t{bookDAO.update(1,book)}")
    print ("test delete")
    print (f"\t{bookDAO.delete(1)}")
   