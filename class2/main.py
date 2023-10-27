# try: # when get erorr
#     x = int(input())
#     print(x)
#     print(type(x))
# except (TypeError, ValueError): # when except catch error
#     print("You have to input 0-9")
# else: # when there is no error
#     print("ok")

# finally: # all time runs
#     print("Finally")



# def function():
#     print("Hello")


# function()

# def function(a=2):
#     for i in range(a):
#         print(i)


# function(5)


## argument

# def function(*a):
#     try:
#         print(a[4])
#         print(*a)
#     except IndexError:
#         print("You have to input at least 4 value")

# function(3, 6, "ER")
# function(3, 6, "R")


## keyword argument

# def function(a=3 , b =5, **kwargs):
#     # print(a, b)
#     print(b)
#     print(kwargs['ui'])

# function(b = 10, a = 45, ui = "rty")



# for i in range(6):
#     if i <= 3:
#         print(i)

# # list comprehension
# print([i for i in range(6) if i<=3])

# def function():
#     print("Hello")


# function()

# x = lambda x=3, y =4 : [(i, y) for i in range(x)]
# print(x())


# iterator

# asdf = ("grghg", "rtgrtg", "htryhtyuh")

# mt = iter(asdf)

# print(next(mt))
# print(next(mt))
# print(next(mt))
# try:
#     print(next(mt))
# except StopIteration:
#     print("Limit exceeded")