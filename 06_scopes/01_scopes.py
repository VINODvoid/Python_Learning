username = "kalki"

def func():
    # username = "tea"
    print(username)

print(username)
func()

x = 10
# def func1(y):
#     z = x+y
#     return z

# result = func1(1)
# print(result)

def func2():
    global x
    x = 99

func2()
print(x)


def f1():
    x = 23
    def f2():
        print(x)
    return f2
my_result =f1()
my_result()

def power(num):
    def pw(x):
        return x ** num
    return pw

power_square = power(3)
print(power_square(5))