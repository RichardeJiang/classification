class Employee:
	empCount = 0

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayEmp(self):
		print "Name: " + self.name
		print "Name: ",self.name

	def displayCount(self):
		print "Number: " % Employee.empCount


emp1 = Employee("A",2000)
emp2 = Employee("b", 30)
emp1.displayEmp()
emp2.displayEmp()
print "Total num:" % Employee.empCount