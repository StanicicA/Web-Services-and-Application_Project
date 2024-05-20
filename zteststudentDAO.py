from zstudentDAO import studentDAO


student = {
  "name":"mark", 
  "age":31
  }

student = studentDAO.create(student)
studentid = student["id"]

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