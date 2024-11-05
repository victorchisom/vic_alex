# you are banding data and methods within a class 
class person:
    def __init__(self, name, age):
            self.name = name
            self._age = age

    def person_details(self):
          print(f"Name:{self.name}, Age:{self._age}")

x = person('Ade', 28) 
print(x.person_details())


# name=("john")
# print(type(name))
# age=25
# print (f"hello,{name}!your are {age} years")


# name="""loremuieie
# iuuuiigiui
# gigigigi"""
# print(name)

# x="welcome"
# print(len(x))

# x=["bmw","volvo","toyota"]
# x.append("honda")
# print(x)

# x=["bmw","volvo","toyota"]
# x.pop(1)
# print(x)

# x=["bmw","volvo","toyota"]
# x.reverse()
# print(x)

# class vivi():
#     pass


# class employee():
#     def __init__(self, age):
#         self.age=("emloyee age is 44")

# def emloyeeID():
#     print("this is just an imployee unic id")
    