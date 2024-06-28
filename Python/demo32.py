import random

def third_largest(nums):
    if len(set(nums)) < 3:
        return "Array doesn't have a third largest element"
    sorted_nums = sorted(set(nums), reverse=True)
    return sorted_nums[2]


def main():
    try:
        pass
    
    except Exception as e:
        print(e)
    
    finally:
        print()
    

