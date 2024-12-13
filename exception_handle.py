def execption_handle(default_response):
    def decorator(func):
        def wrapper(*args,**kwargs):
            try:
                return func(*args,**kwargs)
            except Exception as e :
                print("Exception occured: ", e)
                return default_response
        return wrapper
    return decorator
@execption_handle(default_response="An error Occured")
def devide_numbers(x,y):
    return x/y
result=devide_numbers(7,0)
print("result:", result)


