# it allow us to use different class if there have a common value.
class tolu:
    def employee(self):
        print("come here")


class bolu(tolu):
     def employee(self):
        print("come here")


class dolu(tolu):
     def employee(self):
        print("come here")



Tolu = tolu()
Bolu = bolu()
Dolu =  dolu()


Tolu.employee()
Bolu.employee()
Dolu.employee()
