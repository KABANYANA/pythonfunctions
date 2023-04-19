# if statement 
# checks if an expression is true or false. we use it in combination with comparison operators

def evenNumbers():
    x=range(10)
    for i in x:
        if i%2==0:
            print(i)

def oddNumbers():
    y=range(20)
    for i in y:
        if i%2!=0:
            print(i)

# the if statement can optionally be combined with an else statement. 
# The code inside else will be executed if the precending if statement returns false



def divisible_by_five():
    x=range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by 5")
        else:
            print(f"{i} is not divisible by 5")



# ELIF STATEMENT
# Allows more than one comparison in the flow

def multiple_comparison():
    x= range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by 5")
        elif i%7==0:
            print(f"{i} is divisible by 7")
        elif i%9==0:
            print(f"{i} is divisible by 9")
        else:
            print(f"{i} is not divisible by 5,7 and 9") 

# LOGICAL OPERATORS
# AND,OR NOT

def odd_or_even():
    x= range(20)
    for i in x:
        if i%2==0 and i%3==0:
            print(f"{i} is divisible by both 2 and 3")
        elif  i%2==0 or i%3==0:
            print(f"{i} is divisible by either 2 or 3")
        else:
            print(f"{i} is not divisible by either 2 or 3")


# WHILE LOOP 
# continues running as ling as the set condition

def while_loop():
    x=1
    while x<10:
        print("Hello")
        x+=1

# BREAK STATEMENT
# stops a while loop even is the set condition is true

def break_statement():
    x=1
    while x<10:
        print("Hello")
        x+=1
        if x==5:
            break
        

# CONTINUE STATEMENT
# skips the remainder of the current iteration and goes to the next iteration
        

def continue_statement():
    x=0
    while x<=20:
        x+=1
        if x%3==0:
            continue
        print(x)



                        # ASSIGNMENT 

# Write a function that uses while, if and
#  continue statements to print all the even numbers between 0 and 50. 

def continue_while():
    x=1
    while x<50:
        if x%2!=0:
            x+=1
            continue
        
        print(x)
        x+=1

# Write a function that takes an integer argument
#  and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.

def prime(number):
    if number<=1:
        print(f"{number} is Not prime")
    elif number>1:
        for i in range(2,number):
            if(number%i==0):
                print(f"{number} is Not Prime")
                break
        else:
            print(f"{number} is Prime")




# Write a function that takes a list of integers as
#  input and prints the sum of all the even numbers in the list.

def int_list(numbers):
    total =0
    for i in numbers:
        if i%2==0:
            total+=i
        
    print(total)




# Write a function that takes any two integers
#  as input, and prints the sum of all the numbers 
# between the two integers (inclusive) that are divisible by 3.

def sum_in_range(num1,num2):
    total=0
    for n in range(num1,num2+1):
        if n %3==0:
            total+=n
    print(total)