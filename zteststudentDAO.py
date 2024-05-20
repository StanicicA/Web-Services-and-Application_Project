from zstudentDAO import studentDAO


student2 = {
  "firstname":"mark", 
  "age":31
  }

student2 = studentDAO.create(student2)
studentid = student2["id"]

result = studentDAO.findByID(studentid);
print ("test create and find by id")
print (result)

newstudentvalues= {"name":"fred", "age":18}
studentDAO.update(studentid,newstudentvalues)
result = studentDAO.findByID(studentid);
print("test update")
print (result)

print("test get all")
allStudents = studentDAO.getAll()
for student in allStudents:
  print(student)

studentDAO.delete(studentid)