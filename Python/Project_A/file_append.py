print("Method = 1:")
f = open("demofile.txt", 'a')
str =\
"""
As we know that C/C++ has different method for cmment and java is also having different
methods for comment. We are seeing this as the programming language changing the rule of
comment is also changing.
Markup language also having comment system to increase the readability of program. In a
big program comments are very useful to find a place. Or to Identify a section of code
we use comment as a mark symbol. We have seen this in python that when we start putting
comments the color of text are changed automatically. It is set by designer. Who is
designing that language. All the rules for any programing language is depend on its
creator. Creator always try to make there programming language easy to write code and
also easy to modify code.
He is keeping this in mind that how he can make it better and unique to the other programming
languages.
"""
data = f.write(str)
f.close()
print()

with open('demofile.txt', 'r') as f:
    data = f.read()
    print(data)