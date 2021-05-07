"""
Prende in input una lista con n numeri interi, e RITORNA una NUOVA lista che 
contiene n tuple ciascuna da due elementi. Ogni tupla contiene un numero 
preso dalla corrispondente posizione della lista di partenza, e il suo doppio. 

Per esempio:

doppie([ 5, 3, 8])

deve dare la nuova lista

[(5,10), (3,6), (8,16)]

"""
def doppie(lista):
    # scrivi qui


# INIZIO TEST - NON TOCCARE !
assert doppie([]) == []
assert doppie([3]) == [(3,6)]
assert doppie([2,7]) == [(2,4),(7,14)]
assert doppie([5,3,8]) == [(5,10), (3,6), (8,16)]
# FINE TEST