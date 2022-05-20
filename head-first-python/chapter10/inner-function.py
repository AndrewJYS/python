def outer():
    def inner():
        print('This is inner')

    print('this is outer, invoking inner')
    inner()

outer()
"""
this is outer, invoking inner
This is inner
"""

def outer():
    def inner():
        print('This is inner')

    print('this is outer, invoking inner')
    return inner

i = outer() # this is outer, invoking inner
i() # This is inner