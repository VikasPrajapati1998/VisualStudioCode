# Creating Data Processing Pipeline with Generator Iterators

import math_pipeline as mpl

def main(*args):
    try:
        lst_even = list(
            mpl.to_string(
                mpl.to_squire(
                    mpl.to_even(
                        range(20)
                    )
                )
            )
        )
        print(lst_even)
        
        lst_odd = list(
            mpl.to_string(
                mpl.to_squire(
                    mpl.to_odd(
                        range(20)
                    )
                )
            )
        )
        print(lst_odd)
    
    except Exception as e:
        print("main error : ", e)


if __name__ == "__main__":
    main()


