class BookDAO:         
    def getAll(self):
        #TODO implement
        return [{"id":1,"title":"blah","author":"someone","price":999}]
    def findByID(self, id):
        return {"id":1,"title":"blah","author":"someone","price":999}
    def create(self, book):
        return {"id":1,"title":"blah","author":"someone","price":999}
    def update(self,id , book):
        return {"id":1,"title":"blah","author":"someone","price":999}
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
   