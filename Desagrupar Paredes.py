lista  = App.ActiveDocument.Objects

for i in lista:
	try:	
		if i.IfcType == 'Wall':
			i.Additions = []
			i.Visibility = True
	except:
		pass
	