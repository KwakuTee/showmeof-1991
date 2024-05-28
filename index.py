#given list
mylist=[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#creating an empty list
unique_list=[]
#using the for loop to find the number in the range of numbers in the given list
for i in range(10) :
    #finding which of the item of the range is in the list
    if i in mylist:
        #adding the identified item into the created list
        unique_list.append(i)
print(f"The list with unique elements only is: {unique_list}")
print(mylist)