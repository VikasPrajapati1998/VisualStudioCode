# String
msg = "Survival Transformer"

# String Built-in Functions
print(len(msg))
print(min(msg), max(msg))
print()

# String Methods
print(type(msg))
print(id(msg))
# Content test methods
print(msg.isalpha())
print(msg.isdigit())
print(msg.isalnum())
print(msg.islower())
print(msg.isupper())
print(msg.startswith('S'))
print(msg.endswith('l'))
# content search methods
print(msg.find('v'))
print(msg.replace('v', 'b'))
print(msg.count('v'))
print(msg.center(20, "_"))
# trims whitespace
print(msg.lstrip())
print(msg.rstrip())
print(msg.strip())
# split and partition
print(msg.split('v'))
print(msg.partition("valTrans"))
# join
string1 = "_".join(msg)
print(string1)
print()

# String Conversion
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(msg.swapcase())
print()

# Conversion
num = "45"
print(int(num))
print(float(num))
print(str(num))
print(complex(num))
print(ord('A'))
print(chr(65))
print(ord("Z"))


