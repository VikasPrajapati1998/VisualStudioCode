
from numpy import *  # this is already define in numpy so if you don't want import again not any problem.

m = matrix('1,2,3 ; 4,1,,5 ; 6,7,1')
print(m)
print('Maximum Value = ', m.max())
print('Minimum Value = ', m.min())
print('Diagonal Elements = ', diagonal(m))
print('Address = ', id(m))
print(m.dtype)
