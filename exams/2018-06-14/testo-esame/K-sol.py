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

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------
# Esercizio 2
"""
Quando si analizza una frase, può essere utile processarla per rimuovere parole molto comuni, come
gli articoli e le preposizioni:
Per esempio:
"un libro su Python per principianti"
si può semplificare in
"libro Python principianti"
Le parole 'poco utili' vengono chiamate 'stopwords'. Questo processo è per esempio eseguito
dai motori di ricerca per ridurre la complessità della stringa di input fornita dall'utente.
Implementare una funzione che prende una stringa e RITORNA la stringa di input senza le
stopwords
SUGGERIMENTO 1: le stringhe in Python sono *immutabili* ! Per rimuovere le parole dovete
creare una _nuova_ stringa a partire dalla stringa di partenza.
SUGGERIMENTO 2: create una lista di parole così:
lista = stringa.split(" ")
SUGGERIMENTO 3: operate le opportune trasformazioni su lista, e poi costruite la stringa
da restituire con " ".join(lista)
"""
def nostop(stringa, stopwords):
	readstr = stringa.split(" ")
	print(readstr)

	for i in range(0,len(stopwords)):
		n = readstr.count(stopwords[i])
		word2remove=stopwords[i]
		print("Parola da rimuovere: \"",word2remove, "\" ",n," volte")

		for j in range(0,n):
			readstr.remove(word2remove)
			print(readstr)
			j =+ 1

	print("finale", " ".join(readstr))
	print("-" * 25)
	return " ".join(readstr)


# INIZIO TEST - NON TOCCARE !
assert nostop("un", ["un"]) == ""
assert nostop("un", []) == "un"
assert nostop("", []) == ""
assert nostop("", ["un"]) == ""
assert nostop("un libro", ["un"]) == "libro"
assert nostop("un libro su Python", ["un","su"]) == "libro Python"
assert nostop("un libro su Python per principianti", ["un","uno","il","su","per"]) == "libro Python principianti"
# FINE TEST
# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------