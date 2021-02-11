import numpy as np
from ace_cream import ace_cream
# the wechat data file found in computer folder
# please change the hash name to whatever you want
f = open('build/00b83e5eca94f72bebad3731b31dda34.dat','rb')
st = f.read()
y = np.frombuffer(st, dtype=np.uint8)
# save the sent image explicitly (manually)
f = open('build/00b83e5eca94f72bebad3731b31dda34.jpg','rb')
st = f.read()
x = np.frombuffer(st, dtype=np.uint8)
x = x.astype(np.float)
y = y.astype(np.float)
print(np.corrcoef(x, y)[0, 1])
tx, ty = ace_cream(x, y)
print(np.corrcoef(tx[:, 0], ty[:, 0])[0, 1])
'''
Results:

0.6345836370014625
0.9815445596270364
'''