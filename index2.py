#given set
mylist=[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

#creating an empty list
unique_list=[]

#using for loop to iterate over each element in the given list
for i in mylist:
    #if elememt already in the empty list created it should not be added
    if i in unique_list:
        continue
    #if above condition is satisfied, the element should is not added to the unique_list
    unique_list.append(i)
print(mylist)    
print("The list of unique elements is",unique_list)