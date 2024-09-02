# decorator
import functools, time

# ______________________________________________ Decorators ____________________________________________
def debugger(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        
        value = func(*args, **kwargs)
        
        print(f"{func.__name__}() returned {repr(value)}")
        return value
    return wrapper_debug

def timer(func):
    @functools.wraps(func)
    def wrapper_time(*args, **kwargs):
        start_time = time.perf_counter()
        
        value = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs.")
        return value
    return wrapper_time
# ________________________________________________________________________________________________________


# ___________________________________________ classes ____________________________________________________

@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num_list = [num for num in range(max_num) if num%2 == 0]
    
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([num**2 for num in range(self.max_num)])
    
    def __del__(self):
        del self.max_num_list
# ________________________________________________________________________________________________________

# ___________________________________________ functions __________________________________________________
@timer
@debugger
def print_list(*args):
    lst = []
    for x in args[0]:
        lst.append(x**2)
    return lst
# ________________________________________________________________________________________________________

    
# ========================================== Main ========================================================
def main(*args):
    try:
        tw = TimeWaster(4000)
        tw.waste_time(10)
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()
        
# ========================================================================================================



if __name__ == "__main__":
    main()
