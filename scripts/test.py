import labrad
import time
import numpy as np


cxn=labrad.connect()
dv=cxn.data_vault
dv.cd('')

paths = ['Ziyu','peach']
for path in paths:
	dv.cd(path)

dv.cd()



dv.new('Test_x_y22', [('freq', 'value')], [('z','Test-Spectrum','a.u.')])
dv.add_parameter('simu_eq22', ['ys=sin(xs)'])



xs = np.arange(0.,1001,1)
ys = np.sin(0.1*xs)

for i in range(len(xs)):
    
    x,y=xs[i],ys[i]
    print(i)
    data = [x,y**2]
    data = np.asarray(data)
    
    dv.add(data)
    time.sleep(0.1)

