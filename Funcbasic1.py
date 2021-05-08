# 1 - should return and print 5

def number_of_food_groups():
    return 5


print(number_of_food_groups())


# 2 - my initial guess was that 5 would have been returned, however
# since the arguments are not defined there is an error running the code
def number_of_military_branches():
    return 5


print(number_of_days_in_a_week_silicon_or_triangle_sides() +
    number_of_military_branches())


# 3 - 5 should be returned since the first return statment is 5
def number_of_books_on_hold():
    return 5
    return 10


print(number_of_books_on_hold())


# 4 - 5 should return before the print statment making it
# the only response to this call
def number_of_fingers():
    return 5
    print(10)


print(number_of_fingers())


# 5 - this function never seems to be called so I imagine nothing shall return,
# this one confused me from a base level of understanding.  It looks like what happens
# is that the function is called and that it will first print 5 and then print none, as
# there is no value of great lakes initial paramater set
def number_of_great_lakes():
    print(5)


x = number_of_great_lakes()
print(x)


# 6 - my guess here is that 3 will print, then 5 will print and then 8 will print
# - the first part of my guess was correct, but add(1,2) and add(2,3) are coming
# back with type none and so 8 does not print. I imagine this is because no return
# statement is ever made
def add(b, c):
    print(b+c)


print(add(1, 2) + add(2, 3))


# 7 - here I believe that '25' will be returned and printed
def concatenate(b, c):
    return str(b)+str(c)


print(concatenate(2, 5))


# 8 - I believe here b will print 100 and then as it is greater than 10 will be returned
# and printed.  There are actually formatting issues with this function and it therfore does
# not run at all.
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


# 9 - I believe that this will evaluate each print call and return the corresonding values.
#   The results should be 7 then 14 then 7 + 14 to print 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3


print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3) + \
    number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))


# 10 I believe this will return and print 8
def addition(b, c):
    return b+c
    return 10


print(addition(3, 5))


# 11 500 - 500 - 300 - 300 was my initial guess however the foobar function only runs once
#   and its value is independent of the prestablished b=500 since there is no return call
#   and will not persist thus 500 - 500 - 300 - 500 is the result
b = 500
print(b)


def foobar():
    b = 300
    print(b)


print(b)
foobar()
print(b)


# 12 500 - 500 - 300 - 300 will be the result as, unlike above, there is a return call to the function's new value.
#   This thinking was however wrong again as though the value is returned to the call, it is not printed so nothing
#   actually happens with it then AGAIN the call for b to print refers to the preestablished var who's value is 500.
b = 500
print(b)


def foobar():
    b = 300
    print(b)
    return b


print(b)
foobar()
print(b)


# 13 500 - 500 - 300 - 300.  Fool me once shame on me, fool me TWICE then I'm not grasping this at all.  Now, since
#   not only is the value retuened, but b set to equal the foobar function, will it's value be changed to reflect a
#   new value when the last print(b) is called.
b = 500
print(b)


def foobar():
    b = 300
    print(b)
    return b


print(b)
b = foobar()
print(b)


# 14 - The call from foo() jumps the code up to the function which runs printing 1 then calling on the bar function.
#   bar then prints 3 before resuming the foo() call to like 135 where 2 should finally print.
def foo():
    print(1)
    bar()
    print(2)


def bar():
    print(3)


foo()


# 15 - print y calls on its value, which is the foo() function, resulting in that code block initilizing.
#   1 is printed and x is set to bar().  The print call of x runs the bar function printing 3 and returning 5
#   to the print x call, so 5 also prints.  10 is the returned to the initial call of print y and it is finally printed.
#   1 - 3 - 5 - 10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10


def bar():
    print(3)
    return 5


y = foo()
print(y)