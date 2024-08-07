a = input("Enter some input : ")
# input function always gets a string type value

print(3*a)
print(3*int(a))
print()

#List indexing
mylist = ['a', 'b', 'c']
mylist.__setitem__(0,'d')
print(mylist)
print(mylist.__getitem__(2))