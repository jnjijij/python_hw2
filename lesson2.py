# a = 5
# b = 7
#
# res = a,b
#
# print(res)

# b, a = a, b
#
# print(b, a)

# l = [1, 2, 3, 4, 5, 6]
#
#
# a, b, *_, c = 1
#
# print(a)
# print(b)
# print(c)
# print(_)

# l = [1,2,3,4]
#
# *_, a,b = l
# print(a, b)

# l1=[1,2,3]
#
# l2 = [*l1]





# def decor(func):
#     def inner():
#         print('*'*20)
#
#     return inner
# @decor
# def greeting():
#     print('hello')
# inner = decor(greeting)
#
#
# inner()

#
# inner = decor(greeting)
#
#
# inner()
# greeting('Max')


# for i in range(5):
#     pass
#
# print(i)

# i = 666
# for i in range(5):
#     pass
# print(globals())

# def a():
#     name = 'max'
#     print(locals())
#
# a()
#
# print(globals())


# name = 'Max'
# def a():
#     # name = 'Vasia'
#
#    def b():
#        global name
#        name = 'Petia'
#        print(name)
#
#    b()
#    print(name)
#
#
#
# a()


# def counter():
#     count = 0
#
#     def inc():
#         nonlocal count
#         count+=1
#         return count
#
#     return inc
#
#
# counter1 = counter()
# counter2 = counter()
#
# print(counter1())
# print(counter2())
# print(counter1())
# print(counter2())
# print(counter1())
# print(counter2())

# l1 = [1,2,3,-1,6,8,9]
#
#
# # l.sort(reserve=True)
# l2 = sorted
#
# print(l1)
# print(l2)

# users = [
#     {'name':'max', 'age':15},
#     {'name':'oleh', 'age':20},
#     {'name':'masha', 'age':25},
#     {'name':'dashs', 'age':30},
# ]
#
# def func(item):
#     return item['age']
#
# func = lambda item:item['age']
#
# users.sort(key=lambda item:item['age'], reverse=True)
#
# print(users)



# a: str = 123
#
# print(a+2)

# d = {
#     'name': 'max '
# }
# def func(string:list[str])-> str | int:
#     return 333

# t:tuple[int, str, int] = (1, 's' , 3)

# import typing
#
# typing.TypedDict
#
 from typing import TypedDict, Callable
#
# User = TypedDict("User", {'name': str, 'age':int, 'status': bool}, total=False)

def counter()->callable([], int):
    count = 0


    def inc(a: str, b:int) -> int:
        nonlocal count
        count += 1
        return count

    return inc








