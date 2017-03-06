__author__ = "Sergio"

from flask import Flask, request, Response
import os
app = Flask("EDD_Practica2")

class Nodo():
	def __init__(self,dato):
		self.dato=dato 
		self.sig=None
		self.ant=None
		self.arriba=None
		self.abajo=None
		self.atras=None

	def getDato(self):
		return self.dato 

class NodoMatriz():

	def __init__(self,dato,sig,ant,arriba,abajo):
		self.dato=dato 
		self.sig=sig
		self.ant=ant
		self.arriba=arriba
		self.abajo=abajo

	def getDatos(self):
		return self.dato 

class ListaEnlazada(object):

	def __init__(self):
		self.first=None
		self.last=None
	def isEmpty(self):
		if self.first==None:
			return True
		else:
			return False
	def insertar(self, dato):
		nuevo=Nodo(dato)
		if self.isEmpty() == True:
			self.first=self.last=nuevo
		else:
			self.last.sig=nuevo
			self.last=nuevo

	def eliminar(self,ind):
		index=int(ind)
		contador=0
		nodotem=self.first
		nodotem2=self.first
		index=index-1

		while(contador<index):
			
			if contador== index:
				nodotem.sig=nodotem.sig.sig
				break
			pass
			nodotem=nodotem.sig
			contador=contador+1
		pass

	def extraer(self, indice):
		nodotem=self.first
		contad=0
		while (contad<indice and nodotem.sig!=None):
			nodotem=nodotem.sig
			contad=contad+1
			pass
		
		if indice>self.getSize():
			return None
		if nodotem==None:
			return "Ya no hay datos"
			pass
		return nodotem.getDato()

	def getSize(self):
		contador=0
		temp=self.first
		while(temp!=None):
			temp=temp.sig
			contador=contador+1
		pass
		return contador


	def buscar(self, cadena):
		notem=self.first
		cont=0
		for x in xrange(0,self.getSize()):
			if notem.getDato()==cadena:
				return "Indice "+ str(x)
				break
			notem=notem.sig
			pass
		return "No se encontro"

class Cola(object):
	
	def __init__(self):
		self.first=None
		self.last=None

	def isEmpty(self):
		if self.first==None:
			return True
		else:
			return False

	def archivoCola(self):
		ax=self.first
		ls=ListaEnlazada()
		mat=Matriz()
		while(ax!=None):
			ls.insertar(ax.getDato())
			ax=ax.sig
			pass
		mat.crearArchivo(ls,"cola.dot","cola.png")
		pass
	

	def insertar(self, dato):
		nuevo=Nodo(dato)
		if self.isEmpty() == True:
			self.first=self.last=nuevo
		else:
			self.last.sig=nuevo
			self.last=nuevo

	def extraer(self):
		if self.isEmpty()!=False:
			return "Ya no hay datos en la Cola"
		else:
			te=self.first
			self.first=self.first.sig
			return te.getDato()
					

class Pila(object):

	def __init__(self):
		self.first=None
		self.last=None

	def isEmpty(self):
		if self.first==None:
			return True
		else:
			return False

	def archivoPila(self):
		ax=self.first
		ls=ListaEnlazada()
		mat=Matriz()
		while(ax!=None):
			ls.insertar(ax.getDato())
			ax=ax.sig
			pass
		mat.crearArchivo(ls,"pila.dot","pila.png")
		pass

	def insertar(self, dato):
		nuevo=Nodo(dato)
		if self.isEmpty() == True:
			self.first=self.last=nuevo
		else:
			nuevo.sig=self.first
			self.first=nuevo

	def getSize(self):
		contador=0
		temp=self.first
		while(temp!=None):
			temp=temp.sig
			contador=contador+1
		pass
		return contador

	def lastPush():
		if self.first!=None:
			return self.first.getDato()
		else:
			return None
	
	def extraer(self):
		if self.isEmpty()!=False:
			return None
		else:
			te=self.first
			self.first=self.first.sig
			return te.getDato()
			
	def imprimir():
		tempo=first
		while (tempo!=None):
			print(tempo.getDato())
			pass


class Matriz(object):
	def __init__(self):
		self.first=None
		self.last=None

	def inicializar(self):
		nuevo=Nodo("00")
		self.first=nuevo
		self.last=nuevo

	def existeFila(self, dato):
		auxfila=self.first
		while (auxfila!=None):
			print "columna "+auxfila.getDato()
			if(auxfila.getDato()==dato):
				return True
				break
			auxfila=auxfila.abajo
			pass
		return False

	def existeCol(self,dato):
		auxcol=self.first
		while (auxcol!=None):
			print "FILA "+auxcol.getDato()
			if(auxcol.getDato()==dato):
				return True
				break
			auxcol=auxcol.sig
			pass
		return False


	def printCol(self):
		axc=self.first
		while (axc!=None):
			print axc.getDato()
			axc=axc.sig
			pass
	def printFil(self):
		axc=self.first
		while (axc!=None):
			print axc.getDato()
			axc=axc.abajo
			pass
	def printDatosFila(self):
		axc=self.first
		axc2=self.first
		axc=axc.abajo
		axc2=axc2.abajo
		axc3=axc2

		while (axc!=None):
			#print axc.getDato()
			while (axc2!=None):
				print axc2.getDato()
				axc3=axc2.atras
				while(axc3!=None):
					print axc3.getDato()
					axc3=axc3.atras
					pass
				axc2=axc2.sig
				axc3=axc2
				pass
			axc=axc.abajo
			axc2=axc
			axc3=axc
			pass
	def BuscarDatosFila(self, buscar):
		axc=self.first
		axc2=self.first
		axc=axc.abajo
		axc2=axc2.abajo
		axc3=axc2
		filaData=""
		lis=ListaEnlazada()
		while (axc!=None):
			#print axc.getDato()
			if axc2!=None and buscar==axc2.getDato():
				while (axc2!=None):	
					filaData=filaData+axc2.getDato()+", "
					lis.insertar(axc2.getDato())
					print axc2.getDato()
					axc3=axc2.atras
					while(axc3!=None):
						print axc3.getDato()
						filaData=filaData+" , "+axc3.getDato()
						lis.insertar(axc3.getDato())
						axc3=axc3.atras
					pass
					axc2=axc2.sig
					axc3=axc2
				pass
			pass
			axc=axc.abajo
			axc2=axc
			axc3=axc
		pass
		self.crearArchivo(lis,"filaMatriz.dot","filaMatriz.png")
		return "Resultado: "+filaData

	def crearArchivo(self,lista,nombre,nimage):
		archivoDot="digraph grafo{ \n"
		cont=0
		while cont<lista.getSize()-1:
			archivoDot=archivoDot+lista.extraer(cont)+"->"+lista.extraer(cont+1)+"; \n"
			cont=cont+1
			pass
		archivoDot=archivoDot+"\n }"
		try:
			arch=open("C:\graphviz-2.38\\release\EDD\\"+nombre,"w")
			arch.write(archivoDot)
			arch.close()
			os.system('C:\graphviz-2.38\\release\\bin\dot.exe -Tpng C:\graphviz-2.38\\release\EDD\\'+nombre+' -o C:\graphviz-2.38\\release\EDD\\'+nimage)
			pass
		except Exception as e:
			raise e
	
	def printDatosCol(self):
		axc=self.first
		axc2=self.first
		axc=axc.sig
		axc2=axc2.sig
		axc3=axc2

		while (axc!=None):
			#print axc.getDato()
			while (axc2!=None):
				print axc2.getDato()
				axc3=axc2.atras
				while(axc3!=None):
					print axc3.getDato()
					axc3=axc3.atras
					pass
				axc2=axc2.abajo
				axc3=axc2
				pass
			axc=axc.sig
			axc2=axc
			axc3=axc
			pass

	def dominioBuscar(self, dom):
		axc=self.first
		axc2=self.first
		axc=axc.sig
		axc2=axc2.sig
		axc3=axc2
		colData=""
		lisdom=ListaEnlazada()
		indice=0
		while (axc!=None):
			#print axc.getDato()
			if axc2!=None and dom==axc2.getDato():
				while (axc2!=None):
						
						if indice==0:
							colData=colData+axc2.getDato()+", "
							sinC=self.quitarArroba(axc2.getDato())
							lisdom.insertar(sinC)
							indice=indice+1
							pass	
						else:
							colData=colData+" , "+axc2.getDato()
							lisdom.insertar(axc2.getDato())
							axc3=axc2.atras
						pass
						axc3=axc2.atras
						while(axc3!=None):
							print "esta entrando aca"
							lisdom.insertar(axc3.getDato())
							colData= colData+" , "+axc3.getDato()
							axc3=axc3.atras
						pass
						axc2=axc2.abajo
						axc3=axc2
				pass
			pass
			axc=axc.sig
			axc2=axc
			axc3=axc
		pass
		self.crearArchivo(lisdom,"matrizCol.dot","matrizCol.png")
		return "Resultado: "+ colData

	def quitarArroba(sef, mailarr):
		cont=1
		sinA=""
		while cont<len(mailarr)-4:
			sinA=sinA+mailarr[cont]
			cont=cont+1
			pass
		return sinA
	def imprimir(self):
		self.head=self.first
		son=self.first
		ndata=self.first
		adata=self.first
		print "printing----"

		while self.head!=None:
			print "Cabecera"+ self.head.getDato()
			while son!=None:
				print "Hijo "+son.getDato()
				if ndata!=None:
					ndata=ndata.abajo
					adata=ndata
					while adata!=None:
						if adata.atras!=None:
							print "DATO TRAS "+ndata.atras.getDato()
							pass
						adata=adata.atras
						pass
					pass
				if ndata!=None:
					ndata=ndata.sig
					pass
				while ndata!=None:
					print "DATO "+ndata.getDato()
					ndata=ndata.sig
					pass
				son=son.abajo
				ndata=son
				pass
			self.head=self.head.sig
		pass

	def agregar(self, dato):
		mail=""
		nombre=""
		"""Nombre de correo"""
		for x in xrange(0,len(dato)):
			nombre=nombre+dato[x]
			if dato[x+1]=='@':
				x=x+1
				while (x<len(dato)):
					mail=mail+dato[x]
					x=x+1
				pass
				break	
		pass
		
		print dato + " "+nombre+" "+mail

		self.colAux=self.filAux=self.filAux2=self.colAux2=self.first
		
		if self.first.sig==None and self.first.abajo==None:
			
			filaN=Nodo(dato[0])
			colN=Nodo(mail)
			dataN=Nodo(nombre)

			self.first.sig=colN
			colN.ant=self.first

			self.first.abajo=filaN
			filaN.arriba=self.first

			colN.abajo=dataN
			dataN.arriba=colN
			filaN.sig=dataN
			dataN.ant=filaN
			pass
		elif self.existeCol(mail)==True and self.existeFila(dato[0])==True:
			print "EXISTE COLUMNA, EXISTE FILA"
			self.colAux=self.filAux=self.filAux2=self.colAux2=self.first

			while(self.filAux2!=None):
				
				if self.filAux2.getDato()==dato[0]:
					print "filAux2 VALOR: y dato "+self.filAux2.getDato()+" "+dato[0]	
					self.filAux2=self.filAux2.sig
					while self.filAux2!=None:
						
						if self.filAux2.getDato()[0]==nombre[0]:
							
							datoN=Nodo(nombre)
							
							while (self.filAux2.atras!=None):
								self.filAux2=self.filAux2.atras
							pass
							datoN.atras=None
							self.filAux2.atras=datoN
							datoN.delante = self.filAux2
							break
							pass

						self.filAux2=self.filAux2.sig
					pass
				pass
				self.filAux2=self.filAux2.abajo
				
			pass

		elif self.existeCol(mail)==True and self.existeFila(dato[0])==False:
			print "EXISTE COLUMNA, NO EXISTE FILA"
			self.colAux=self.filAux=self.filAux2=self.colAux2=self.first

			while(self.colAux!=None):
				
				if(self.colAux.getDato()==mail):
					
					while self.filAux.getDato()[0]<dato[0]:
						if self.colAux.abajo!=None:
							self.colAux=self.colAux.abajo
						self.filAux=self.filAux.abajo
						pass
					
						filaN=Nodo(dato[0])#Creacion encabezado de fila
						filaN.arriba=self.filAux
						self.filAux.abajo=filaN

						datoN=Nodo(nombre) #Creacion de nombre
						datoN.ant=filaN
						filaN.sig=datoN

						self.colAux.abajo=datoN
						datoN.arriba=self.colAux
					break
				self.colAux=self.colAux.sig
			pass
		elif self.existeCol(mail)==False and self.existeFila(dato[0])==True:
			print "NO EXISTE COLUMNA, EXISTE FILA"
			self.colAux=self.filAux=self.filAux2=self.colAux2=self.first
			while(self.filAux!=None):
				"""Si la inicial es igual al de la cabecera fila"""
				if self.filAux.getDato()[0]==dato[0]:
						print "fila == dato[0]"
						while self.colAux.getDato()[0]<dato[0]:
							if self.colAux.sig!=None:
								self.colAux=self.colAux.sig
								if self.filAux.sig!=None:
									self.filAux=self.filAux.sig
							else:
								break
							pass
						columna=Nodo(mail) #Creacion Nueva Columna
						columna.ant=self.colAux.ant
						self.colAux.ant.sig=columna

						columna.sig=self.colAux
						self.colAux.ant=columna
						#columna.ant=colAux.ant.ant

						datoN=Nodo(nombre) #Creacion de nodo nombre
						datoN.ant=self.filAux.ant
						self.filAux.ant.sig=datoN

						datoN.sig=self.filAux
						self.filAux.ant=datoN

						columna.abajo=datoN
						datoN.arriba=columna
						break
				self.filAux=self.filAux.abajo
				pass
		elif self.existeCol(mail)==False and self.existeFila(dato[0])==False:
				self.colAux=self.filAux=self.filAux2=self.colAux2=self.first
				print "NO EXISTE COLUMNA, NO EXISTE FILA"
				while(self.filAux!=None):
					"""Si la inicial es igual al de la cabecera fila"""
					if self.filAux.getDato()[0]>=dato[0] or self.filAux.abajo==None:
						while ord(self.colAux.getDato()[1])<ord(mail[1]) and self.colAux.sig!=None:
							self.colAux=self.colAux.sig	
						pass

						self.columna=Nodo(mail) #Creacion Nueva Columna
						self.colAux.sig=self.columna
						self.columna.ant=self.colAux
						self.columna.sig=self.colAux.sig.sig
							
						filaN=Nodo(dato[0])
						filaN.arriba=self.filAux
						
						if self.filAux.abajo!=None:
							filaN.abajo=self.filAux.abajo
							pass
						self.filAux.abajo=filaN
						
						datoN=Nodo(nombre) #Creacion de nodo nombre
						filaN.sig=datoN
						datoN.ant=filaN
							
						self.columna.abajo=datoN
						datoN.arriba=self.columna
						break

					self.filAux=self.filAux.abajo
					print self.filAux.abajo
				pass
		



""" LISTA ENLAZADA """
@app.route('/lista',methods=['POST'])
def addLista():
	par= str(request.form['agregar'])
	ls.insertar(par)
	m.crearArchivo(ls,"listaenl.dot","listaenl.png")
	return "Added"

@app.route('/lista/buscar',methods=['POST'])
def buscarL():	
	parb= str(request.form['buscar'])
	m.crearArchivo(ls,"listaenl.dot","listaenl.png")
	return ls.buscar(parb) 

@app.route('/lista/eliminar',methods=['POST'])
def eliminarL():
	pare= str(request.form['eliminar'])
	ls.eliminar(pare)
	m.crearArchivo(ls,"listaenl.dot","listaenl.png")
	return "Eliminado" 
"""PILA"""
@app.route('/pila',methods=['POST'])
def addPila():
	par= str(request.form['add'])
	p.insertar(par)
	p.archivoPila()
	return "Added"

@app.route('/pop',methods=['POST'])
def pop():
	par= str(request.form['pop'])
	pop=p.extraer()
	p.archivoPila()
	return "POP: "+pop 

"""COLA"""
@app.route('/cola',methods=['POST'])
def addCola():
	par= str(request.form['addC'])
	c.insertar(par)
	c.archivoCola()
	return "Added"

@app.route('/dequeue',methods=['POST'])
def dequeue():
	par= str(request.form['deq'])
	var=c.extraer()
	c.archivoCola()
	return "DEQUEUE: "+var 

"""MATRIZ"""
@app.route('/addmatriz',methods=['POST'])
def addMatrz():
	par=str(request.form['dato'])
	m.agregar(par)
	return "Added"

@app.route('/buscarletra',methods=['POST'])
def buscarLetter():
	par= str(request.form['bl'])
	return m.BuscarDatosFila(par) 

@app.route('/buscardom',methods=['POST'])
def buscarDom():
	par= str(request.form['dm'])
	
	return m.dominioBuscar(par)


""""""
@app.route("/")
def say():
	return "Hello"

if __name__ == "__main__":
 ls=ListaEnlazada()
 p=Pila()
 c=Cola()
 m=Matriz()
 m.inicializar()
 app.run()

