#Student-class objects display using print(), using __str__() sp-method
#Student.py

class Student:
	def __init__(self,sno,sname,height):
		self.sno=sno;
		self.sname=sname;
		self.height=height;
	def __str__(self):
		ss=str(self.sno)+"\t"+self.sname+"\t"+str(self.height);
		return ss;
	
s1 = Student(1001,"Sai",6.2);
s2 = Student(1002,"Ram",5.9);
print(s1)
print(s2)
print(id(s1))
print(id(s2))
#s1.display()
#s2.display()