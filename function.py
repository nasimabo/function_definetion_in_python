############################ function definetion ##############

'''def fnc(a,b): #paramiter
    sum = a+b
    print(sum)

fnc(5,10)''' # argument


'''def fnc(a,b):
    return a+b
print(fnc(5,15))'''

'''def fnc():
    print("hello")

output = fnc()
print(output)'''

'''def avg(a,b,c):
    sum = a+b+c
    av = sum / 2
    print(av)
    return av
result = avg(1,2,3)
print(result)'''

'''def fnc(a,b=5):
    print(a*b)
    return a*b

fnc(1)'''


############################ pactices qs ##############


'''count = ["Dhaka","rongpur","khulna","kustiya","gopalgonj"]

def count_def(con):
    print(len(con))

count_def(count)'''


'''count = ["Dhaka","rongpur","khulna","kustiya","gopalgonj"]

def pri_def(li):
    for i in li:
        print(i,end=" ")

pri_def(count)'''

'''def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    print(fac)

factorial(5)'''

'''def converter(usd):
    con_usd = usd * 126
    print(usd,"USD =",con_usd,"TAKA")
converter(int(input("Enter the usd: ")))'''

'''def eve(n):
    if (n % 2 == 0):
        print("even")
    else:
        print("odd")

x = int(input("Enter the number: "))

eve(x)'''


########################## Recursion function ##############

'''def rec(n):
    if (n == 0):  # base case
        return
    print(n)
    rec (n-1)
    print('hello')

rec(5)'''

'''def fac(n):
    if (n == 0 or n == 1):
        return 1
    return fac(n-1) * n

print(fac(4))'''


########################## Recursion function ##############


'''def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n
print(cal_sum(10))'''

def print_list(li,idx = 0):
    if (idx == len(li)):
        return
    print(li[idx])
    print_list(li,idx+1)

li = ['mango','banana','apple','orange']

print(print_list(li))


























    
