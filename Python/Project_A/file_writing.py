print("Method = 1:")
f = open("demofile.txt", 'w')
str =\
"""
This is a multi line string. Same method use to  making comments in programme.
So never be confuse comments are a string which are not assign in any variable.
There is a real way to giving comments in python that is using # symbol. But
this give comment of one line. This is not multiline comment. So for multiline
comment we use this 3 inverted commas.
    May language have different rules and symbol for comment. you can not use
that rule in python coz python is another programming language. 
"""
data = f.write(str)
f.close()
print()

with open('demofile.txt', 'r') as f:
    data = f.read()
    print(data)