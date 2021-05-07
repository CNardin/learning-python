"""

ESERCIZIO 4

Ritorna un generatore che genera una sequenza contenente n stringhe, con queste 
regole:

- si suppone che il primo elemento della sequenza sia ad indice zero

se si sta generando una stringa:
- ad indice pari, la stringa deve contenere la lettera 'a'
- ad indice dispari, la stringa deve contenere la lettera 'b'
- ad indice divisibile per 3, la stringa deve contenere la lettera 'c'. 
  Tale lettera deve essere posta alla fine della stringa
  
Per esempio: 

list(gen(7)) 

deve dare

['ac','b','a','bc','a','b','ac'] 

Perchè

Indice    Stringa   Perchè
  0        'ac'     0 è pari e divisibile per 3
  1        'b'      1 è dispari 
  2        'a'      2 è pari
  3        'bc'     3 è dispari e divisibile per tre
  4        'a'      4 è pari
  5        'b'      5 è dispari 
  6        'ac'     6 è pari e divisibile per tre

Suggerimenti
- se volete usare i moduli, per vedere se un indice i è divisibile per m scrivete i % m == 0
- se avete letto la documentazione dei generatori, in alternativa ai moduli c'è 
  un'altro modo più furbo che potete usare
"""

def gen(n):
    
    # Scrivi qui



# INIZIO TEST - NON TOCCARE !!!


import types
assert isinstance(gen(0), types.GeneratorType) # verifico che pari ritorni un generatore e non una lista
            
assert list(gen(1)) == ['ac']
assert list(gen(2)) == ['ac','b'] 
assert list(gen(3)) == ['ac','b','a']
assert list(gen(4)) == ['ac','b','a','bc']
assert list(gen(5)) == ['ac','b','a','bc','a']
assert list(gen(6)) == ['ac','b','a','bc','a','b'] 
assert list(gen(7)) == ['ac','b','a','bc','a','b','ac'] 

# FINE TEST



