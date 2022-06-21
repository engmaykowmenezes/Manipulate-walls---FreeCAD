import FreeCAD, FreeCADGui, Part, math, os

path_ui = str(os.path.dirname(__file__))+'/DistanciaparedeGui.ui'

class DistParedes:
	def __init__(self):
		# Carrega a GUI
		self.form = FreeCADGui.PySideUic.loadUi(path_ui)

		#Define a função do botão ok
		self.form.btn_ok.clicked.connect(self.accept)

	def accept(self):
		try:
			dist = float(self.form.entrada.text())
		except:
			print('O valor da distancia é inválido.')
		self.ferramenta(dist)
		FreeCADGui.Control.closeDialog()

	def ferramenta(self,dist):
		# pega a lista dos objetos celecionados
		lista = Gui.Selection.getSelection()

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

		#pega a distancia entre as paredes
		

		#Analiza se a linha 2 está paralela a x ou a y  e cria as linhas 3 e 4
		if abs(linha2[0][0] - linha2[1][0]) < 1: # paralelo ao eixo y
			xref2 = linha2[0][0]
			if linha1[0][0] > xref2:
				linha1[0][0] = xref2 + dist
				linha1[1][0] = xref2 + dist
			else:
				linha1[0][0] = xref2 - dist
				linha1[1][0] = xref2 - dist
				
				
			
		elif abs(linha2[0][1] - linha2[1][1]) < 1: # paralelo ao eixo x
			yref2 = linha2[0][1]
			if linha1[0][1] > yref2:
				linha1[0][1] = yref2 + dist
				linha1[1][1] = yref2 + dist
			else:
				linha1[0][1] = yref2- dist
				linha1[1][1] = yref2 - dist
			
		else:
			print('Erro ao distanciar parede.')
			print(linha1)
			print(linha2)

		#Crias os Skets 
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

painel = DistParedes()
FreeCADGui.Control.showDialog(painel) 