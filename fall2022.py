
# ● The function name: function01
# ● This function takes two positional arguments
# ○ First argument: int type
# ○ Second argument: int type
# ● The return value
# ○ sum of the two arguments
# ● For example, this function will be tested with positional arguments as follows:
# ○ function01(1, 2) returns 3
# ○ function01(0, 0) returns 0
# ○ function01(-1, -2) returns -3

def function1(x : int,y : int)->int:
    return x + y



# ● The function name: function02
# ● This function takes one positional argument
# ○ a list or tuple which has only int type elements
# ● The return value
# ○ Sum of all elements. Return 0 if there is no element.
# ● For example, this function will be tested with positional arguments as follows:
# ○ function02([1, 2, 3, 4, 5]) returns 15
# ○ function02((1, 2, -3, 4)) returns 4
# ○ function02([]) returns 0
def function2(x):
    if not x:
        return 0
    else:
        return sum(x)


# ● The function name: function03
# ● This function takes two positional arguments
# ○ First argument: int type
# ○ Second argument: int type (this argument is bigger than the first argument)
# ● The return value
# ○ sum of integers which is between the first argument and the second argument
# (not including the first and second arguments)
# ● For example, this function will be tested with positional arguments as follows:
# ○ function03(1, 4) returns 5
# ○ function03(0, 3) returns 3○ function03(-3, -1) returns -2
def function3(x : int,y : int):
    return sum(range(x+1,y))



# ● The function name: function04
# ● This function takes one positional argument
# ○ a list or tuple which has only int type elements
# ● The return value
# ○ Sum of elements which are even. Return 0 if there is no element.
# ● For example,
# ○ function04([1, 2, 3, 4, 5]) returns 6
# ○ function04((1, 3, 2)) returns 2
# ○ function04([]) returns 0
# ○ function04([-2, 0, 1]) returns -2
def function4(x):
    if(len(x)==0):
        return 0
    total = 0
    for i in x:
        if (i %2 ==0):
            total += i
    return total



# ● The function name: function05
# ● This function takes one positional argument
# ○ str type (a length of the argument is greater than 1. All the characters are
# alphabet letters.)
# ● The return value
# ○ The string with the uppercase first character and lowercase remaining
# characters
# ● For example, this function will be tested with positional arguments as follows:
# ○ function05(“hello”) returns “Hello”
# ○ function05(“heLLO”) returns “Hello”
# ○ function05(“pythoN”) returns “Python”
# ○ function05(“AA”) returns “Aa”
def function5(x):
    return x.capitalize()
        

# ● The function name: function06
# ● This function takes one positional argument
# ○ str type (the length of this argument is greater than 1. All the characters are
# alphabet letters, no spaces)
# ● The return value (bool type)
# ○ True if the argument is palindrome, False otherwise. (ignore cases)
# ○ [Tip] The palindrome is a word that reads the same backwards as forwards,
# such as “우영우”, “기러기”, “인도인”, “level”, “mygym”, and “ABCcba”.
# ● For example, this function will be tested with positional arguments as follows:
# ○ function06(“level”) returns True
# ○ function06(“levEL”) returns True
# ○ function06(“Aa”) returns True
# ○ function06(“hello”) returns False (because “hello” != “olleh”)○ function06(“pythoN”) return False (because “pythoN” != “Nohtyp”)
def function6(x):
    temp = x.lower()
    if(str(temp) == str(temp[::-1])):
        return True
    else:
        return False


# ● The function name: function07
# ● This function takes one positional argument
# ○ a list or tuple which has only int type elements
# ● The return value
# ○ Sum of only unique elements from the given argument (for example, if [1, 2,
# 3, 3, 3] is given, return sum of 1, 2, 3 after removing two 3 which are
# duplicated.). Return 0 if there is no element.
# ● For example, this function will be tested with positional arguments as follows:
# ○ function07([1, 2, 2, 3, 3, 3]) returns 6
# ○ function07((2, 2, 1)) returns 3
# ○ function07([-1]) returns -1
# ○ function07((-1, -1, 0, 1)) returns 0
def function7(x):
    uniqueNum = set(x)
    return sum(uniqueNum)
        


# ● The function name: function08
# ● This function takes the unknown number of positional arguments
# ○ all arguments are int type
# ● The return value
# ○ Sum of the arguments which are even. Return 0 if there is no argument.
# ● For example, this function will be tested with positional arguments as follows:
# ○ function08() returns 0
# ○ function08(1) returns 0
# ○ function08(1, 2, 3) returns 2
# ○ function08(1, -2, 3, 6) returns 4
# ○ function08(1, 2, 3, 4, 5) returns 6
def function8(*x):
    total = 0
    for i in x:
        if(i % 2 == 0):
            total += i
    return total



# ● The function name: function09
# ● This function takes the unknown number of positional or keyword arguments
# ○ All arguments are int type
# ● The return value
# ○ A maximum value of the keyword arguments’ values (not keys)
# ○ If there are no keyword arguments, return -1
# ● For example, this function will be tested with positional and keyword arguments as
# follows:
# ○ function09() returns -1
# ○ function09(1, 2, 3) returns -1
# ○ function09(a=1, b=2) returns 2○ function09(1, 2, 7, n1=5, n2=4) returns 5
# ○ function09(5, k=2) returns 2
def function9(*positional,**kwargs):
    if(kwargs):
        return (max(kwargs.values()))
    return -1


# ● The function name: function10
# ● This function takes one positional argument
# ○ int type (positive integer)
# ● The return value
# ○ N th (the argument) number from Fibonacci sequence
# ○ ※ The Fibonacci sequence is a set of integers that starts with two 1. Then,
# the sequence follows the rule that each number is equal to the sum of the
# preceding two numbers.
# ■ 1, 1, 2, 3, 5, 8, 13, 21, 34 ……
# ● For example, this function will be tested with positional arguments as follows:
# ○ function10(1) returns 1
# ○ function10(2) returns 1
# ○ function10(3) returns 2
# ○ function10(4) returns 3
# ○ function10(5) returns 5
# ○ function10(6) returns 8
def function10(n):
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b



    
