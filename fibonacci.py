#fibonacci sequence generation: 0, 1, 1, 2, 3, 5, 8...

#provision to input the number for the desired starting point
a=int(input("Enter a starting point for your fibonacci sequence, either 0 or 1:"))

#provision to input the number of numbers to be generated in the sequence
b=int(input("Enter number of numbers to be generated in the sequence: "))

#intializing a list container with seeded number to collect numbers generated
f_seq=[a]

#setting a reference for the calculation of the fibonacci number
A=0
#setting reference to 1 regardless of the seeded number being 1 or 0, and adding it to the list container
if f_seq[0]==0 or f_seq[0]==1:
        A=A+1
        f_seq.append(A)
i=1 #initializing the index, i, for the while loop
while i<b:
     #setting the addition sequence in fibonacci   
    B=f_seq[i]+f_seq[i-1]
    #adding it to the list container
    f_seq.append(B)
    #increment of the index required of the while loop
    i=i+1
#outputing the sequence generated
print(f_seq)       
    

