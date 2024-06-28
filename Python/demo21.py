s = {'gate', 'fate', 'late'}
s.add('rate')
print(s)

f = frozenset({'gate', 'fate', 'late'})
try:
    f.add('rate') # error
    print()
except Exception as e:
    print(e)



