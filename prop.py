from math import *
import sys

def parse_args(args):
	args.append(' ')
	g = {'plar':plar,'plsr':plsr,'pigeonnier':pigeonnier\
	,'csr':csr,'pourcentage':pourcentage,'binomial':binomial}
	equation = ""
	if args[0] in ('plar','plsr','csr'):
		for c, item in enumerate(args[:]):
			if item in ['+','*','/','-',' ']:
				#Probleme ici avec les args coupé donc certain cais
				#il en faut 2 et parfois 3 ...
				print(args)
				equation += str(g[args[0]](*[args[c - 2], args[c - 1]])) + item
		a = eval(equation)
	else:
		a = g[args[0]](*args[1:])
	return a

def binomial(*args):
	print(args)
	if len(args[0]) != 1:


	else:
		x, n, p = int(args[0]), int(args[1]), float(args[2])
		a = _bi(x,n,p)
	return a
def _bi(x,n,p):
	return round(csr(*[n,x]) * p**x * (1-p)**(n-x),3)


def plar(*args):
	#Placement lineaire avec repetition
	a, g = list(args), 1
	for o in range(2,len(a)):
		g = g * factorial(int(a[o]))
	return factorial(int(a[1]))/g

def plsr(*args):
	#placement lineaire sans repetition
	return factorial(int(args[1]))

def csr(*args):
	#combinaison sans repetitions de r objets choisis parmi n objets
	n, r = int(args[0]), int(args[1])
	return factorial(n)/(factorial(r) * factorial(n-r))

def smallestfraction(*args):
	pass

def pourcentage(*args):
	n, d = int(args[1]), int(args[2])
	return round(n*100/d, 2)

def pigeonnier(*args):
	oeufs, nids, contrainte = int(args[1]),int(args[2]),int(args[3])
	m=1
	retour = [False,0]
	while m < oeufs:
		if oeufs > m * nids and m < contrainte:
			retour[0], retour[1] = True, m + 1
		if (m+1) > contrainte:
			retour[0] = False
			break 
		m += 1
	return tuple(retour)

a = [sys.argv[i] for i in range(1,len(sys.argv))]
print(parse_args(a))
#print(a)
#g = {'plar':plar,'plsr':plsr,'pigeonnier':pigeonnier,'csr':csr,'pourcentage':pourcentage}
#print(g[a[0]](*a)) if g.__contains__(a[0]) else print('premiere argv invalide')