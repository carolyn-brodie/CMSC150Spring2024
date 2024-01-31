myList = ["apples", "oranges", 2]
print(myList)

print(myList[1])
#
if myList[1] == "apples":
    print("It is apples")
#
newList = [myList[1], 2, "hi",5, "hi"]
newList.remove("hi")
print(newList)


# print (newList[3][1])
# print(len(newList))
# myString = "Abc"
# myString[1] = "z"
# newList[3] = 10
# print(newList)
# newList.append(100)
# print(newList)


# ## Break string apart
# print(list("hi there"))
#
# ##join list
# lst1 = ["a","b","c"]
# separator = ""
# out = separator.join(lst1)
# print(out)