def yearOfBirth(name,age):
    year = 2023 - age
    print(f"hello {name},you were born in {year}")

def myCountry(country=" Kenya"):
    print(f"Hello you are from {country}")


# a function that accept any number of argument

# define a function which has only one parameter but we add a star 
# before the parameter name
def hello(*names):
    for name in names:
        print(f"hello {name}")

def add(*nums):
    answer = 0
    for num in nums:
        answer +=num 
    return answer

# we add ** for keyword arguments

def mult(**kwargs):
    answer =1
    for nums in kwargs.values():
        answer*=nums
    return answer

# A function named concatenate_args that takes 
# any number of string arguments in positional arguments 
# format and concatenates them into a single string

def concatenate_args(*name):
    concatenated=[]
    for n in name:
        concatenated.extend(n)
    return' '.join(concatenated)

# A function named concatenate_kwargs
#  that takes any number of string arguments 
# in keyword arguments  format and concatenates them into a single string

def concatenate_kwargs(**kwargs):
    name =''
    for n in kwargs.values():
        name+=n
    return name
    