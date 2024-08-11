mylist = ["cat", 1, 3]

for index, item in enumerate(mylist):
    row = f"{index+1}-{item}"
    print(row)
print("Length is", index+1)

#By using fstring
print(f"Length is {index+1}")

#By using len() function
print(len(mylist))

print("\n------------------------------------------------------------------------\n\n")
# Strings can be also used in enumerate functions
for i, j in enumerate("Hello"):
    print(i, j)

