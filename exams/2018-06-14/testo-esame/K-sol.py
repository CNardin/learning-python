# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# Esercizio 1
# """
# Prende in input una lista con n numeri interi, e RITORNA una NUOVA lista che
# contiene n tuple ciascuna da due elementi. Ogni tupla contiene un numero
# preso dalla corrispondente posizione della lista di partenza, e il suo doppio.
# Per esempio:
# doppie([ 5, 3, 8])
# deve dare la nuova lista
# [(5,10), (3,6), (8,16)]
# """
# def doppie(lista):
# 	lista2x = []
# 	n = len(lista)
# 	print("-" * 25)
# 	print("list: ", lista, "length: ", n )
# 	lista2x = [(x,2*x) for x in lista]
# 	print(lista2x)
# 	print("-" * 25)
# 	return lista2x

# # INIZIO TEST - NON TOCCARE !
# assert doppie([]) == []
# assert doppie([3]) == [(3,6)]
# assert doppie([2,7]) == [(2,4),(7,14)]
# assert doppie([5,3,8]) == [(5,10), (3,6), (8,16)]
# # FINE TEST

# # -----------------------------------------------------------------------------------------------------
# # -----------------------------------------------------------------------------------------------------
# # Esercizio 2
# """
# Quando si analizza una frase, può essere utile processarla per rimuovere parole molto comuni, come
# gli articoli e le preposizioni:
# Per esempio:
# "un libro su Python per principianti"
# si può semplificare in
# "libro Python principianti"
# Le parole 'poco utili' vengono chiamate 'stopwords'. Questo processo è per esempio eseguito
# dai motori di ricerca per ridurre la complessità della stringa di input fornita dall'utente.
# Implementare una funzione che prende una stringa e RITORNA la stringa di input senza le
# stopwords
# SUGGERIMENTO 1: le stringhe in Python sono *immutabili* ! Per rimuovere le parole dovete
# creare una _nuova_ stringa a partire dalla stringa di partenza.
# SUGGERIMENTO 2: create una lista di parole così:
# lista = stringa.split(" ")
# SUGGERIMENTO 3: operate le opportune trasformazioni su lista, e poi costruite la stringa
# da restituire con " ".join(lista)
# """
# def nostop(stringa, stopwords):
# 	readstr = stringa.split(" ")
# 	print(readstr)

# 	for i in range(0,len(stopwords)):
# 		n = readstr.count(stopwords[i])
# 		word2remove=stopwords[i]
# 		print("Parola da rimuovere: \"",word2remove, "\" ",n," volte")

# 		for j in range(0,n):
# 			readstr.remove(word2remove)
# 			print(readstr)
# 			j =+ 1

# 	print("finale", " ".join(readstr))
# 	print("-" * 25)
# 	return " ".join(readstr)


# # INIZIO TEST - NON TOCCARE !
# assert nostop("un", ["un"]) == ""
# assert nostop("un", []) == "un"
# assert nostop("", []) == ""
# assert nostop("", ["un"]) == ""
# assert nostop("un libro", ["un"]) == "libro"
# assert nostop("un libro su Python", ["un","su"]) == "libro Python"
# assert nostop("un libro su Python per principianti", ["un","uno","il","su","per"]) == "libro Python principianti"
# # FINE TEST
# # -----------------------------------------------------------------------------------------------------
# # -----------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# Esercizio 3
"""
Restituisce un dizionario con n coppie chiave-valore, dove le chiavi sono
numeri interi da 1 a n incluso, e ad ogni chiave i è associata una lista di numeri
da 1 a i
NOTA: le chiavi sono *numeri interi*, NON stringhe !!!!!
Esempio:
dilist(3)
deve dare:
{
1:[1],
2:[1,2],
3:[1,2,3]
}
"""


def dilist(n):
# # scrivi qui
	diz = dict()
	for voce in range(1,n+1):
		diz[voce] = list(range(1,voce+1))
#		print("incremento diz;" , diz)
		
	print("Diz.: ", diz)
	print("-"*25)
	return diz 

#INIZIO TEST - NON TOCCARE !
assert dilist(0) == dict()
assert dilist(1) == {
1:[1]
}
assert dilist(2) == {
1:[1],
2:[1,2]
}
assert dilist(3) == {
1:[1],
2:[1,2],
3:[1,2,3]
}
# FINE TEST

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# Esercizio 4
import numpy as np
"""
RESTITUISCE una NUOVA matrice numpy che ha i numeri della matrice numpy
di input ruotati di una colonna.
Per ruotati intendiamo che:
- se un numero nella matrice di input si trova alla colonna j, nella matrice
di output si troverà alla colonna j+1 nella stessa riga.
- Se un numero si trova nell'ultima colonna, nella matrice di output
si troverà nella colonna zeresima.
Esempio:
Se abbiamo come input
np.array( [
[0,1,0],
[1,1,0],
[0,0,0],
[0,1,1]
])
Ci aspettiamo come output
np.array( [
[0,0,1],
[0,1,1],
[0,0,0],
[1,0,1]
])
"""
def matrot(matrice):
	raise Exception
# scrivi qui
# INIZIO TEST - NON TOCCARE !
m1 = np.array( [
[1]
])
mat_attesa1 = np.array( [
[1]
])
assert np.allclose(matrot(m1), mat_attesa1)
m2 = np.array( [
[0,1]
])
mat_attesa2 = np.array( [
[1,0]
])
assert np.allclose(matrot(m2), mat_attesa2)
m3 = np.array( [
[0,1,0]
])
mat_attesa3 = np.array(
[
[0,0,1]
])
assert np.allclose(matrot(m3), mat_attesa3)
m4 = np.array( [
[0,1,0],
[1,1,0]
])
mat_attesa4 = np.array( [
[0,0,1],
[0,1,1]
])
assert np.allclose(matrot(m4), mat_attesa4)
m5 = np.array([
[0,1,0],
[1,1,0],
[0,0,0],
[0,1,1]
])
mat_attesa5 = np.array([
[0,0,1],
[0,1,1],
[0,0,0],
[1,0,1]
])
assert np.allclose(matrot(m5), mat_attesa5)
# FINE TEST
