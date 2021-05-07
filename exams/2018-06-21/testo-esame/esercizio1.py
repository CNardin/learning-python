"""
ESERCIZIO 1


RITORNA un dizionario in cui le chiavi sono numeri interi da 1 a n inclusi, e i rispettivi 
valori sono i quadrati delle chiavi 

powers(3)

Ritorna

{
 1:1,
 2:4,
 3:9
}

"""
def powers(n):
    # scrivi qui


# INIZIO TEST - NON TOCCARE !!!
assert powers(1) == {1:1}
assert powers(2) == {
                        1:1,
                        2:4
                    }
assert powers(3) == {
                        1:1,
                        2:4,
                        3:9
                    }

assert powers(4) == {
                        1:1,
                        2:4,
                        3:9,
                        4:16
                    }
# FINE TEST
