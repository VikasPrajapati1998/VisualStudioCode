def main(*args):
    try:
        i = 5
        print(f"int : Value: {i}, Type: {type(i)}, Hash: {hash(i)}")
        
        f = 5.6
        print(f"float: Value: {f}, Type: {type(f)}, Hash: {hash(f)}")
        
        s = "Alpha"
        print(f"string: Value: {s}, Type: {type(s)}, Hash: {hash(s)}")
        
        l = [5, 6, 7, 8]
        # Lists are mutable, hence not hashable
        try:
            print(f"list: Value: {l}, Type: {type(l)}, Hash: {hash(l)}")
        except TypeError as e:
            print(f"List is not hashable: {e}")
        
        t = (3, 4, 5, 6)
        # Tuples are hashable if all their elements are hashable
        print(f"tuple: Value: {t}, Type: {type(t)}, Hash: {hash(t)}")
        
        s = {1, 2, 3, 4}
        # Set are mutable, hence not hashable
        try:
            print(f"set: Value: {s}, Type: {type(s)}, Hash: {hash(s)}")
        except TypeError as e:
            print(f"Set is not hashable: {e}")
        
        d = {"a": 1, "b": 2, "c": 3}
        # Dictionaries are mutable, hence not hashable
        try:
            print(f"dict: Value: {d}, Type: {type(d)}, Hash: {hash(d)}")
        except TypeError as e:
            print(f"Dictionary is not hashable: {e}")
        
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print("Finished checking hashability.")

if __name__ == "__main__":
    main()
