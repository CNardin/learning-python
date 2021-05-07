"""

Esercizio 3 

Prende una matrice come lista di liste in ingresso contenenti zeri e uni, e 
RITORNA una nuova matrice (sempre come lista di liste), costruita prima 
invertendo tutte le righe della matrice di input e poi rovesciando tutte le righe

- Invertire una lista vuol dire trasformare gli 0 in 1 e gli 1 in 0.
  Per esempio,
    [0,1,1] diventa [1,0,0]
    [0,0,1] diventa [1,1,0]
    
- Rovesciare una lista vuol dire che rovesciare l'ordine degli elementi:

    Per esempio 
      [0,1,1] diventa [1,1,0]
      [0,0,1] diventa [1,0,0]

Combinando inversione e rovesciamento, per esempio se partiamo da


[
  [1,1,0,0],
  [0,1,1,0],
  [0,0,1,0]
]


Prima invertiamo ciascun elemento:

[
  [0,0,1,1],
  [1,0,0,1],
  [1,1,0,1]
]


e poi rovesciamo ciascuna riga:

[
  [1,1,0,0],
  [1,0,0,1],
  [1,0,1,1]

]

Suggerimenti

 - per rovesciare una lista usare il metodo .reverse() come in   mia_lista.reverse()
   NOTA: mia_lista.reverse() modifica mia_lista, *non* ritorna una nuova lista !!
 - ricordarsi ll return !!
"""
def flip(matrice):
    
    # Scrvi qui

  
# INIZIO TEST - NON TOCCARE !!!

assert flip([[]]) == [[]]
assert flip([[1]]) == [[0]]
assert flip([[1,0]]) == [[1,0]]
  
m1 = [
      [1,0,0],
      [1,0,1]
     ]
mat_attesa1 = [
    [1,1,0],
    [0,1,0]
]
assert flip(m1) == mat_attesa1
  
  
m2 = [
  [1,1,0,0],
  [0,1,1,0],
  [0,0,1,0]
]

mat_attesa2 = [
  [1,1,0,0],
  [1,0,0,1],
  [1,0,1,1]

]

assert flip(m2) == mat_attesa2

# verifica che l'm originale non è cambiato !
assert m2 == [   
  [1,1,0,0],
  [0,1,1,0],
  [0,0,1,0]
]

# FINE TEST
