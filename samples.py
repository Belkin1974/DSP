list1=[1,3,5,6,7,9,33]
list3=[1,6,11,33]
list2=filter(lambda y: y in list1, list3)
print(list(list2))