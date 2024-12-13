import tracemalloc
def measure_memory_usage(func):
    def wrapper(*args,**kwargs):
        tracemalloc.start()
        result=func(*args,**kwargs)
        snapshot=tracemalloc.take_snapshot()
        top_stats=snapshot.statistics("lineno")
        print("memory consumtion of ", func.__name__)
        for stat in top_stats [:5]:
            print(stat)
        tracemalloc.stop()

        return result
    return wrapper
@measure_memory_usage
def calculate_factorial(n):
    if n==0:
        return 1
    else:
        return n*calculate_factorial(n-1)
result= calculate_factorial(5)
print("Result",result)

