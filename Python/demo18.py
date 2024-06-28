lst = ["Shubha", "Nisha", "Sudha", ('Suresh',), ('Rajesh',), 'Radha']
tpl = (10,)
print(tpl, type(tpl))

boys = 0
girls = 0

for ele in lst:
    if isinstance(ele, tuple):
        boys += 1
    else:
        girls += 1

print('Boys = ', boys, 'Girls = ', girls)
       


