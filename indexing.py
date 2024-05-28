mylist=[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list=[]
for i in range(10) :
    if i in mylist:
        unique_list.append(i)
print(f"The list with unique elements only is: {unique_list}")
print(mylist)