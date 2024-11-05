# parent class
class Person:
     def __init__(self, first_name, last_name):
      self.first_name= first_name
      self.last_name = last_name

     def full_name(self):
        return f"{self.first_name}, {self.last_name}"
      

    

    # child class
class Employee(Person):
    def __init__(self, first_name,last_name,employee_id):
        super().__init__(first_name,last_name)  #inherit from parent class
        self.employee_id= employee_id



    def employee_details(self):
                return f"Name: {self.full_name()} ID:{self.employee_id}"
            
        # create instance of the class
person = Person("Ade", "Ogu")
emp = Employee("Gift", "Mark", 1)
print(person.full_name())
print(emp.employee_details())