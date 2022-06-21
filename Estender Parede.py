import FreeCAD, FreeCADGui, Part, math, os
path_ui = str(os.path.dirname(__file__))+'/EstenderParedeGui.ui'

class EstendeParede():
	def __init__(self, lista):
		self.lista  = lista
		# Carrega a GUI
		self.form = FreeCADGui.PySideUic.loadUi(path_ui)

		#Define a função do botão ok
		self.form.btn_ok.clicked.connect(self.accept)


		

	def accept(self):
		try:
			num = float(self.form.entrada.text())
			
		except:
			print('O valor da distancia é inválido.')
			FreeCADGui.Control.closeDialog()

		self.ferramenta1(num)
		FreeCADGui.Control.closeDialog()


	def ferramenta1(self, num):
		#Pega o objeto base das paredes
		base1 = self.lista[0].Base
		#pegando as coodenadas das linhas 
		linha1 = [base1.Geometry[0].StartPoint, base1.Geometry[0].EndPoint]

		#Ajustando as coordenadas do elemento devido ao ao deslocamento do mesmo (Placment)
		linha1[0][0] += base1.Placement.Base[0]
		linha1[0][1] += base1.Placement.Base[1]
		linha1[0][2] += base1.Placement.Base[2]
		linha1[1][0] += base1.Placement.Base[0]
		linha1[1][1] += base1.Placement.Base[1]
		linha1[1][2] += base1.Placement.Base[2]


		if abs(linha1[0][0] - linha1[1][0]) < 1: # paralelo ao eixo y
			if num > 0 and linha1[0][1] > linha1[1][1]:
				linha1[0][1] += abs(num)
			elif num > 0 and linha1[0][1] < linha1[1][1]:
				linha1[1][1] += abs(num)
			elif num < 0 and linha1[0][1] > linha1[1][1]:
				linha1[1][1] -=  abs(num)
			elif num < 0 and linha1[0][1] < linha1[1][1]:
				linha1[0][1] -=  abs(num)
			
		elif abs(linha1[0][1] - linha1[1][1]) < 1: # paralelo ao eixo x
			if num > 0 and linha1[0][0] > linha1[1][0]:
				linha1[0][0] +=  abs(num)
			elif num > 0 and linha1[0][0] < linha1[1][0]:
				linha1[1][0] +=  num
			elif num < 0 and linha1[0][0] > linha1[1][0]:
				linha1[1][0] -=  abs(num)
			elif num < 0 and linha1[0][0] < linha1[1][0]:
				linha1[0][0] -=  abs(num)

		#Cria um Sketcher
		doc = App.ActiveDocument
		sketch1 = doc.addObject("Sketcher::SketchObject", "Sketch")
		sketch1.addGeometry(Part.LineSegment(App.Vector(linha1[0][0],linha1[0][1],0),App.Vector(linha1[1][0],linha1[1][1],0)), False)
		
		#Criando as paredes
		parede1 = Arch.makeWall(sketch1, length=None, width=self.lista[0].Width, height=self.lista[0].Height, align = self.lista[0].Align)

		#copia as propriedades de bloco das paredes antigas para as novas paredes
		parede1.BlockHeight = self.lista[0].BlockHeight
		parede1.BlockLength = self.lista[0].BlockLength
		parede1.Joint = self.lista[0].Joint
		parede1.MakeBlocks = self.lista[0].MakeBlocks
		parede1.OffsetFirst = self.lista[0].OffsetFirst
		parede1.OffsetSecond = self.lista[0].OffsetSecond
		parede1.MoveBase = True

		#Apagando a parede original
		doc.removeObject(self.lista[0].Name)
		doc.removeObject(base1.Name)
		doc.recompute()


	
def ferramenta2(lista):
	#Pega o objeto base das paredes
	base1 = lista[0].Base
	base2 = lista[1].Base
	
	#pegando as coodenadas das linhas 
	linha1 = [base1.Geometry[0].StartPoint, base1.Geometry[0].EndPoint]
	linha2 = [base2.Geometry[0].StartPoint, base2.Geometry[0].EndPoint]
	
	#Ajustando as coordenadas do elemento devido ao ao deslocamento do mesmo (Placment)
	linha1[0][0] += base1.Placement.Base[0]
	linha1[0][1] += base1.Placement.Base[1]
	linha1[0][2] += base1.Placement.Base[2]
	linha1[1][0] += base1.Placement.Base[0]
	linha1[1][1] += base1.Placement.Base[1]
	linha1[1][2] += base1.Placement.Base[2]
	
	linha2[0][0] += base2.Placement.Base[0]
	linha2[0][1] += base2.Placement.Base[1]
	linha2[0][2] += base2.Placement.Base[2]
	linha2[1][0] += base2.Placement.Base[0]
	linha2[1][1] += base2.Placement.Base[1]
	linha2[1][2] += base2.Placement.Base[2]

	#Analiza se a linha 2 está paralela a x ou a y e estende a linha 1 até a linha 2
	if abs(linha2[0][0] - linha2[1][0]) < 1: # paralelo ao eixo y
		xref = linha2[0][0]
		if abs(linha1[0][0] - xref) < abs(linha1[1][0] - xref):
			linha1[0][0] = xref
		else:
			linha1[1][0] = xref	
	elif abs(linha2[0][1] - linha2[1][1]) < 1: # paralelo ao eixo x
		yref = linha2[0][1]
		if abs(linha1[0][1] - yref) < abs(linha1[1][1] - yref):
			linha1[0][1] = yref
		else:
			linha1[1][1] = yref	
	else:
		print('Erro ao estender a parede')
	
	#Muda altera o Sketch
	doc = App.ActiveDocument
	sketch1 = doc.addObject("Sketcher::SketchObject", "Sketch")
	sketch1.addGeometry(Part.LineSegment(App.Vector(linha1[0][0],linha1[0][1],0),App.Vector(linha1[1][0],linha1[1][1],0)), False)
	
	#Criando as paredes
	parede1 = Arch.makeWall(sketch1, length=None, width=lista[0].Width, height=lista[0].Height, align = lista[0].Align)

	#copia as propriedades de bloco das paredes antigas para as novas paredes
	parede1.BlockHeight = lista[0].BlockHeight
	parede1.BlockLength = lista[0].BlockLength
	parede1.Joint = lista[0].Joint
	parede1.MakeBlocks = lista[0].MakeBlocks
	parede1.OffsetFirst = lista[0].OffsetFirst
	parede1.OffsetSecond = lista[0].OffsetSecond
	parede1.MoveBase = True

	#Apagando a parede original
	doc.removeObject(lista[0].Name)
	doc.removeObject(base1.Name)
	doc.recompute()


#pega a lista dos objetos celecionados
lista = Gui.Selection.getSelection() # caso ele tiver com somente uma parede celecionada
if len(lista) <2:
	painel = EstendeParede(lista)
	FreeCADGui.Control.showDialog(painel) 

else:
	ferramenta2(lista)#caso ele tiver mais de uma parede celecionada




