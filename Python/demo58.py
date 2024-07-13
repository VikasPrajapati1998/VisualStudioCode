import sys

# --------------------------------------------------------------------------
def fun():
    y = 20
    print(f"x={x}, y={y}")
    print(len(str(x)))
    
    def foo():
        z = 30
        print(f"x={x}, y={y}, z={z}")
        print(len(str(x)))
        print("foo locals : ", locals())
        print("foo globals : ", globals())
        
    foo()
    
    print("fun locals : ", locals())
    print("fun globals : ", globals())
# -------------------------------------------------------------------------

# =========================================================================
def main(*args):
    try:
        for path in sys.path:
            print(path)
        print()
        fun()
        
    except Exception as e:
        print("main error : ", e)
# ========================================================================

# ########################################################################
x = 10
print(f"lenght(x)={len(str(x))}")
print("__main__ locals : ", locals())
print("__main__ globals : ", globals())

if __name__ == "__main__":
    main()

# ########################################################################

