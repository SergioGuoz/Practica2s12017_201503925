class Nodo():

	def __init__(self,dato):
		self.dato=dato 
		self.sig=None
		self.ant=None
		self.arriba=None
		self.abajo=None

	def getDato(self):
		return self.dato 

class NodoMatriz():

	def __init__(self,dato,sig,ant,arriba,abajo):
		self.dato=dato 
		self.sig=sig
		self.ant=ant
		self.arriba=arriba
		self.abajo=abajo

	def getDato(self):
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

	def eliminar(self,index):
		contador=0
		nodotem=self.first
		nodotem2=self.first
		index=index-1

		while(contador<index):
			
			if contador== index:
				print "Entra"
				nodotem.sig=nodotem.sig.sig
				break
				pass
			print "no"
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
				return x
				break
			notem=notem.sig
			pass

class Cola(object):
	
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

	def extraer(self):
		if self.isEmpty()!=False:
			return None
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
		nuevo=Nodo(0)
		self.first=nuevo
		self.last=nuevo

	def existeCol(self, dato):
		auxfila=self.first
		while (auxfila!=None):
			if(auxfila.getDato()==dato):
				return True
				break
			auxfila=auxfila.sig
			pass
		return False
	def existeFila(self,dato):
		auxcol=self.first
		while (auxcol!=None):
			if(auxcol.getDato()==dato):
				return True
				break
			auxcol=auxcol.sig
			pass
		return False

	def agregar(self, dato):
		mail=""
		nombre=""
		"""Nombre de correo"""
		for x in xrange(0,len(dato)):
			nombre=nombre+dato[x]

			if dato[x]=='@'
				while (x<len(dato)):
					mail=mail+dato[x]
					x=x+1
				pass	
		pass

		colAux=filAux=self.first
		
		nuevo=Nodo(nombre)

		if existeCol(mail)==True and existeFila(dato[0])==True:
			while(colAux.getDato()!=None):
				if(colAux.getDato()==dato):
					colAux=colAux.abajo
					while colAux.getDato()!=None:
						if colAux.getDato()==
						colAux=colAux.abajo
						pass
				colAux=colAux.sig	
			filAux=filAux.sig

		elif existeCol(mail)==True and existeFila(dato[0]==False):
			while(colAux.getDato()!=None):
				if(colAux.getDato()==dato):
					cont=0
						while filAux.getDato()[cont]>dato[cont]:
							if colAux.abajo!=None:
								colAux=colAux.abajo
							filAux=filAux.abajo
							pass

						fila=Nodo(dato[0])
						fila.arriba=filAux
						filAux.abajo=fila
						datoN=Nodo(nombre)
						colAux.abajo=datoN
						datoN.arriba=colAux
						fila.sig=datoN
						datoN.ant=fila

		elif existeCol(mail)==False and existeFila(dato[0]==True):
			while(filAux.getDato()!=None):
				if(filAux.getDato()==dato[0]):
					cont=0
					cont2=0
						while colAux.getDato()[cont]>dato[cont2]:
							if colAux.abajo!=None:
								colAux=colAux.abajo
							filAux=filAux.abajo
							cont2=cont2+1
							pass
						
						fila=Nodo(dato[0])
						fila.arriba=filAux
						filAux.abajo=fila
						datoN=Nodo(nombre)
						colAux.abajo=datoN
						datoN.arriba=colAux
						fila.sig=datoN
						datoN.ant=fila
						
		elif existeCol(mail)==False and existeFila(dato[0]==False):
			


		
class code(Pila):
	p=Pila()	
	p.insertar("Ingresado Primero")
	p.insertar("Ingresado Segundo")
	p.insertar("Ingresado Tercero")

	c=Cola()
	c.insertar("Cola 1")
	c.insertar("Cola 2")
	c.insertar("Cola 3")
	c.insertar("Cola 4")

	ls=ListaEnlazada()

	ls.insertar("LE1")
	ls.insertar("LE2")
	ls.insertar("LE3")

	while (p.isEmpty()==False):
		print p.extraer();
		pass
	
	while (c.isEmpty()==False):
		print c.extraer();
		pass
	print ls.extraer(0)
	print ls.extraer(1)
	print ls.extraer(2)
	print ls.buscar("LE1")	
	print ls.buscar("LE3")
	ls.eliminar(2)
	print ls.extraer(0)
	print ls.extraer(1)
	print ls.extraer(2)