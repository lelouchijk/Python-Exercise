# function1 (1 point)
# ● The function name: function1
# ● This function takes two positional arguments
# ○ First argument: int type
# ○ Second argument: int type
# ● The return value: int type
# ○ The result of subtracting the second argument from the first argument
# ● This function will be tested with positional arguments, for example:
# ○ print(function1(1, 2)) # -1 (because 1-2 is -1)
# ○ print(function1(2, -1)) # 3 (because 2-(-1) is 3)
# ○ print(function1(-3, 4)) # -7 (because (-3)-4 is -7)
# ○ print(function1(-3, -4)) # 1 (because (-3)-(-4) is 1)

def function1(x : int,y : int)->int:
    return x-y

# function2 (1 point)
# ● The function name: function2
# ● This function takes two positional arguments
# ○ First argument: int type
# ○ Second argument: int type
# ● The return value: int type
# ○ The absolute value of the result of subtracting the second argument from the
# first argument (for example, |-1| = 1)
# ● This function will be tested with positional arguments, for example:
# ○ print(function2(1, 2)) # 1 (because 1-2 is -1, then the absolute value is 1)
# ○ print(function2(2, -1)) # 3 (because 2-(-1) is 3, then the absolute value is 3)
# ○ print(function2(-3, 4)) # 7 (because (-3)-4 is -7, then the absolute value is 7)
# ○ print(function2(-3, -4)) # 1 (because (-3)-(-4) is 1, then the absolute value is 1)


# The abs() function in Python is a built-in function that returns the absolute value of a number.
# abs(number)
def function2(x : int,y : int)->int:
    z = x + y
    return abs(z)


# function3 (1 point)
# ● The function name: function3
# ● This function takes two positional arguments
# ○ First argument: int type
# ○ Second argument: list type (including only int type values or nothing)
# ● The return value: int type
# ○ The number of values in the second argument (a list) that are greater than the
# first argument (int)
# ● This function will be tested with positional arguments, for example:
# ○ print(function3(1, [0, 1, 2, 3])) # 2 (because 2 and 3 are greater than 1)
# ○ print(function3(99, [99, 100, -2, 5])) # 1 (because only 100 is greater than 99)
# ○ print(function3(-3, [7, -6, 0, -10])) # 2 (because 7 and 0 are greater than -3)
# ○ print(function3(9, [3])) # 0 (because there is no digit greater than 9)
# ○ print(function3(10, [ ])) # 0 (because there is no digit greater than 10)
# ○ print(function3(1, [5, 5, 5, 5])) # 4 (because there are four 5 greater than 1)

def function3(x : int,y : list)->int:
    count = 0
    for i in y:
        if (type(i) == int and i > x) :
            count += 1
    return count


# function4 (1 points)
# ● The function name: function4
# ● This function takes one positional arguments
# ○ Only one argument: str type (consisting of only alphabetic characters with a
# length of 1 or more)
# ● The return value: bool type
# ○ True if the given string is a palindrome, ignoring case, and False otherwise
# ○ A palindrome is a string that reads the same forward and backward
# ● This function will be tested with positional arguments, for example:
# ○ print(function4('abcba')) # True
# ○ print(function4('abcBA')) # True
# ○ print(function4('abBa')) # True
# ○ print(function4('c')) # True
# ○ print(function4('APT')) # False
# ○ print(function4('Rose')) # False

def palindrome(y):
    if(y.isalpha() and len(y)>1):
        x = y.lower()
        return str(x) == str(x[::-1])

def function4(x : str)->bool:
    if(palindrome(x)):
        return True
    else:
        return False



# function5 (1 points)
# Using the concept of the Pythagorean equation a2+b2=c2, let's create a function that checks if the given three side lengths of a triangle satisfy the Pythagorean theorem.
# ● The function name: function5
# ● This function takes three positional arguments
# ○ First argument: int type
# ○ Second argument: int type
# ○ Third argument: int type
# ● The return value: bool type
# ○ True if the three arguments satisfy the Pythagorean equation, otherwise returns False
# ● This function will be tested with positional arguments, for example:
# ○ print(function5(3, 4, 5)) # True (because 5**2 = 3**2 + 4**2)
# ○ print(function5(5, 3, 4)) # True (because 5**2 = 3**2 + 4**2)
# ○ print(function5(1, 2, 3)) # False
# ○ print(function5(6, 1, 5)) # False
# ○ print(function5(12, 13, 5)) # True (because 13**2 = 12**2 + 5**2)
# ○ print(function5(7, 24, 25)) # True (because 25**2 = 24**2 + 7**2)
# ○ print(function5(7, 23, 25)) # False

def function5(x : int, y : int, z : int)->bool:
    return x**2 == y**2 + z**2 or y**2 == x**2 + z**2 or z**2 == x**2+y**2

# function6 (1 point)
# ● The function name: function6
# ● This function takes one positional arguments: int type (greater than or equal to 1)
# ● The return value: int type
# ○ The sum of all natural numbers less than or equal to the given argument that are multiples of 2 or 7
# ● This function will be tested with positional arguments, for example:
# ○ print(function6(10)) # 37 (because 2+4+6+7+8+10)
# ○ print(function6(1)) # 0 (because there is no multiple of 2 or 7)
# ○ print(function6(7)) # 19 (because 2+4+6+7)
# ○ print(function6(14)) # 63 (because 2+4+6+7+8+10+12+14)
# ○ print(function6(3)) # 2

def function6(x : int)->int:
    total = 0
    for i in range(x+1):
        if (i%2==0):
            total +=i
        if (i == 7):
            total += i
    return total


# function7 (1 points)
# ● The function name: function7
# ● This function takes one positional arguments: int type (greater than or equal to 2)
# ● The return value: bool type
# ○ True if the given argument is a prime number, otherwise returns False
# ○ *A prime number is a number that has only 1 and itself as factors
# ● This function will be tested with positional arguments, for example:
# ○ print(function7(2)) # True (because the factors are 1 and 2)
# ○ print(function7(3)) # True (because the factors are 1 and 3)
# ○ print(function7(4)) # False (because the factors are 1, 2, 4)
# ○ print(function7(6)) # False (because the factors are 1, 2, 3, 6)
# ○ print(function7(13)) # True (because the factors are 1 and 13)
# ○ print(function7(121)) # False (because the factors are 1, 11, 121)

def function7(num: int)->bool:
    if (num<=1):
        return False
    for i in range(2,num):
        if(num % i ==0 ):
            return False
    return True

# function8 (1 points)
# ● The function name: function8
# ● This function takes one positional argument: str type (consisting of only alphabetic characters with a length of 2 or more)
# ○ Given the string, only one alphabet appears twice, but the other numbers appear once (case insensitive)
# ● The return value: str type
# ○ Find the alphabetic characters that appears twice and return it in lowercase (The alphabet that appears twice must exist.)
# ● This function will be tested with positional arguments, for example:
# ○ print(function8('Hello')) # l (because 'l' appears twice)
# ○ print(function8('Apple')) # p (because 'p' appears twice)
# ○ print(function8('Caffe')) # f (because 'f' appears twice)
# ○ print(function8('Kick')) # k (because 'k' appears twice)
# ○ print(function8('SUMmER')) # m (because 'm' appears twice)

def function8(variable : str)->str:
    duplicate = set()
    for i in variable.lower():
        if i in duplicate:
            return i
        duplicate.add(i)


# function9 (1 points)
# ● The function name: function9
# ● This function takes the unknown number of positional arguments: int types
# ● The return value: int type
# ○ Returns the sum of all the arguments if the number of arguments is even
# ○ Returns the product of all the arguments if the number of arguments is odd
# ○ If there are no arguments, returns 0
# ● This function will be tested with positional arguments, for example:
# ○ print(function9(1, 2)) # 3 (because 1+2 is 3)
# ○ print(function9(1, 2, 3)) # 6 (because 1×2×3 is 6)
# ○ print(function9()) # 0
# ○ print(function9(-21, 23, 13, 98, 0)) # 0 (because (-21)×23×13×98×0 is 0)
# ○ print(function9(1, -1, 2, -2)) # 0 (because 1+(-1)+2+(-2) is 0)
    
def function9(*x):
    if (len(x) == 0):
        return 0
    if(len(x)%2 == 0):
        total = 0
    else:
        total = 1 
    for i in x:
        if(len(x)%2 == 0):
            total += i
        else:
            total *= i
    return total
        

# function10 (1 points)
# ● The function name: function10
# ● This function takes the unknown number of positional or keyword arguments.
# ○ All arguments are int types
# ● The return value: int type
# ○ (The sum of all keyword argument values) - (The sum of all positional
# arguments)
# ○ If there are no positional arguments, their sum is 0
# ○ If there are no keyword arguments, their sum is 0
# ● This function will be tested with positional arguments, for example:
# ○ print(function10(1, 2, a1=10, a2=7)) # 14 (because (10+7) - (1+2))
# ○ print(function10(-1, n=10, k=20)) # 31 (because (10+20) - (-1))
# ○ print(function10(a1=20, a2=5)) # 25 (because (20+5) - (0))
# ○ print(function10(2, 3, 4)) # -9 (because (0) - (2+3+4))
# ○ print(function10()) # 0 (because (0) - (0))

def function10(*args,**kwargs):
    sumPositional = sum(args)
    sumKeyword = sum(kwargs.values())
    return sumKeyword - sumPositional

