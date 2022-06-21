import FreeCAD, FreeCADGui, Part, math, os
path_ui = str(os.path.dirname(__file__))+'/RecuarParedeGui.ui'

class RecuarParede():
	def __init__(self):
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

		self.ferramenta(num)
		FreeCADGui.Control.closeDialog()


	def ferramenta(self, num):
		#ferramenta que estende uma parede até a outra parede perpendicular
		#pega a lista dos objetos celecionados
		lista = Gui.Selection.getSelection()

		#Pega o objeto base das paredes
		base1 = lista[0].Base
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
				linha1[0][1] -= abs(num)
			elif num > 0 and linha1[0][1] < linha1[1][1]:
				linha1[1][1] -= abs(num)
			elif num < 0 and linha1[0][1] > linha1[1][1]:
				linha1[1][1] +=  abs(num)
			elif num < 0 and linha1[0][1] < linha1[1][1]:
				linha1[0][1] +=  abs(num)
			
		elif abs(linha1[0][1] - linha1[1][1]) < 1: # paralelo ao eixo x
			if num > 0 and linha1[0][0] > linha1[1][0]:
				linha1[0][0] -=  abs(num)
			elif num > 0 and linha1[0][0] < linha1[1][0]:
				linha1[1][0] -=  num
			elif num < 0 and linha1[0][0] > linha1[1][0]:
				linha1[1][0] +=  abs(num)
			elif num < 0 and linha1[0][0] < linha1[1][0]:
				linha1[0][0] +=  abs(num)

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

		#Apagando a parede original
		doc.removeObject(lista[0].Name)
		doc.removeObject(base1.Name)
		doc.recompute()



painel = RecuarParede()
FreeCADGui.Control.showDialog(painel)