
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
    # scrivi qui


# INIZIO TEST - NON TOCCARE !

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
