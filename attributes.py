class Person:
    def __init__(vic,age, name):
       vic.age = age
       vic.name = name

    def output(vic):
        print(f"age:{vic.age}, name :{vic.name}")



#object
g=Person(34, 'olu')

g.output()