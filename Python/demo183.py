def main(*args):
    try:
        d = {"alpha": 45, "beta": 87}
        val = d.get("alpha", None)
        print(val)
        val = d.get("charli", None)
        print(val)
        val = d.get("petta", {})
        print(val)
    
    
    except Exception as e:
        print("main error : ", e)



if __name__ == "__main__":
    main()

