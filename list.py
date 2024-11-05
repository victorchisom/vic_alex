cars=['toyota','audie','nissan']
# print(cars[0])
# print(len(cars))
# for x in cars:
#     print(x)
    
# print ("<br>")
# cars.append('lambo')
# for x in cars:
#     print(x)
# print ("<br>")

# cars.pop(0)
# for x in cars:
    # print(x)



cars=['toyota','audie','nissan']
# print(cars[1])
cars[2]='camery'
print(cars)
cars.append("van")
print(cars)
cars.insert(2, "google")
print(cars)
cars.extend([344,6655])
print(cars)

cars.pop(0)
print(cars)

my_list = [1,2,3,4,5,6,7,8,9,1,1]
print(my_list)

my_list.pop(0)
print(my_list)

slice_list = my_list[0:6]
print(slice_list)