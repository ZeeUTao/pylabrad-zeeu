cxn=labrad.connect()
dv=cxn.data_vault
dv.cd('')

paths = ['Ziyu','peach']
for path in paths:
	dv.cd(path)

dv.cd()