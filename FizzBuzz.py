'''Writing a program that prints the numbers from 1 to 50. But for multiple of three print "Fizz"
    instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz"
'''

for i in range(1, 51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
        continue
    elif i%3==0:
        print("Fizz")
        continue
    elif i%5==0:
        print("Buzz")
        continue
    else:
        print(i)

