#Read comma seperated integers
numbers=input("Enter comma-sepated numbers: ")

number_list=numbers.split(",")

number_tuple=tuple(number_list)

print("List: ",number_list)
print("Tuple: ",number_tuple)
