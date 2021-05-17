# TOC: Esercizi matrici 
'''
	1. esrigaf(mat,i) : ritorna la i-esima riga
		1.a. con FOR
		1.b. con RANGE
		1.c. con SLICE
		1.d. con LIST COMPREHENSION
	1. escolf(mat,i) : ritorna la i-esima colonna
'''
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# 1) ESERCIZIO: Implementa la funzione esrigaf, che RITORNA la i-esima riga da mat

# def esrigaf(mat, i):
#   riga = mat
#   return riga[i]
#   print("Prova",mat[i])
#   return mat[i]

# # RISOLUZIONE con FOR
# def esrigaf(mat, i):
#     riga = []
#     for x in mat[i]:
#         riga.append(x)
#     return riga

# # RISOLUZIONE con RANGE
# def esrigaf(mat, i):
#     riga = []
#     for j in range(len(mat[0])):
#         riga.append(mat[i][j])
#     return riga


# # RISOLUZIONE con SLICE
#return mat[i][:]
# def esrigaf(mat, i):
#     riga = []
# #    riga.append(riga.slice(0,len(mat[i])))
#     return riga
# print(len(m[0]))
# x = slice(1,len(m[1]),len(m[1]))
# print(m[x])
# print(type(m[0]))


# # # RISOLUZIONE con LIST COMPREHENSION
# def esrigaf(mat, i):
#      return [x for x in mat[i]]

# m = [ ['a','b'],
#       ['c','d'],
#       ['a','e'] ]




# assert esrigaf(m, 0) == ['a','b']
# assert esrigaf(m, 1) == ['c','d']
# assert esrigaf(m, 2) == ['a','e']

# # controlla che non abbia cambiato la matrice originale!
# r = esrigaf(m, 0)
# r[0] = 'z'
# assert m[0][0] == 'a'

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# ESERCIZIO 2: colonna
# def escolf(mat, j):
# 	colonna = []
# 	for i in range(len(mat)):
# 		colonna.append(mat[i][j])
# 		#print(colonna)
# 	return colonna
	
# 	#   raise Exception('TODO IMPLEMENT ME !')

# m = [ ['a','b'],
#       ['c','d'],
#       ['a','e'] ]

# aa = escolf(m, 0)
# print(aa)
# assert escolf(m, 0) == ['a','c','a']
# assert escolf(m, 1) == ['b','d','e']

# # Controlla che la colonna ritornata non modifichi m
# c = escolf(m,0)
# c[0] = 'z'
# assert m[0][0] == 'a'

# # togli il commento se vuoi visualizzare l'esecuzione qui
# #jupman.pytut()

# def escolf(mat, j):
# 	return [x[j] for x in mat]
	
# 	#   raise Exception('TODO IMPLEMENT ME !')

# m = [ ['a','b'],
#       ['c','d'],
#       ['a','e'] ]

# aa = escolf(m, 0)
# print(m[0][0])

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# ESERCIZIO 3: matrici vuote

# def matrice_vuota(n, m):
# 	temp = []
# 	for i in range(0,n):
# 		print("i",i)
# 		temp.append(0)
# 		print(temp)
# 		for j in range(0,m):
# 			print("j",j)
# 			temp.append(0)
# 			print(temp)
# #			temp[i][j] = 0
# 			print(temp) 
# 	return temp

# #   raise Exception('TODO IMPLEMENT ME !')
# # def matrice_vuota(n, m):
# # 	temp = []
# # 	for i in range(0,n):
# # 		riga = []
# # 		print("riga i",i)
# # 		temp.append(riga)
# # 		print(temp)
# # 		for j in range(0,m):
# # 			print("j",j)
# # 			riga.append(0)
# # 			print(temp) 
# # 	return temp

# prova = matrice_vuota(2,2)
# print(prova)
# assert matrice_vuota(1,1) == [ [0] ]

# assert matrice_vuota(1,2) == [ [0,0] ]

# assert matrice_vuota(2,1) == [ [0],
#                                [0] ]

# assert matrice_vuota(2,2) == [ [0,0],
#                                [0,0] ]

# assert matrice_vuota(3,3) == [ [0,0,0],
#                                [0,0,0],
#                                [0,0,0] ]