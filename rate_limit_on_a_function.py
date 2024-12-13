import time
def rate_limits(max_calls,period):
    def decorator(func):
        calls=0
        last_reset=time.time()
        def wrapper(*args,**kwargs):
            nonlocal calls,last_reset
            current_time=time.time()
            elapsed=current_time-last_reset
            if elapsed > period:
                calls=0
                last_reset=current_time
            if calls >= max_calls:
              raise Exception("rate limit exceeded.try agin later.")
            calls +=1
            return func(*args,**kwargs)
        return wrapper
    return decorator
@rate_limits(max_calls=6,period=10)
def api_call():
    print("Api call executed successfully...")
for _ in range(8):
    try:
        api_call()
    except Exception as e :
        print(f"Error occured",{e})
