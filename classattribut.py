class employee():
    percentage=5
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def raise_salary(self):
        amount=(self.salary*employee.percentage)/100
        self.salary+=amount
        return self.salary
    
chalo= employee("chalo",24000)
print(chalo.name,chalo.salary)


chalo.raise_salary()
print(chalo.name,chalo.salary)


employee.percentage=50
chalo.raise_salary()
print(chalo.name,chalo.salary)


# employee.percentage =10
# chalo.raise_salary()
# print(chalo.name,chalo.salary)


# employee2 = employee('mary', 50000)
# print(employee2.name,employee2.salary)


# employee.percentage= 25
# employee2.raise_salary()
# print(employee2.name,employee2.salary)

