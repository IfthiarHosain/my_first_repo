def decorators(func):
    def wrap (*args,**kwargs):
        print(f"calling {func.__name__} with args{args},kwargs{kwargs}")
        result=func(*args,**kwargs)
        print(f"{func.__name__} returned:{result}")
        return result
    return wrap
@decorators
def multiple_numbers(x,y):
    return x*y
result= multiple_numbers(10,20)
print("Result: ", result)
