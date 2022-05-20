def function1(num: int):
    num += 1

num1 = 4
print(num1)
function1(num1)
print(num1)


website = "JournalDev.com"

def print_website():
    global website
    print(f'My favorite website is {website}')

    website = 'Wikipedia.com'
    print(f'My favorite website is {website}')

print_website()
print(f'My favorite website is {website}')


import static_variable_pk as st

def static_test():
    st.static_var += 4
    print(st.static_var)

static_test()  # output 5
static_test()  # output 9
