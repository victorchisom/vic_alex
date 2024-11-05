dict1 = {
    "name":"chisom",
    "age":45,
    "class": 32,
    'email': 'John',
    'address': ['Ketu', 'Ikeja', 'Ikorodu']
}
print(type(dict1))

dict2 = dict(
    name ="chisom",
    age = 45,
    class1 =  32,
    email= 'John',
    address= ['Ketu', 'Ikeja', 'Ikorodu']
)
dict2['email']='bag@gmail.com'
print(dict2)

dict2['phone']="0886353761"
print(dict2)

del dict2["phone"]
print(dict2)



for name, chisom in dict2.items():
    print(name, chisom)