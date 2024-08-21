'''
1. Understand the Json Syntax
2. Convert Python data to Json
3. Deserialize Json to Python
4. Write and Read Json Files
5. Validate Json Syntax
6. Prettify Json in the terminal
7. Minify Json with Python

JSON Data Type: 
    object : A collection of key-value pairs inside curly braces. {}
    array : A list of values wrapped in square brackets. []
    string : Text wrapped in double quotes. ""
    number : Integers or floating-point numbers.
    boolean : Either true of false without quotes.
    null : Represents a null value, written as null.
    
JSON Syntax Pitfalls:
    Do not allow any comments.
    Do not use single quotes for string.
    Do not use trailing comma after the final key-value pair.
    Do not contains a trailing comma in the array.
    
Serialize Python Data Types to JSON
Python  >---------->>>  JSON    >---------->>>  Python
____________________________________
dict    >---------->>>  object  >---------->>>  dict  
list    >---------->>>  array   >---------->>>  list
tuple   >---------->>>  array   >---------->>>  list
str     >---------->>>  string  >---------->>>  str
int     >---------->>>  number  >---------->>>  int
float   >---------->>>  number  >---------->>>  float
True    >---------->>>  true    >---------->>>  True
False   >---------->>>  false   >---------->>>  False
None    >---------->>>  null    >---------->>>  None

'''
def main(*args):
    try:
        import json
        
        # dictionary
        food_ratings = {
            "organic dog food": 2,
            "human food": 10
        }
        
        # serialization
        print(json.dumps(food_ratings))
        
        
    
    except Exception as e:
        print("main error : ", e)
    
    finally:
        print()


if __name__ == "__main__":
    main()



