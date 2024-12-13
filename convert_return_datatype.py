def convert_to_a_datatype(data_type):
    def decorator(func):
        def wrapper(*args,**kwargs):
            result=func(*args,**kwargs)
            return data_type(result)
        return wrapper
    return decorator
def add_numbers(x,y):
    return x+y
result= add_numbers(10,20)
print("Result", result, type(result))
def concatenate_str(x,y):
    return x+y
result= concatenate_str("python", "decorator")
print("Result:",result,type(result))