def squareIt(number):
    return number ** 2

list_of_numbers = [1, 4, 5, 6, 10]

squared_list = []
for number in list_of_numbers:
    squared_list.append(number ** 2)

print(squared_list)

squared_list_lc = [squareIt(number) for number in list_of_numbers]
print(squared_list_lc)

def isGreater20(number):
    return number > 20

#
#
# total = sum([squareIt(num) for num in list_of_numbers if isGreater20(squareIt(x))])
# print(total)
#
# ## First Sum
# ## built in function to add all the numbers in a list
# print(sum([1, 2, 3]))
#
# #Square all the numbers in a list
# numbers_squared = [squareIt(x) for x in list_of_numbers]
# print(numbers_squared)
#
# # print([x ** 2 for x in list_of_numbers])
#
# ## filter
# filtered = [num for num in numbers_squared if isGreater20(num)]
# print(filtered)
#
# numbers_squared = [squareIt(x) for x in list_of_numbers]
# filtered = [num for num in numbers_squared if isGreater20(num)]
# total = sum(filtered)
# print("total is ", total)


def find_capitalized_indexes(word):
    capitalized_indexes = []
    for i in range(len(word)):
        if word[i].isupper():
            capitalized_indexes.append(i)
    return capitalized_indexes

word = "uPPerCase"

print([(index, char) for index, char in enumerate(word)])
# capital_indices = [index for index, char in enumerate(word) if char.isupper()]
# print(capital_indices)



