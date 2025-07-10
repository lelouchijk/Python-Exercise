
# ● The function name: function1
# ● This function takes three positional arguments
# ○ First argument: int type
# ○ Second argument: int type
# ○ Third argument: int type
# ● The return value: int type
# ○ Sum of the three arguments
# ● This function will be tested with positional arguments, for example:
# ○ print(function1(1, 4, 5)) # 10 (because 1+4+5 is 10)
# ○ print(function1(0, 3, -9)) # -6 (because 0+3+(-9) is -6)
# ○ print(function1(-3, -2, 5)) # 0 (because (-3)+(-2)+5 is 0)
# ○ print(function1(0, 999, 1)) # 1000 (because 0+999+1 is 1000)
def function1(x : int, y : int, z : int)->int:
    return x + y + z


# ● The function name: function2
# ● This function takes one positional argument: list type (all elements are int types)
# ● The return value: int type
# ○ Sum of elements which are odd numbers, such as -3, -1, 1, 3, 5, 7 ….
# ○ If the given argument has no odd numbers, return 0.
# ● This function will be tested with positional arguments, for example:
# ○ print(function2([1, 2, 3])) # 4 (because 1+3 is 4)
# ○ print(function2([ ])) # 0 (because there are no odd numbers to sum)
# ○ print(function2([1, 2, 3, 4])) # 4 (because 1+3 is 4)
# ○ print(function2([-3, 1, 3, 2, 100])) # 1 (because (-3)+1+3 is 1)
def function2(x : list)->int:
    temp = 0
    if(len(x)==0):
        return 0
    for i in x:
        if (i % 2 == 0):
            continue
        temp += i
    return temp



# ● The function name: function3
# ● This function takes one positional argument: list type (all elements are int types)
# ○ There is no duplicated number.
# ● The return value: int type
# ○ The second largest number from the given list.
# ○ If the given argument is an empty list, return 0.
# ○ If the given argument has only one element, return the element.
# ● This function will be tested with positional arguments, for example:
# ○ print(function3([ ])) # 0 (because there is no element.)
# ○ print(function3([-99])) # -99 (because there is only 99 in the given list.)
# ○ print(function3([3, 1, 2, 0])) # 2 (because 2 is the second largest number.)
# ○ print(function3([99, 2, -1, 100])) # 99 (because 2 is the second largest number.)
# ○ print(function3([-1, -3, -2, 0])) # -1 (because -1 is the second largest number.)
def function3(x : list)->int:
    if (len(x)==0):
        return 0
    if(len(x)==1):
        return x[0]
    x.sort()
    largest = x[-2]
    return largest


# ● The function name: function4
# ● This function takes one positional argument: str type
# ○ The length of the argument is greater than 2.
# ○ All the characters are alphabet letters.
# ● The return value: str type
# ○ A string in which only the last letter is upper-case and the rest is lower-case.
# ● This function will be tested with positional arguments, for example:
# ○ print(function4("Hello")) # hellO
# ○ print(function4("PyTHON")) # pythoN
# ○ print(function4("abc")) # abC
# ○ print(function4("ClasS")) # clasS
def function4(x : str)->str:
    tempStr = x[::-1]
    temp = tempStr.capitalize()
    realStr = temp[::-1]
    return realStr


# ● The function name: function5
# ● This function takes one positional arguments: str type
# ○ The argument includes at least one numeric letter.
# ○ All letters are alphabetic or numeric.
# ● The return value: str type
# ○ The average of all digit letters from the given argument as str type
# ● This function will be tested with positional arguments, for example:
# ○ print(function5("todayis0425")) # 2.75 (because ((0+4+2+5) / 4) is 2.75)
# ○ print(function5("h2a0p2p3y")) # 1.75 (because ((2+0+2+3) / 4) is 1.75)
# ○ print(function5("A1B2C3")) # 2.0 (because ((1+2+3) / 3) is 2.0)
# ○ print(function5("pyt0hon")) # 0.0 (because 0/1 is 0)

def function5(x : str)->str:
    count = 0
    temp = 0
    for i in x:
        if(i.isdigit()):
            temp += int(i)
            count +=1
    ans = temp / count
    return ans



# ● The function name: function6
# ● This function takes two positional arguments
# ○ The first argument: int type (greater than 1 and smaller than 1000)
# ○ The second argument: int type (greater than 1 and smaller than 1000)
# ● The return value: set type
# ○ All common factors that divide the two given arguments leaving no remainder.
# ○ For example,
# ■ The factors of 6 are 1, 2, 3, and 6. The factors of 10 are 1, 2, 5, and 10.
# ■ Then, the common factors of the two numbers are {1, 2}.
# ● This function will be tested with positional arguments, for example:
# ○ print(function6(6, 10)) # {1, 2}
# ○ print(function6(2, 3)) # {1}
# ○ print(function6(24, 12)) # {1, 2, 3, 4, 6, 12}
# ○ print(function6(11, 121)) # {1, 11}
def function6(x : int, y : int)->set:
    x1 = set()
    y1 = set()
    for i in range(1,x+1):
        if(x % i == 0):
            x1.add(i)

    for j in range(1,y+1):
        if(y % j ==0):
            y1.add(j)

    ans = x1.intersection(y1) 
    return ans



# i used ai assit for this solution
# def function7(x : dict)->int:
    
#     for i in x:
#         if((x.keys() != "math")):
#             list1.append(x.values())
#     print(list1)
#     # return sum(list1)
# print(function7({"math": 90, "english": 25, "korean": 30}))



# ● The function name: function8
# ● This function takes one positional argument: list type (all elements are int types)
# ○ There is at least one element in the given list.
# ○ Given the list of integers, only one number appears once, but the other numbers
# appear twice.
# ● The return value: int type
# ○ Find the number that appears once. (The number that appears once must exist.)
# ● This function will be tested with positional arguments, for example:
# ○ print(function8([4,1,2,1,2])) # 4 (because 4 appears once)
# ○ print(function8([1])) # 1 (because 1 appears once)
# ○ print(function8([2, 2, -1])) # -1 (because -1 appears once)
# ○ print(function8([-1, 1, -1, 99, 1, 2, 2])) # 99 (because 99 appears once)
# i used ai assit for this solution        
def function8(x):
    for i in x:
        if(x.count(i)==1):
            return i


# ● The function name: function9
# ● This function takes two or three positional argument: all arguments are int types
# ● The return value: int type
# If two arguments are given, return the sum of the two arguments+10.
# ○ If three arguments are given, return the sum of the three arguments.
# ● This function will be tested with positional arguments, for example:
# ○ print(function9(1, 2)) # 13 (because 1+2+10 is 13)
# ○ print(function9(1, 2, 3)) # 6 (because 1+2+3 is 6)
# ○ print(function9(-9, -1)) # 0 (because ((-9)+(-1)+10 is 0)
# ○ print(function9(10, 20, -30)) # 0 (because 10+20+(-30) is 0)
def function9(*x):
    if (len(x)<=2):
        return sum(x)+10
    else:
        return sum(x)


# ● The function name: function10
# ● This function takes the unknown number of positional or keyword arguments.
# ○ All arguments’ values are int types.
# ● The return value: int type
# ○ (Sum of all keyword arguments’ values) - (Sum of all positional arguments)
# ○ If there are no positional arguments, the sum of all positional arguments is 0.
# ○ If there are no keyword arguments, the sum of all keyword arguments is 0.
# ● This function will be tested with positional arguments, for example:
# ○ print(function10(1, 2, a=10, b=7)) # 14 (because (10+7) - (1+2))
# ○ print(function10(-1, n=10, k=20)) # 31 (because (10+20) - (-1))
# ○ print(function10(age=20, height=175)) # 195 (because (20+175) - (0))
# ○ print(function10(1, 2, 3, 4)) # -10 (because (0) - (1+2+3+4))
# ○ print(function10()) # 0 (because (0) - (0))
def function10(*x,**y):
    sumPositional = sum(x)
    sumKeyword = sum(y.values())
    return sumKeyword - sumPositional
