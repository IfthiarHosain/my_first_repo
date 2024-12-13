def cache_results(func):
    cache={}
    def wrapper(*args,**kwargs):
        key=(*args,*kwargs.items())
        if key in cache:
            print("retrive result from cache: ")
            return cache[key]
        result= func(*args,**kwargs)
        cache[key]=result
        return result
    return wrapper
@cache_results
def calculate_multply(x,y):
    print("calculate two variables :")
    return x*y
print(calculate_multply(4,5))
print(calculate_multply(4,5))
print(calculate_multply(5,7))
print(calculate_multply(5,7))
print(calculate_multply(3,4))
print(calculate_multply(3,4))