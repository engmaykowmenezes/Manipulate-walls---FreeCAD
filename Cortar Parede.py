#ferramenta que corta o primeiro elemento criando outros dosi elementos de parede

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

#linhas a serem criadas
linha3 = []
linha4 = []
#Analiza se a linha 2 está paralela a x ou a y  e cria as linhas 3 e 4
if abs(linha2[0][0] - linha2[1][0]) < 1: # paralelo ao eixo y
	xref = linha2[0][0]
	linha3 = [(linha1[0][0],linha1[0][1],0),(xref,linha1[0][1],0)]
	linha4 = [(xref ,linha1[1][1],0),(linha1[1][0],linha1[1][1],0)]
elif abs(linha2[0][1] - linha2[1][1]) < 1: # paralelo ao eixo x
	yref = linha2[0][1]
	linha3 = [(linha1[0][0],linha1[0][1],0),(linha1[0][0],yref,0)]
	linha4 = [(linha1[1][0],yref,0),(linha1[1][0],linha1[1][1],0)]
else:
	print('Erro ao cortar a parede')
	print(linha1)
	print(linha2)

# Crias os Skets 
doc = App.ActiveDocument
sketch1 = doc.addObject("Sketcher::SketchObject", "Sketch")
sketch1.addGeometry(Part.LineSegment(App.Vector(linha3[0][0],linha3[0][1],0),App.Vector(linha3[1][0],linha3[1][1],0)), False)

sketch2 = doc.addObject("Sketcher::SketchObject", "Sketch")
sketch2.addGeometry(Part.LineSegment(App.Vector(linha4[0][0],linha4[0][1],0),App.Vector(linha4[1][0],linha4[1][1],0)), False)

#Criando as paredes
parede1 = Arch.makeWall(sketch1, length=None, width=lista[0].Width, height=lista[0].Height, align = lista[0].Align)
parede2 = Arch.makeWall(sketch2, length=None, width=lista[0].Width, height=lista[0].Height, align = lista[0].Align)

#copia as propriedades de bloco das paredes antigas para as novas paredes
parede1.BlockHeight = lista[0].BlockHeight
parede1.BlockLength = lista[0].BlockLength
parede1.Joint = lista[0].Joint
parede1.MakeBlocks = lista[0].MakeBlocks
parede1.OffsetFirst = lista[0].OffsetFirst
parede1.OffsetSecond = lista[0].OffsetSecond

parede2.BlockHeight = lista[0].BlockHeight
parede2.BlockLength = lista[0].BlockLength
parede2.Joint = lista[0].Joint
parede2.MakeBlocks = lista[0].MakeBlocks
parede2.OffsetFirst = lista[0].OffsetFirst
parede2.OffsetSecond = lista[0].OffsetSecond


#Apagando a parede original
doc.removeObject(lista[0].Name)
doc.removeObject(base1.Name)
doc.recompute()
