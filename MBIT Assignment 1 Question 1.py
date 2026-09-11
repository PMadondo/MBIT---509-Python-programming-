|import time

def rate_limit(max_calls: int, period: int):
    def decorator(func):
        calls = []
        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove timestamps older than the period window
            calls = [t for t in calls if now - t < period]
            if len(calls) >= max_calls:
                raise Exception("Rate limit exceeded")
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3, period=10)
def fetch_user_data(user_id):
    return f"Data for {user_id}"

# Bug 1 - This is because calls is assigned within the Python treats it as a local variable throughout wrapper. Then, on the right side of that same line, one will be try to read the local variable before it has been assigned, which  then results in the UnboundLocalError.

# Bug 2 - Modify the state tracking by storing timestamps on the instance (self) instead of in a shared closure. The wrapper can use the first argument (self) as the key rate-limit access.





