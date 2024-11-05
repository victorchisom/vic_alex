# class chisom ():
#     def setage(self,number):
#         self.age = number 


#     def getage(self):
#         return self.age
    

# t=chisom()
# t.setage(45)
# print(t.getage())

# t.setage("thirty two")
# print(t.getage())


class chisom(object):
    def setage(self, number):
        if isinstance(number,(int,float)):
            self.age = number
        else:
            raise ValueError ('Age must be a number')
        
    def getage(self):
        return self.age
    

divine = chisom()

divine.setage(11)
print(divine.getage())




        