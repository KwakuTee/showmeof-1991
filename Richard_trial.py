#initialize the count by setting count to 0
count=0

#provision to input your list
List_input=[]
i=0
while i<=5:
    a=int(input("enter a number: "))
    List_input.append(a)
    i=i+1

#for order in operation, the list has to be sorted in ascending order
List_sorted=sorted(List_input)

#initializing the index, i by setting it to the last index of the list
i=len(List_sorted)-1

#iterating over the items in the list as far as index, i, is less than the length of the list
while i<(len(List_sorted)):
    #if index, i, is negative, the loop should end
    if i==0:
        break
   #comparing numbers from the last item of the list
   #to the immediate number next to it and reducing it by 1 if they are equal 
    elif List_sorted[i]==List_sorted[i-1]:
        List_sorted[i-1]=List_sorted[i] - 1
        count=count+1
    #if the above condition is not satisfied, the count should remain the same
    else:
        count=count+0
    #in the while loop, after every iteration, the index, i, reduces by 1 until it turns 0
    i=i-1
#printing the results of the count
print(count)
#printing the results of the list after the operation
print(List_sorted)