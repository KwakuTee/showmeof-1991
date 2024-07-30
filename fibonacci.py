#fibonacci sequence: 0, 1, 1, 2, 3, 5, 8...
a=int(input("Enter a starting point for your fibonacci sequence, either 0 or 1:"))
b=int(input("Enter number of numbers to be generated in the sequence: "))

f_seq=[a]
A=0

if f_seq[0]==0 or f_seq[0]==1:
        A=A+1
        f_seq.append(A)
i=1
while i<b:
    B=f_seq[i]+f_seq[i-1]
    
    f_seq.append(B)
    
    i=i+1

print(f_seq)       
    

