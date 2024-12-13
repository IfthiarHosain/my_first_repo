import inspect
def enforce_type_checking(func):
    def wrapper(*args,**kwargs):
        signature=inspect.signature(func)
        parameters=signature.parameters
        for i, arg in enumerate(args):
            param_name=list(parameters.keys())[i]
            param_type=parameters[param_name].annotation
            if not isinstance(arg,param_type):
                raise TypeError (f"Argument{param_name} must be type of {param_type.__name__}")
        for param_name, arg in kwargs.items():
            param_type=parameters[param_name].annotation
            if not isinstance(arg,param_type):
                raise TypeError (f"Argument{param_name} must be tyow of {param_type.__name__}")
        return func (*args,**kwargs)
    return wrapper
@enforce_type_checking
def multiply_numbers(x:int,y:int):
    return x*y
result= multiply_numbers(5,7)
print("Result", result)
result= multiply_numbers("5",7)
    