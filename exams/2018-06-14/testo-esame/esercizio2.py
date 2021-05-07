'''
Esercizio 2


RESTITUISCE un generatore che produce una sequenza dei primi n elevati al quadrato

Esempio

potenza(4) resituirà 

0 (0*0)
1 (1*1)
4 (2*2)
9 (3*3)
16 (4*4)


'''
def potenza(n):
  # scrivi qui


      
# INIZIO TEST - NON TOCCARE !

import types
assert isinstance(potenza(0), types.GeneratorType) # verifico che pari ritorni un generatore e non una lista
            
assert list(potenza(0)) == [0]
assert list(potenza(1)) == [0,1]
assert list(potenza(2)) == [0,1,4]
assert list(potenza(3)) == [0,1,4,9]
assert list(potenza(4)) == [0,1,4,9,16]

# FINE TEST
