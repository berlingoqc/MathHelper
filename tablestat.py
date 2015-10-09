from terminaltables import AsciiTable
from math import sqrt

class TableauProp(object):

	def __init__(self, dicta):
		#Recoit dictionnaire que la cle correspond au valeur de x et valeur a sa probabilité
		self.dict = dicta
		self.do_math()
		self.draw_table()

	def do_math(self):
		#Calcul l'esperance la variance
		# valeur : [ P(x=x), x * P(x=x), (x - u)^2, last one]
		tEsp = 0
		tProp = 0 
		for k,v in self.dict.items():
			k1 = int(k)
			t = k1*v
			tEsp += t
			tProp += v
			self.dict[k] = [str(v), str(round(t,2)),0,0]
		self.esperance = str(round(tEsp,2))
		self.total_prop = str(tProp)

		tVar = 0
		for k in self.dict.keys():
			k1 = int(k)
			var = (k1 - tEsp)**2
			tVar += var
			self.dict[k][2] = str(round(var,2))
			self.dict[k][3] = str(round(var * float(self.dict[k][1]),2))
		self.variance = str(round(tVar,2))
		self.ecart_type = str(round(sqrt(tVar),2))

	def draw_table(self):
		table = [['x','P(X=x)','x * P(X=x)', '(x - Moy(x))^2','Variance']]
		for k,v in self.dict.items():
			table.append([k]+v) 
		table.append(['Total', self.total_prop,self.esperance,'',self.variance])
		t = AsciiTable(table)
		print()
		print(t.table)
		print()
		print('Esperence : ', self.esperance)
		print('Variance : ', self.variance)
		print('Ecart-type : ', self.ecart_type)

TableauProp({'1':0.16,'2':0.16,'3':0.16,'4':0.16,'5':0.16,'45':0.16})

