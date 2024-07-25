def isprime(num:int)->bool:
    try:
        if num > 1:
            for i in range(2, (num // 2)+1):
                if num % i == 0:
                    return False
            else:
                return True
        else:
            return False
        
    except Exception as e:
        print("isprime error : ", e)


# generator
def generate_primes():
    try:
        num = 1
        while True:
            if isprime(num):
                yield num
            num += 1
    except Exception as e:
        print("generate_primes error : ", e)

# ############################################################################################
def main(*args):
    try:
        total = 0
        for next_prime in generate_primes():
            if next_prime < 30000:
                # print(next_prime, end=", ")
                total += next_prime
            else:
                print(total)
                break
        # print(type(generate_primes))
    
    except Exception as e:
        print("main error : ", e)


# ############################################################################################




if __name__ == "__main__":
    main()

