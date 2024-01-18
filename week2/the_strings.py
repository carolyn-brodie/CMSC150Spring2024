## Strings are immutable
## this is a method for echanging strings

my_string = "ABC"
print(my_string[1])
my_string= my_string[0] + "Z" + my_string[2]
print(my_string)