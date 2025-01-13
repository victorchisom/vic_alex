import random
a=1
b=10
random_number=random.randint(a,b)
print(random_number)
random_float=random.uniform(a,b)
print(random_float)


seq=[1,2,3,4,5]
random.shuffle(seq)
print(seq)

element=random.choice(seq)
print(element)
k=2
elements=random.sample(seq,k)
print(elements)
