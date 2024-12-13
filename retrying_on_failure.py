import sqlite3
import time
def retrying_on_failure(max_retries,delay=1):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(max_retries):
                try:
                    result=func(*args,**kwargs)
                    return result
                except Exception as e :
                    print(f"Error occurd: {e} retryng...." )
                    time.sleep(delay)
            raise Exception("Maximum retries exceeded.function failed.")
        return wrapper
    return decorator
@retrying_on_failure(max_retries=3,delay=2)
def connect_to_database():
    conn= sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute("SELECT *FROM users")
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result
try:
    data=connect_to_database()
    print("DAta receve successfully:", data)
except Exception as e:
    print(f"failed to connect database: {e}" )

                    