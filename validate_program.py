def validate_arguements(condition):
    def decorator (func):
        def wrapper(*args,**kwargs):
            if condition(*args,**kwargs):
                return func(*args,**kwargs)
            else:
                raise ValueError("invalid arguments passed to the function")
        return wrapper
    return decorator
@validate_arguements(lambda x:x>0)
def calculate_cube(x):
   return x**3
print(calculate_cube(5))
print(calculate_cube(-2))




