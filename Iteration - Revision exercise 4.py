#Adam Howe
#Iteration - Revision exercise 4
#16/10/2014


number = int(input("Enter a number between 10 and 20: "))

while not 10 <= number <= 20:  
    number = int(input("The number is outside the range, enter another one: "))
    if 10<= number <= 20:
        print("The number is within range")

    
