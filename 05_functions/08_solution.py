#  **kwargs = key word arguments 
#  **kwargs is a dictionary that allows you to pass a variable number of keyword arguments to a function

def my_func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key,value in kwargs.items():
        print(f"{key} is {value}")


my_func(name="kalki",age=20)
# {'name': 'kalki', 'age': 20}
