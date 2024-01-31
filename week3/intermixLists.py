##intermix two lists

list1 = [0,5,8,9]
list2 = [1,3,9,12]

mixedList = []
for index in range(len(list1)):
    if list1[index] < list2[index]:
        mixedList.append(list1[index])
        # list1.remove(list1[index])
    else:
        mixedList.append(list2[index])
        # list2.remove(list2[index])

print(mixedList)

##What happens if the lists are not the same length?  Let's fix it so it works then

 
