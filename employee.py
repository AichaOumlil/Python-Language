class employee :
    def __init__(self,name , age , gender,salary):
        self.name =name 
        self.age = age
        self.gender = gender
        self.salary = salary
    def totalsalary(self,target):
        totalsalary = self.salary + target
        print (f"The total salary is : {totalsalary}")
        print("\n")

    def printall(self) : 
        print (f"The name  is : {self.name}")
        print (f"The age = {self.age}")
        print (f"The gender is : {self.gender}")
        print (f"The salary is : {self.salary}")

em1 = employee("Nisma",17,"female",100000)
em1.printall()
em1.totalsalary(1000)

em2 = employee("Ali",25,"male",2000000)
em2.printall()
em2.totalsalary(20000)