# Arithmetic Operation
# Operator "+" <- Addition
def addition(x,y):
    return x+y
print(addition(2,2)) #Output = 4

# Operator "-" <- Subtraction
def subtraction(x,y):
    return x-y
print(subtraction(3,2)) #Output 1

# Operator "*" <- Multiplication
def multiplicatin(x,y):
    return x*y
print(multiplicatin(2,4)) #Output 8

# Operator "/" <- Division 
def division(x,y):
    return x/y
print(division(6,3)) #Output 2.0

# Operator "%" <- Modulus
# give the remainder of two division numbers
def modulus(x,y):
    return x%y
print(modulus(17,3)) #Output 2

# Operator "//" <- Quotient(Floor Division)
# rounded down into nearest lower integer number

# so 1.5 will be 1
#    2.5 will be 2
# because <- lowest 1,2,3,4,5 highest -> 

# so -1.5 will be -2
#    -2.5 will be -3
# because <-lowest -5,-4,-3,-2,-1  highest ->

def floorDivision(x,y):
    return x//y
print(floorDivision(7,3))


# Operator "**" <- Exponentitation 
# same as math module pow(2,3)
# first int power second int 
def exponentitation(x,y):
    return x**y
print(exponentitation(2,3))


# Memory address 
a = 5
b = 5
# will same memory address because 5 take in the memory
# and variable a and b use same value of memory address 
print(id(a))
print(id(b))

L1 = [1,2,3,4]
L2 = [1,2,3,4]
print(id(L1) == id(L2))   # False

L3 = L1.copy()
print(id(L1) == id(L3))   # True 

L4 = L1
print(id(L1) == id(L4))   # False

L5 = L1[:]
print(id(L1) == id(L5))   # False

import copy
L6 = copy.deepcopy(L1)
print(id(L1) == id(L6))   # False

# List 
# Difference between str and List is str object does not support item assignment, but List does
A = "hello"
A[0] = A[0].lower()
print(A)

L = ["H","E","L","L","O"]
L[0] = L[0].lower()
print(L)

Iterable items can be use loop their variable name 
1. Lists
2. Tuples
3. Strings
4. Dictionaries
5. Sets

# But String is iterable so we can use loop on string 
a = "HELLO"
for i in a:
    print()

Non-iterable are 
1. int
2. float
3. boolean



