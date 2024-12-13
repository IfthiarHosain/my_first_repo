import time
def calculate_function_runtime(func):
    def wraper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        execution_time= end_time-start_time
        print(f"function,{func.__name__} took {execution_time:.4f} second to execute")
        return result
    return wraper
@calculate_function_runtime
def measure_multiply(numbers):
    tot=1
    for x in numbers:
        tot*=x
    return tot
result= measure_multiply([2,3,5,6,7,8,5])
print("Result:", result)